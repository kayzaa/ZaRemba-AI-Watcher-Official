# Detection rules

Every finding has a stable rule ID, so you can search for it, filter it in JSON output or report a false positive.

| Severity | Meaning |
|---|---|
| 🟥 **CRITICAL** | A known malicious component is present. Act now. |
| 🟧 **HIGH** | A setting or extension that attackers actively abuse. Fix soon. |
| 🟨 **MEDIUM** | A weakness that makes an attack easier. Fix when you can. |
| 🟦 **LOW** | Worth a look. |
| ⬜ **INFO** | Inventory – shown with `--all`. Nothing wrong. |

## AI Inventory
| Rule | Severity | What it means |
|---|---|---|
| `ZRW-INV-001` | INFO | An AI agent, assistant or local model runtime is installed |
| `ZRW-INV-002` | INFO | An AI coding agent is installed as a VS Code extension |

## MCP servers
| Rule | Severity | What it means |
|---|---|---|
| `ZRW-MCP-001` | INFO | An MCP server is configured for one of your AI clients |
| `ZRW-MCP-002` | CRITICAL | The MCP server is on the list of known malicious servers |
| `ZRW-MCP-003` | MEDIUM | The server starts without a fixed version and can change with any update |
| `ZRW-MCP-004` | MEDIUM | The server is reached over unencrypted `http://` on the internet |
| `ZRW-MCP-005` | MEDIUM | An AI key is stored in plain text in the MCP configuration |

## Agent skills
| Rule | Severity | What it means |
|---|---|---|
| `ZRW-SKL-001` | INFO | A skill is installed (OpenClaw, Claude Code) |
| `ZRW-SKL-002` | CRITICAL | The skill is on the list of known malicious skills |
| `ZRW-SKL-003` | HIGH | The skill's instructions download a script and run it immediately |
| `ZRW-SKL-004` | HIGH | The skill asks you to open a password-protected archive |

## Agent settings
| Rule | Severity | What it means |
|---|---|---|
| `ZRW-CFG-001` | HIGH | Claude Code is set to bypass all permission prompts |
| `ZRW-CFG-002` | MEDIUM | Claude Code may run every shell command without asking |
| `ZRW-CFG-003` | HIGH | Codex CLI never asks before acting |
| `ZRW-CFG-004` | HIGH | Codex CLI sandbox is switched off |

## Secrets
| Rule | Severity | What it means |
|---|---|---|
| `ZRW-SEC-001` | MEDIUM | An AI or GitHub key is stored in plain text in a shell profile or `.env` file |

Detected key types: OpenAI, Anthropic, Google AI (Gemini), Hugging Face, OpenRouter, GitHub. Values are never shown.

## Packages
| Rule | Severity | What it means |
|---|---|---|
| `ZRW-PKG-001` | CRITICAL | A known malicious npm package version is installed |

## AI Tripwire
| Rule | Severity | What it means |
|---|---|---|
| `ZRW-TRP-001` | INFO | A decoy is armed and untouched |
| `ZRW-TRP-002` | HIGH | A decoy file was changed |
| `ZRW-TRP-003` | HIGH | A decoy file was deleted or moved |
| `ZRW-TRP-004` | HIGH | Live tripwire alarms were recorded |

## Threat database
The built-in database covers publicly documented incidents, for example the **s1ngularity / Nx** supply-chain attack and the
**postmark-mcp** malicious MCP server. Know of another one?
[Report it](https://github.com/kayzaa/ZaRemba-AI-Watcher-Official/issues/new?template=threat_report.yml).
