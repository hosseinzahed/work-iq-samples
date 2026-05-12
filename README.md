# 💡 Work IQ Samples

This repository contains sample projects demonstrating how to use **WorkIQ** and related MCP (Model Context Protocol) tools for building intelligent agent solutions with Microsoft 365 Copilot extensibility.

---

## 📚 What is WorkIQ?

WorkIQ is a framework and set of APIs for extending Microsoft 365 Copilot with custom agents, tools, and workflows. It enables developers to build, test, and integrate their own intelligence into Microsoft 365 experiences.

![WorkIQ Layers Diagram](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/assets/diagrams/work-iq-layers.png)

---

## 🧑‍💻 Example Projects

This repo includes:

| File | Description |
|---|---|
| **`src/agent_with_workiq.py`** | Agent that connects to the WorkIQ MCP server using `MCPStdioTool` and exposes a development UI via `agent_framework.devui`. |
| **`src/agent_with_email_tools.py`** | Agent combining the WorkIQ MCP server with the Microsoft 365 Mail Tools MCP server (`MCPStreamableHTTPTool`) for email automation. |
| **`src/chainlit_app.py`** | Interactive Chainlit chat UI backed by a WorkIQ-enabled agent, with session management and streaming responses. |

---

## 🤖 GitHub Copilot Agent — `workiq-agent`

This workspace ships a custom **`workiq-agent`** that is available directly inside VS Code via GitHub Copilot Chat. The agent is pre-configured to call the `mcp_workiq_ask_work_iq` tool, giving you a conversational interface to Work IQ data without writing any code.

To use it, open the Copilot Chat panel in VS Code and select **workiq-agent** from the agent list (or type `@workiq-agent` in the chat input).

---

## 🔗 Key Documentation & Resources

| Link | Description |
|---|---|
| [WorkIQ Overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq) | Introduction to WorkIQ and its extensibility model |
| [Tooling Servers Overview](https://learn.microsoft.com/en-us/microsoft-agent-365/tooling-servers-overview) | Overview of MCP tooling servers and their capabilities |
| [Mail Tools Server Reference](https://learn.microsoft.com/en-us/microsoft-agent-365/mcp-server-reference/mail) | Reference for MCP Mail Tools server APIs |
| [WorkIQ API Overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq-api-overview) | API details for WorkIQ extensibility |
| [WorkIQ CLI](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq-cli) | Command-line interface for WorkIQ development |
| [WorkIQ GitHub Repo](https://github.com/microsoft/work-iq) | Official WorkIQ source code and releases |

---

## 🛠️ Supported MCP Tools (for .vscode/mcp.json)

You can configure the following MCP tools in your `.vscode/mcp.json` file to enable various Microsoft 365 agent capabilities:

```json
{
  "servers": {
    "workiq": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@microsoft/workiq@0.2.8", "mcp"]
    },
    "powerbi-remote-tools": {
      "type": "http",
      "url": "https://api.fabric.microsoft.com/v1/mcp/powerbi"
    },
    "calendar-tools": {
      "type": "http",
      "url": "https://agent365.svc.cloud.microsoft/agents/tenants/{tenant-id}/servers/mcp_CalendarTools",
      "headers": {}
    },
    "teams-tools": {
      "type": "http",
      "url": "https://agent365.svc.cloud.microsoft/agents/tenants/{tenant-id}/servers/mcp_TeamsServer",
      "headers": {}
    },
    "mail-tools": {
      "type": "http",
      "url": "https://agent365.svc.cloud.microsoft/agents/tenants/{tenant-id}/servers/mcp_MailTools",
      "headers": {}
    },
    "sharepoint-tools": {
      "type": "http",
      "url": "https://agent365.svc.cloud.microsoft/agents/tenants/{tenant-id}/servers/mcp_ODSPRemoteServer",
      "headers": {}
    },
    "word-tools": {
      "type": "http",
      "url": "https://agent365.svc.cloud.microsoft/agents/tenants/{tenant-id}/servers/mcp_WordServer",
      "headers": {}
    }
  }
}
```

Replace `{tenant-id}` with your actual Microsoft 365 tenant ID.

---

## 🚀 Getting Started

Follow these steps to clone and run the project:

1. **Clone the repository**

   ```sh
   git clone https://github.com/hosseinzahed/work-iq-samples.git
   cd work-iq-samples
   ```

2. **(Optional) Create and activate a Python virtual environment**

   ```sh
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Copy `.sample.env` to `.env` and fill in the required values:

   ```sh
   cp .sample.env .env
   ```

   | Variable | Description |
   |---|---|
   | `FOUNDRY_PROJECT_ENDPOINT` | Azure AI Foundry project endpoint URL |
   | `MODEL_DEPLOYMENT_NAME` | Model deployment name (e.g. `gpt-4.1`) |
   | `AZURE_TENANT_ID` | Azure AD tenant ID for Foundry authentication |
   | `WORK_TENANT_ID` | Microsoft 365 tenant ID for Mail/Calendar/Teams tools |

5. **Run the WorkIQ agent example**

   ```sh
   cd src
   python agent_with_workiq.py
   ```

6. **Run the agent with email tools**

   ```sh
   cd src
   python agent_with_email_tools.py
   ```

7. **Run the Chainlit app**

   ```sh
   cd src
   chainlit run chainlit_app.py
   ```

---

## 📝 Notes

- Make sure you have Python 3.10+ and Node.js installed.
- The WorkIQ MCP package used in the samples is `@microsoft/workiq@0.2.8`.
- For MCP tools, ensure you have access to the required Microsoft 365 tenant and the necessary permissions.
- The `workiq-agent` in VS Code uses the MCP server configured in `.vscode/mcp.json` — make sure it is set up before using the Copilot Chat agent.
- See the linked documentation above for more details on each tool and API.