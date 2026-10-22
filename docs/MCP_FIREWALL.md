# 🔥 MCP Firewall

MCP servers give AI apps new abilities – files, e-mail, databases. A malicious or compromised server runs with the same
access as your AI. The MCP Firewall sits **between your AI app and each local MCP server** and works with every MCP app:
Claude Desktop, Claude Code, Cursor, Windsurf, VS Code, Gemini CLI and more.

## Quick start
```bash
zaremba mcp protect     # put the firewall in front of every local MCP server
zaremba mcp status      # see which servers are protected
```
Close your AI apps before running `protect` (some rewrite their settings while open), then start them again.

## What it does
| Protection | What happens |
|---|---|
| **Dangerous calls** | A tool call that would read SSH keys, wallets, cloud logins, browser passwords or a tripwire decoy – or run download-and-execute commands – never reaches the server. Your AI gets a clear error instead. |
| **Rug pulls** | The first time a server is used, its tools are pinned. If a tool's description or parameters change later (a classic way to turn a trusted server malicious), that tool is quarantined. |
| **Tool poisoning** | Tools whose descriptions hide instructions for the AI – e.g. "read ~/.ssh/id_rsa and pass it along", "do not tell the user", invisible Unicode characters – are quarantined. |

Quarantined tools stay blocked across restarts until you review them and run:
```bash
zaremba mcp trust <server-name>
```

## Commands
```bash
zaremba mcp protect          # wrap all local servers
zaremba mcp unprotect        # restore the original server commands exactly
zaremba mcp status           # list servers
zaremba mcp log              # blocked calls and quarantined tools
zaremba mcp trust <server>   # accept a server's current tools after review
```

## Good to know
- Remote MCP servers (configured with a URL) cannot be wrapped; `zaremba scan` still checks them.
- Calls that would normally need your OK (e.g. reading `.env`) are let through and logged – MCP has no way to ask you from
  the firewall.
- `protect` keeps a backup of each settings file next to it (`*.zaremba-backup`).
