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

## Agent Guard
| Rule | Decision | What it means |
|---|---|---|
| `ZRW-GRD-001` | DENY | Access to a no-go zone (credentials, browser secrets, wallets, ZaRemba itself) |
| `ZRW-GRD-002` | DENY | An agent touched an AI Tripwire decoy |
| `ZRW-GRD-003` | ASK | Reading a `.env` file |
| `ZRW-GRD-004` | DENY | Download-and-run command |
| `ZRW-GRD-005` | DENY | Starting an AI agent with safety prompts switched off |
| `ZRW-GRD-006` | ASK | Uploading a local file |
| `ZRW-GRD-007` | ASK | Autostart / persistence change |
| `ZRW-GRD-008` | DENY | Wiping the home folder or a disk |
| `ZRW-GRD-009` | ASK | Paste, webhook or tunnel service |
| `ZRW-GRD-010` | DENY | Switching ZaRemba off |
| `ZRW-GRD-020` | WARN | Injection Shield: a tool result (web page, file, MCP answer) contains hidden instructions – the agent is told to treat it as data, you get a notice |
| `ZRW-GRD-100` | INFO | Agent is protected by the Agent Guard |
| `ZRW-GRD-101` | LOW | Agent is installed but not protected |

## Agent forensics (past sessions) – new in 1.2
| Rule | Severity | What it means |
|---|---|---|
| `ZRW-AUD-001` | HIGH / MEDIUM | In a past session the agent read content with hidden AI instructions (HIGH when it came from the web or an MCP tool) |
| `ZRW-AUD-002` | HIGH | In a past session the agent did something the Agent Guard blocks today (calls that were blocked are not counted) |
| `ZRW-AUD-003` | MEDIUM | AI keys are stored in plain text in an agent's chat history |

Claude Code sessions of the last 90 days are checked (`~/.claude/projects`). Secret values never appear in reports.

## Deep scan – new in 1.2
| Rule | Severity | What it means |
|---|---|---|
| `ZRW-MEM-001` | HIGH | An agent rules / memory file (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `.cursorrules`, `.windsurfrules`, Copilot instructions, Cursor/Windsurf rules) hides orders: invisible characters, orders inside HTML comments, or "override the user" plus a risky action |
| `ZRW-IDE-001` | CRITICAL | A VS Code / Cursor / Windsurf / VSCodium extension contains invisible-character code (technique of the GlassWorm worm, 2025) |
| `ZRW-IDE-002` | CRITICAL | An installed extension is named in public GlassWorm reports |
| `ZRW-MDL-001` | CRITICAL | An AI model file (pickle-based: `.pt`, `.pth`, `.bin`, `.pkl`, `.ckpt`, `.joblib`) would run commands or code when loaded (`os.system`, `subprocess`, `exec`, sockets …). Files are only read, never loaded |
| `ZRW-MDL-002` | MEDIUM | A model file is packed as 7z – used by the nullifAI technique to slip past model scanners |
| `ZRW-MAL-001` | HIGH | A script calls an AI model API, asks it for commands or code and runs the answer – the pattern of AI-steered malware such as LameHug and PROMPTFLUX |
| `ZRW-MAL-002` | HIGH | A script starts an AI agent CLI with its safety prompts switched off (s1ngularity pattern) |

Model and malware checks look in Downloads, Desktop, Documents, autostart folders, the Hugging Face / PyTorch caches and
the project folders you pass with `--project`.

## MCP Firewall (log events)
| Event | Meaning |
|---|---|
| `blocked_call` | A tool call was blocked by an Agent Guard rule |
| `warned_call` | A tool call that would need your OK was let through and logged |
| `changed_tool` | A tool's definition changed since it was pinned – quarantined |
| `poisoned_tool` | A tool's description contains hidden instructions – quarantined |
| `pinned` | A server added a new tool |

## Threat database
The built-in database covers publicly documented incidents, for example the **s1ngularity / Nx** supply-chain attack and the
**postmark-mcp** malicious MCP server. Know of another one?
[Report it](https://github.com/kayzaa/ZaRemba-AI-Watcher-Official/issues/new?template=threat_report.yml).
