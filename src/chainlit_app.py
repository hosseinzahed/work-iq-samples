"""AG-UI server example."""

import os
from dotenv import load_dotenv
from azure.identity import AzureDeveloperCliCredential
from agent_framework import Agent, MCPStdioTool, Message, AgentSession
from agent_framework.foundry import FoundryChatClient
from agent_framework.observability import configure_otel_providers
import chainlit as cl
from typing import List
from engineio.payload import Payload
import socketio

# Set the buffer size to 10MB or use a configurable value from the environment
MAX_HTTP_BUFFER_SIZE = int(os.getenv("MAX_HTTP_BUFFER_SIZE", 100_000_000))
# Configurable buffer size
sio = socketio.AsyncServer(
    async_mode='aiohttp',
    transport='websocket',
    max_http_buffer_size=MAX_HTTP_BUFFER_SIZE)
Payload.max_decode_packets = 500

# Load environment variables from .env file, overriding existing ones
load_dotenv(override=True)

configure_otel_providers()

# Initialize the FoundryChatClient with credentials and
# model information from environment variables
foundry_client = FoundryChatClient(
    project_endpoint=os.getenv("FOUNDRY_PROJECT_ENDPOINT"),
    credential=AzureDeveloperCliCredential(),
    model=os.getenv("MODEL_DEPLOYMENT_NAME")
)

# Define a tool for interacting with Microsoft Work IQ capabilities
work_iq_mcp_tool = MCPStdioTool(
    name="work-iq-mcp-tool",
    command="npx",
    args=["-y", "@microsoft/workiq@latest", "mcp"],
    load_prompts=False
)

# Create an agent that will interact with Microsoft
# Work IQ capabilities using the FoundryChatClient
agent = Agent(
    name="simple-work-iq-agent",
    instructions="""
    You're an agent that can interact with 
    Microsoft Work IQ capabilities using the work-iq-mcp-tool.
    Use the work-iq-mcp-tool to execute commands related to Work IQ.
    """,
    client=foundry_client,
    tools=[work_iq_mcp_tool],
    default_options={
        "allow_multiple_tool_calls": False,
    },
)


@cl.on_chat_start
async def on_chat_start():

    # Initialize an empty chat history
    chat_history: list[Message] = []
    cl.user_session.set("chat_history", chat_history)

    # Initialize empty chat thread
    cl.user_session.set("chat_session", None)


@cl.on_message
async def on_message(user_message: cl.Message):

    # Retrieve chat history
    chat_history: list[Message] = cl.user_session.get("chat_history")

    # Get chat session from user session or create a new one if it doesn't exist
    chat_session: AgentSession = cl.user_session.get("chat_session")
    if not chat_session:
        # Create a new chat session for the agent
        chat_session = agent.create_session()
        print(f"Created new chat session with ID: {chat_session.session_id}")

    # Append user message to chat history
    chat_history.append(Message(role="user", contents=user_message.content))
    cl.user_session.set("chat_history", chat_history)

    answer = cl.Message(content="")

    # Stream the agent's response token by token
    async for chunk in agent.run(
            messages=chat_history,
            session=chat_session,
            stream=True
    ):
        # Append token to the answer content
        if chunk.text:
            await answer.stream_token(chunk.text)

    # Update chat history and thread
    cl.user_session.set("chat_session", chat_session)
    chat_history.append(Message(role="assistant", contents=answer.content))

    # Send the final message
    await answer.send()


@cl.set_starters  # type: ignore
async def set_starts() -> List[cl.Starter]:
    return [
        cl.Starter(
            label="Today's meetings",
            message="What meetings do I have today?",
        ),
        cl.Starter(
            label="Email summary",
            message="Can you summarize my unread emails?",
        )
    ]
