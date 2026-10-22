# 🗺️ ZaRemba AI Watcher – Public Roadmap

This is where we show what is done, what we are building right now and what comes next.
Dates are targets, not promises – security work gets released when it is ready.

**Legend:** ✅ Released · 🔨 In development · 🧪 Testing · 🗓️ Planned · 💡 Exploring

_Last updated: October 2026_

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

## 🔨 v0.2 – AI Tripwire · *in development*
- 🔨 Decoy files that look like crypto wallets, password lists, `.env` files and AI keys
- 🔨 Instant alarm when any program or AI agent opens them – shows *which* program did it
- 🗓️ Optional "AI tripwire" text inside decoys that makes a reading AI reveal itself
- 🗓️ One command to install, check and remove all decoys

## 🗓️ v0.3 – AI Network Watch
- 🗓️ Shows which program talks to which AI service (OpenAI, Anthropic, Google, Hugging Face, OpenRouter …)
- 🗓️ Alarm when an unknown program secretly calls an AI service – the pattern used by AI-powered malware
- 🗓️ Allow-list for the AI apps you trust

## 🗓️ v0.4 – Real-time Agent Guard & MCP Firewall
- 🗓️ No-go zones for AI agents: wallets, SSH keys, browser passwords, AI keys
- 🗓️ Blocks dangerous command patterns (download-and-run, secret harvesting)
- 🗓️ MCP Firewall: sits between your agent and its MCP servers, blocks hidden data leaks
- 🗓️ Integrations through official agent hooks – no hacks

## 🗓️ v1.0 – Desktop App · Windows & macOS
- 🗓️ Beautiful app with one-click scan and live protection
- 🗓️ Background service, tray icon and notifications
- 🗓️ Signed installers (Windows code signing, Apple notarization)
- 🗓️ Automatic, signed threat-database updates
- 🗓️ Languages: English, German, more to follow

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
