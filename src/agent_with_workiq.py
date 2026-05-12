import os
from dotenv import load_dotenv
from azure.identity import AzureDeveloperCliCredential, AzureCliCredential
from agent_framework import Agent, MCPStdioTool
from agent_framework.foundry import FoundryChatClient
from agent_framework.devui import serve
from agent_framework.observability import configure_otel_providers

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
    args= ["-y", "@microsoft/workiq@0.2.8", "mcp"],
    load_prompts=False
)

# Create an agent that will interact with Microsoft
# Work IQ capabilities using the FoundryChatClient
agent = Agent(
    name="agent-with-workiq",
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

# Serve the agent using the development UI
if __name__ == "__main__":
    serve(entities=[agent],
          host="localhost",
          port=8000,
          auto_open=True)
