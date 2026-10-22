# 🗺️ ZaRemba AI Watcher – Public Roadmap

This is where we show what is done, what we are building right now and what comes next.
Dates are targets, not promises – security work gets released when it is ready.

**Legend:** ✅ Released · 🔨 In development · 🧪 Testing · 🗓️ Planned · 💡 Exploring

_Last updated: October 2026 (v1.3.0)_

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

## ✅ v1.1 – Quarantine & bring your own AI · October 2026
- ✅ One-click **Quarantine** for malicious MCP servers, skills and packages – restore exactly or delete for good
- ✅ Optional **automatic quarantine** of known threats from the signed threat database
- ✅ **Bring your own AI**: Anthropic, OpenAI, Google Gemini, local Ollama or your installed Claude Code explains findings and gives second opinions – you see every word before it is sent, keys stay in your system keychain
- ✅ Threat updates are future-proof: new kinds of entries never break older versions

## ✅ v1.2 – Deep defense · October 2026
- ✅ **Injection Shield for agents**: Claude Code (verified) and Gemini CLI check every tool result for hidden instructions
- ✅ **Agent forensics**: past sessions checked for injected content, dangerous actions and keys left in the chat history
- ✅ **Deep scan**: poisoned agent rules files, IDE extensions with invisible code (GlassWorm), malicious AI model files (pickle, nullifAI), AI-steered malware scripts (LameHug / PROMPTFLUX pattern)
- ✅ **Attack Lab** (`zaremba lab`): 26 harmless attack simulations mapped to the OWASP Top 10 for Agentic Applications – 26 of 26 detected
- ✅ Fewer false alarms: example keys in docs are ignored; text written to files is not treated as a command

## ✅ v1.3 – One threat list for every device · October 2026
- ✅ The signed threat list now also covers **IDE extensions, browser extensions and Android apps**
- ✅ Desktop app, command line, browser extension and Android app all download it and check its signature – new threats arrive without an app update
- ✅ Daily research team adds newly reported threats; new attack techniques become rules through a weekly, reviewed build

## 🧪 Browser extension · *developer preview available*
- ✅ **Prompt-Injection Shield** for Chrome, Edge, Brave, Opera and Firefox: finds hidden instructions on web pages aimed at AI browsers and assistants, one-click neutralize and restore
- ✅ **Secret paste guard**: warns before you paste API keys, private keys or passwords into ChatGPT, Claude, Gemini and 13 other AI chats
- ✅ **Malicious AI extension check**: 34 fake AI extensions caught stealing chats and e-mails, each with its public source
- ✅ Download on GitHub for developer mode – [install guide](docs/BROWSER_EXTENSION.md)
- 🔨 Chrome Web Store, Microsoft Edge Add-ons and Firefox Add-ons (automatic updates)
- ✅ Signed live updates of the malicious-extension list (1.3.0)

## ✅ Android app 1.0 · October 2026 · *APK on GitHub*
- ✅ Fake AI app check: apps posing as ChatGPT, Claude, Gemini, DeepSeek, Grok, Copilot, Perplexity, Meta AI, Mistral, Poe, Character.AI, Kimi or Qwen
- ✅ Known malicious apps from public reports (e.g. the fake DeepSeek banking trojan)
- ✅ Apps from outside a store with screen control (Accessibility), device admin, notification or SMS access
- ✅ AI apps overview with access rights · check any text for hidden AI instructions (Share → ZaRemba)
- ✅ Background checks with alerts, update check
- ✅ Signed live threat updates (1.1.0)
- 🗓️ Google Play release · AI network watch (local VPN, opt-in)

## 🗓️ Trust & depth
- 🗓️ Installers signed with Microsoft and Apple developer certificates (no first-launch warnings)
- 🗓️ Tripwire read-detection on Windows and macOS (driver / Endpoint Security)
- 🗓️ Network Watch from system events instead of polling – catches even very short connections
- 🗓️ Confirm Gemini CLI, Cursor, Windsurf and Copilot CLI integrations on real installs; add more agents as they ship hooks
- 🗓️ German interface

## 🗓️ v1.x – Every device
- 🗓️ **iPhone & iPad**: Safari protection, link and media checks (Apple does not allow scanning other apps)
- 💡 **Deepfake & voice-clone warning** for calls, videos and voice messages

## 💡 Later
- 💡 ZaRemba for Teams & Servers – protection for companies and AI infrastructure
- 💡 Independent lab testing (AV-TEST / AV-Comparatives)
- 💡 Public threat feed of malicious AI extensions

---

### Have an idea or need something first?
[Share an idea in Discussions](https://github.com/kayzaa/ZaRemba-AI-Watcher-Official/discussions/categories/ideas) or [suggest a feature](https://github.com/kayzaa/ZaRemba-AI-Watcher-Official/issues/new?template=feature_request.yml) –
the most requested features move up the list.
