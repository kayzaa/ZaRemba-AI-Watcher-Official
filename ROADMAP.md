# 🗺️ ZaRemba AI Watcher – Public Roadmap

This is where we show what is done, what we are building right now and what comes next.
Dates are targets, not promises – security work gets released when it is ready.

**Legend:** ✅ Released · 🔨 In development · 🧪 Testing · 🗓️ Planned · 💡 Exploring

_Last updated: October 2026 (v1.0.0)_

---

## Who we protect first
1. **People who use AI agents** – Claude Code, Cursor, Copilot, OpenClaw, Gemini CLI, Codex and friends. This is where real damage happens today.
2. **Everyone else** – a simple app for home users on PC, phone and tablet.

---

## ✅ v0.1 – AI Inventory Scanner · *Developer Preview* · October 2026
- ✅ Finds installed AI agents, assistants, editor extensions and local model runtimes
- ✅ Audits MCP servers in Claude Desktop, Claude Code, Cursor, Windsurf, Gemini CLI, VS Code and project folders
- ✅ Detects known malicious MCP servers, skills and npm packages
- ✅ Warns about MCP servers that silently auto-update and unencrypted remote servers
- ✅ Flags skills that download and run code or ship password-protected archives
- ✅ Flags agents running with no permission prompts or with the sandbox switched off
- ✅ Finds AI keys stored in plain text – without ever printing them
- ✅ Text and JSON reports, exit codes for scripts and CI
- ✅ Windows, macOS (Apple Silicon + Intel), Linux

## ✅ v0.2 – AI Tripwire · October 2026
- ✅ Decoy files that look like a crypto wallet recovery phrase, a password list, a production `.env` file and API keys – all fake
- ✅ Live alarm when a decoy is changed, moved or deleted (Windows, macOS, Linux)
- ✅ Linux: alarm when a decoy is merely **opened**, including *which* program did it
- ✅ One command each to install, check, watch and remove; changed decoys are kept as evidence
- ✅ Tripwire state and alarms show up in every `zaremba scan`

## ✅ v0.3 – AI Network Watch · October 2026
- ✅ Shows which program talks to which AI service – 13 cloud AI providers plus local Ollama and LM Studio servers
- ✅ Flags unknown programs, script hosts, abused Windows system tools and programs running from temp/download folders – the pattern used by AI-powered malware
- ✅ Live watch mode with history log
- ✅ Trusted list for the programs you know
- ✅ Metadata only – traffic is never read

## ✅ v0.4 – Real-time Agent Guard & MCP Firewall · October 2026
- ✅ One rule set for every agent, connected through official hooks: **Claude Code** (verified), Gemini CLI, Cursor, Windsurf, GitHub Copilot CLI (experimental)
- ✅ No-go zones: SSH keys, cloud logins, tokens, keychains, browser passwords & cookies, crypto wallets, tripwire decoys
- ✅ Blocks download-and-run, agents launched without safety prompts (s1ngularity), disk wipes, attempts to switch ZaRemba off
- ✅ Asks before `.env` reads, uploads, autostart changes and paste/webhook services
- ✅ MCP Firewall for every MCP app: blocks dangerous calls, rug-pull protection (pinned tools), poisoned-tool quarantine
- ✅ Install/uninstall restore your settings exactly

## ✅ v1.0 – Desktop App · October 2026
- ✅ Desktop app for Windows, macOS (Apple Silicon + Intel) and Linux with one-click protection and live protection score
- ✅ Background protection in the tray: tripwire alarms, AI network watch, live Agent Guard / MCP Firewall alerts, notifications
- ✅ Signed automatic app updates (verified against ZaRemba's release key before installing)
- ✅ Daily threat-intelligence research team; signed feed delivered automatically to every app
- ✅ Starts with your computer (optional), English interface

## 🔨 v1.1 – Trust & depth · *in development*
- 🗓️ Installers signed with Microsoft and Apple developer certificates (no first-launch warnings)
- 🗓️ Tripwire read-detection on Windows and macOS (driver / Endpoint Security)
- 🗓️ Network Watch from system events instead of polling – catches even very short connections
- 🗓️ Confirm Gemini CLI, Cursor, Windsurf and Copilot CLI integrations on real installs; add more agents as they ship hooks
- 🗓️ German interface

## 🗓️ v1.x – Every device
- 🗓️ **Browser extension** (Chrome, Edge, Firefox, Safari): Prompt-Injection Shield – spots hidden instructions aimed at AI browsers
- 🗓️ **Android**: Fake-AI-app check, AI network watch, scam protection
- 🗓️ **iPhone & iPad**: Safari protection, link and media checks (Apple does not allow scanning other apps)
- 💡 **Deepfake & voice-clone warning** for calls, videos and voice messages

## 💡 Later
- 💡 ZaRemba for Teams & Servers – protection for companies and AI infrastructure
- 💡 Independent lab testing (AV-TEST / AV-Comparatives)
- 💡 Public threat feed of malicious AI extensions

---

### Have an idea or need something first?
[Suggest a feature](https://github.com/kayzaa/ZaRemba-AI-Watcher-Official/issues/new?template=feature_request.yml) –
the most requested features move up the list.
