# Changelog

All notable changes to ZaRemba AI Watcher are listed here.
Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.3.0] – 2026-10 · Browser extension 1.3.0 · Android 1.1.0
### Added
- **One signed threat list for every device**: the threat database now also lists malicious IDE extensions, browser
  extensions and Android apps. The **browser extension** (1.3.0) and the **Android app** (1.1.0) download it, verify
  its signature with the same ZaRemba intel key as the desktop app and use it – new threats arrive without an app
  update. Android: can be switched off in Settings.
### Changed
- `ZRW-IDE-002` (malicious IDE extension) now uses the signed threat list and respects affected versions.

## [1.2.0] – 2026-10
### Added
- **Injection Shield for agents** (`ZRW-GRD-020`): Agent Guard now also hooks `PostToolUse` (Claude Code) and
  `AfterTool` (Gemini CLI, experimental). Tool results with hidden instructions or invisible-character payloads are
  flagged; the agent is told to treat them as data and you see a notice. Existing installs are upgraded automatically.
- **Agent forensics** (`ZRW-AUD-001…003`): every scan reviews Claude Code sessions of the last 90 days.
- **Deep scan**: poisoned agent rules files (`ZRW-MEM-001`), IDE extensions with invisible code or named in GlassWorm
  reports (`ZRW-IDE-001/002`), malicious AI model files (`ZRW-MDL-001/002`), AI-steered malware scripts and AI CLIs
  started without safety prompts (`ZRW-MAL-001/002`).
- **Attack Lab**: `zaremba lab` – 26 harmless attack simulations, 26 detected. See [Attack Lab](docs/ATTACK_LAB.md).
### Changed
- Example/dummy keys from documentation are no longer reported as secrets.
- Text written with `echo` / `printf` is treated as data, not as a command, unless it is piped into a shell.

## [Android 1.0.0] – 2026-10
### Added
- **ZaRemba AI Watcher for Android** (APK, Android 8+): fake AI app detection, known malicious apps, apps from
  outside a store with Accessibility / device admin / notification / SMS access, apps allowed to install other apps,
  AI apps overview, text check (Share → *Check with ZaRemba*), background checks with alerts, update check.
  See [Android](docs/ANDROID.md).

## [1.1.0] – 2026-10
### Added
- **Quarantine** for malicious findings: one click takes an MCP server, agent skill or poisoned package folder out of
  action; **Restore** puts it back exactly, **Delete** (two clicks) removes it for good. New **Quarantine** page.
- **Automatic quarantine** (optional, switched on by *Protect everything*): critical matches from the signed threat
  database are quarantined as soon as they are found. Nothing is ever deleted automatically.
- **Bring your own AI** (optional): connect Anthropic, OpenAI, Google Gemini, a local Ollama model or your installed
  Claude Code. **Ask AI** explains any finding in plain language; **Second opinion** rates a skill or MCP server as
  safe / suspicious / malicious. You see the exact text before it is sent, secrets are removed first, keys live in the
  system keychain, and the AI only advises.
- Command line: `zaremba quarantine list | auto | restore | delete`.
- **Browser extension 1.2.0 – developer preview** (Chrome, Edge, Brave, Opera, Firefox), attached to this release:
  Prompt-Injection Shield (hidden instructions for AI assistants: hidden/tiny/transparent/off-screen text, comments,
  image descriptions, invisible Unicode characters; neutralize and restore), secret paste guard for 16 AI chats,
  check against 34 known malicious AI extensions. See [Browser extension](docs/BROWSER_EXTENSION.md).
### Changed
- Threat-intelligence files may contain new kinds of entries in the future; this version safely ignores kinds it does
  not know instead of rejecting the whole file.

## [1.0.0] – 2026-10
### Added
- **Desktop app** for Windows, macOS (Apple Silicon + Intel) and Linux: overview with protection score,
  **Protect everything** in one click, AI Agents, MCP Firewall, AI Tripwire, Network Watch, Scan, Activity, Settings.
