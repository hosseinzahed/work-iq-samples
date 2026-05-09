# 💡 Work IQ Samples

This repository contains sample projects demonstrating how to use **Work WorkIQ** and related MCP (Model Context Protocol) tools for building intelligent agent solutions with Microsoft 365 Copilot extensibility.

---

## 📚 What is WorkIQ?

WorkIQ is a framework and set of APIs for extending Microsoft 365 Copilot with custom agents, tools, and workflows. It enables developers to build, test, and integrate their own intelligence into Microsoft 365 experiences.

![WorkIQ Layers Diagram](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/assets/diagrams/work-iq-layers.png)

---

## 🧑‍💻 Example Projects

This repo includes:

- **agent_with_workiq.py**: Example of integrating with the WorkIQ MCP server.
- **agent_with_email_tools.py**: Example of using MCP Mail Tools for email automation.
- **chainlit_app.py**: Example Chainlit app for interactive agent demos.

---

## 🔗 Key Documentation & Resources

| Link                                                                                                              | Description                                            |
| ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| [WorkIQ Overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq)                  | Introduction to WorkIQ and its extensibility model     |
| [Tooling Servers Overview](https://learn.microsoft.com/en-us/microsoft-agent-365/tooling-servers-overview)        | Overview of MCP tooling servers and their capabilities |
| [Mail Tools Server Reference](https://learn.microsoft.com/en-us/microsoft-agent-365/mcp-server-reference/mail)    | Reference for MCP Mail Tools server APIs               |
| [WorkIQ API Overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq-api-overview) | API details for WorkIQ extensibility                   |
| [WorkIQ CLI](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq-cli)                   | Command-line interface for WorkIQ development          |
| [WorkIQ GitHub Repo](https://github.com/microsoft/work-iq)                                                        | Official WorkIQ source code and releases               |

---

## 🛠️ Supported MCP Tools (for .vscode/mcp.json)

You can configure the following MCP tools in your `.vscode/mcp.json` file to enable various Microsoft 365 agent capabilities:

```json
{
  "servers": {
    "workiq": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@microsoft/workiq@latest", "mcp"]
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
   git clone https://github.com/hosseinzahed/microsoft-iq-samples.git
   cd microsoft-iq-samples
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

4. **Run the WorkIQ agent example**

   ```sh
   cd src
   python agent_with_workiq.py
   ```

5. **Run the Chainlit app**
   ```sh
   chainlit run chainlit_app.py
   ```

---

## 📝 Notes

- Make sure you have Python 3.8+ and Node.js installed.
- For MCP tools, ensure you have access to the required Microsoft 365 tenant and permissions.
- See the provided links above for more details on each tool and API.