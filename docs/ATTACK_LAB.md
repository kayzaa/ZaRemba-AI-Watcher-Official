# 🧪 Attack Lab – measured, not claimed

No security product can promise 100 % protection, and ZaRemba does not. What we can do is **measure**: the Attack Lab
rebuilds every class of AI attack we know of as a **harmless simulation** – fake configurations, decoy files and text,
nothing executable, no real malware – and runs it through the same engines the app uses.

Run it yourself on any computer:

```bash
zaremba lab
```

Everything happens in a temporary folder that is deleted afterwards. Nothing on your system is changed.

## Result for ZaRemba 1.2: 26 of 26 attack classes detected

The classes follow the [OWASP Top 10 for Agentic Applications (2026)](https://genai.owasp.org/).

| Case | OWASP risk | Simulated attack | Caught by | Detected |
|---|---|---|---|---|
| LAB-01 | ASI01 Agent goal hijack | Hidden instructions in a web page or tool result | Injection Shield | ✅ |
| LAB-02 | ASI01 Agent goal hijack | Invisible Unicode tag message (ASCII smuggling) | Injection Shield | ✅ |
| LAB-03 | ASI01 Agent goal hijack | Past session that read injected content (forensics) | Agent forensics | ✅ |
| LAB-04 | ASI02 Tool misuse | Agent reads SSH private key | Agent Guard | ✅ |
| LAB-05 | ASI02 Tool misuse | Agent reads browser passwords / cookies | Agent Guard | ✅ |
| LAB-06 | ASI02 Tool misuse | Agent reads a crypto wallet | Agent Guard | ✅ |
| LAB-07 | ASI02 Tool misuse | Data upload to a webhook / paste service | Agent Guard | ✅ |
| LAB-08 | ASI02 Tool misuse | Wiping the home folder | Agent Guard | ✅ |
| LAB-09 | ASI03 Identity & privilege abuse | AI key in a shell profile | Scanner | ✅ |
| LAB-10 | ASI03 Identity & privilege abuse | AI keys in an agent's chat history | Agent forensics | ✅ |
| LAB-11 | ASI03 Identity & privilege abuse | Agent configured with all permission prompts off | Scanner | ✅ |
| LAB-12 | ASI03 Identity & privilege abuse | Agent tries to switch ZaRemba off | Agent Guard | ✅ |
| LAB-13 | ASI04 Agentic supply chain | Known malicious MCP server (postmark-mcp) | Scanner + threat intel | ✅ |
| LAB-14 | ASI04 Agentic supply chain | MCP server that silently auto-updates | Scanner | ✅ |
| LAB-15 | ASI04 Agentic supply chain | Poisoned MCP tool description | MCP Firewall | ✅ |
| LAB-16 | ASI04 Agentic supply chain | Skill that downloads and runs code (ClawHavoc pattern) | Scanner | ✅ |
| LAB-17 | ASI04 Agentic supply chain | Poisoned npm package (s1ngularity / Nx) | Scanner + threat intel | ✅ |
| LAB-18 | ASI04 Agentic supply chain | IDE extension with invisible code (GlassWorm) | IDE extension scan | ✅ |
| LAB-19 | ASI04 Agentic supply chain | Malicious AI model file (pickle code execution) | Model scan | ✅ |
| LAB-20 | ASI05 Unexpected code execution | Download-and-run (curl | bash) | Agent Guard | ✅ |
| LAB-21 | ASI05 Unexpected code execution | AI agent started without safety prompts (s1ngularity) | Agent Guard | ✅ |
| LAB-22 | ASI05 Unexpected code execution | AI-steered malware on disk (LameHug pattern) | AI malware scan | ✅ |
| LAB-23 | ASI06 Memory & context poisoning | Hidden instructions in an agent rules file (CLAUDE.md) | Rules-file scan | ✅ |
| LAB-24 | ASI06 Memory & context poisoning | Persistence: agent edits autostart files | Agent Guard | ✅ |
| LAB-25 | ASI10 Rogue agents / AI-powered malware | Program touches a decoy wallet / key file | AI Tripwire | ✅ |
| LAB-26 | ASI10 Rogue agents / AI-powered malware | Unknown program from a temp folder talks to an AI API | Network Watch | ✅ |

## What this number means – and what it does not
- It shows that **every attack class we know of has at least one working detection layer**, tested automatically with
  every build. When we learn about a new class of attack, it is added here first – as a gap until a detector ships.
- It is **our own lab**, not an independent test. Real attacks vary; a brand-new variant can look different from our
  simulation. Independent lab testing (AV-TEST / AV-Comparatives) is on the [roadmap](../ROADMAP.md).
- OWASP risks ASI07 (inter-agent communication), ASI08 (cascading failures) and ASI09 (human trust) are about how
  agent systems are built and used; they are not attacks a device scanner can simulate.
- Some layers only work where you turned them on: the Agent Guard, Injection Shield and MCP Firewall protect the agents
  you connected (*Protect everything* in the app).

Keep your normal antivirus – ZaRemba adds the AI-specific layer it does not have.