- Background protection from the tray with system notifications; optional start with the computer.
- **Signed automatic updates** of the app (minisign release key; forged updates are rejected).
- **Signed threat intelligence feed**: downloaded automatically (desktop every 4 h, CLI `zaremba update`), verified
  against the intel key and a quality gate; maintained daily by the ZaRemba research team.
- The command-line program is bundled with the desktop app (AI agents and MCP configs call it).
### Changed
- Network downloads trust the operating system's certificate store (works behind company proxies).

## [0.4.0] – Developer Preview – 2026-10
### Added
- **Agent Guard**: `zaremba guard install | uninstall | status | test | log`.
  - Connects through official hooks of Claude Code (verified in a real session), Gemini CLI, Cursor, Windsurf and
    GitHub Copilot CLI (experimental).
  - Blocks: no-go zones (SSH, cloud logins, tokens, keychains, browser passwords/cookies, crypto wallets), tripwire
    decoys, download-and-run, agents launched without safety prompts, disk wipes, switching ZaRemba off.
  - Asks before: `.env` reads, file uploads, autostart/persistence changes, paste/webhook/tunnel services.
  - Settings are restored exactly on uninstall; broken settings files are never touched.
- **MCP Firewall**: `zaremba mcp protect | unprotect | status | trust | log`.
  - Blocks dangerous tool calls, pins tool definitions (rug-pull protection), quarantines tools with hidden
    instructions or invisible characters. Quarantine persists across restarts.
- `zaremba scan` now reminds you when an installed agent is not protected (`ZRW-GRD-100/101`).

## [0.3.0] – Developer Preview – 2026-10
### Added
- **AI Network Watch**: `zaremba net [check | watch | allow | disallow | allowed | history]`.
  - Shows which program is connected to which AI service: OpenAI, ChatGPT, Anthropic, Claude, Google Gemini, Vertex AI,
    Hugging Face, OpenRouter, Mistral, DeepSeek, Groq, Together AI, Perplexity, xAI, Cohere, Alibaba Qwen, plus local
    Ollama and LM Studio servers.
  - Verdicts: expected (browsers, AI apps), script host, unknown, high risk (abused system tools such as wscript/mshta,
    or programs running from temp/download folders), trusted by you.
  - Watch mode reports every new program once and keeps a history log.
  - Exit codes: `2` high risk · `1` unknown program · `0` otherwise.

## [0.2.0] – Developer Preview – 2026-10
### Added
- **AI Tripwire**: `zaremba tripwire install | status | watch | alerts | remove`.
  - Four fake decoys: wallet recovery phrase, password list, production `.env`, API keys. Existing files are never overwritten.
  - Live alarms on change, move and delete (all platforms); on Linux also on open, with the responsible program.
  - Status checks never open the decoys, so checking does not trip the alarm.
  - Changed decoys are kept as evidence on `remove` unless `--force` is used.
- New scan rules `ZRW-TRP-001` … `ZRW-TRP-004`.

## [0.1.0] – Developer Preview – 2026-10
### Added
- `zaremba scan`: read-only AI Inventory scanner for Windows, macOS and Linux.
- AI agent inventory: Claude Code, Claude Desktop, Cursor, Windsurf, GitHub Copilot, Cline, Roo Code, Continue,
  Gemini CLI, Gemini Code Assist, Codex CLI, Amazon Q Developer CLI, OpenClaw, Ollama, LM Studio.
- MCP server audit across Claude Desktop, Claude Code, Cursor, Windsurf, Gemini CLI, VS Code and project configs.
- Skill audit for OpenClaw and Claude Code skills.
- Risky-setting checks for Claude Code and Codex CLI.
- Plain-text AI key detection (redacted output).
- Known-malicious npm package detection (global and per project).
- Built-in threat database, text and JSON reports, exit codes.
