"""Agent with email tools example."""

import os
from dotenv import load_dotenv
from azure.identity import AzureDeveloperCliCredential, AzureCliCredential, get_bearer_token_provider
from agent_framework import Agent, MCPStdioTool, MCPStreamableHTTPTool
from agent_framework.foundry import FoundryChatClient
from agent_framework.devui import serve

# Load environment variables from .env file, overriding existing ones
load_dotenv(override=True)

# Initialize the FoundryChatClient with credentials and
# model information from environment variables
foundry_client = FoundryChatClient(
    project_endpoint=os.getenv("FOUNDRY_PROJECT_ENDPOINT"),
    credential=AzureDeveloperCliCredential(),
    model=os.getenv("MODEL_DEPLOYMENT_NAME")
)

# Define a tool for interacting with Microsoft Work IQ capabilities
work_iq_mcp = MCPStdioTool(
    name="work-iq-mcp",
    command="npx",
    args=["-y", "@microsoft/workiq@latest", "mcp"],
    load_prompts=False
)

# Setup authentication for email tool. The credential caches tokens
# internally and refreshes them automatically when they expire.
credential = AzureCliCredential(tenant_id=os.getenv("WORK_TENANT_ID"))
get_agent365_token = get_bearer_token_provider(
    credential,
    f"https://agent365.svc.cloud.microsoft/agents/tenants/{os.getenv('WORK_TENANT_ID')}/servers/mcp_MailTools/.default"
)
print(get_agent365_token())

def get_email_headers(_kwargs: dict[str, object]) -> dict[str, str]:
    return {"Authorization": f"Bearer {get_agent365_token()}"}

# Define a tool for interacting with email capabilities
email_tools = MCPStreamableHTTPTool(
    name="email-tools",
    url=f"https://agent365.svc.cloud.microsoft/agents/tenants/{os.getenv('WORK_TENANT_ID')}/servers/mcp_MailTools",
    header_provider=get_email_headers,
    load_prompts=False,
)

# Create an agent that will interact with Microsoft
# Work IQ capabilities using the FoundryChatClient
agent = Agent(
    name="simple-work-iq-agent",
    instructions="""
    You're an agent that can interact with 
    Microsoft Work IQ capabilities using the work-iq-mcp-tool.
    Use the provided tools to execute commands related to Work IQ and email.
    """,
    client=foundry_client,
    tools=[work_iq_mcp, email_tools]
)

# Serve the agent using the development UI
if __name__ == "__main__":
    serve(entities=[agent],
          host="localhost",
          port=8000,
          auto_open=True)
