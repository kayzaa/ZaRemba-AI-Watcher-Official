# 🌐 AI Network Watch

AI-powered malware has to talk to an AI model somewhere. LameHug asked a model on Hugging Face which commands to run;
PROMPTFLUX asked Gemini to rewrite its own code every hour. AI Network Watch shows **which program on your computer is
talking to which AI service** – so a program that has no business doing that stands out.

## Quick start
```bash
zaremba net            # who is talking to AI services right now?
zaremba net watch      # keep watching, report every new program (Ctrl+C to stop)
```

Example:
```text
🚨 HIGH RISK    invoice_helper (PID 3268) → Hugging Face
               C:\Users\you\Downloads\invoice_helper.exe
               A system tool or a program from a temp/download folder talking to AI is a known malware pattern.
⚠️  UNKNOWN    pdftool (PID 4120) → OpenAI API
               Unknown program. If you don't recognise it, investigate. Trust it with: zaremba net allow "pdftool"
🟨 SCRIPT       node (PID 2211) → Anthropic API
               Script host. Normal for AI coding tools (e.g. Claude Code, Codex run on Node.js) – but also how AI malware runs.
✅ expected     chrome (PID 912) → ChatGPT
```

## Verdicts
| Verdict | Meaning | What to do |
|---|---|---|
| 🚨 **High risk** | A Windows system tool (wscript, cscript, mshta, rundll32, regsvr32, certutil …) or a program running from a temp or Downloads folder | Investigate now. Disconnect from the internet if you don't know the program. |
| ⚠️ **Unknown** | A program ZaRemba does not know | If you recognise it, trust it: `zaremba net allow "name"`. If not, investigate. |
| 🟨 **Script** | Python, Node.js, PowerShell, shell, curl … | Normal if you use AI coding tools or your own scripts. Trust it once you're sure. |
| ✅ **Expected** | Browsers and known AI apps (Claude, ChatGPT, Cursor, VS Code, Windsurf, Ollama, LM Studio …) | Nothing. |
| ✅ **Trusted** | On your trusted list | Nothing. |

## Which AI services are recognised
OpenAI API · ChatGPT · Anthropic API · Claude · Google Gemini API · Google Vertex AI · Hugging Face (incl. Inference) ·
OpenRouter · Mistral AI · DeepSeek · Groq · Together AI · Perplexity · xAI · Cohere · Alibaba Qwen ·
local **Ollama** (port 11434) and **LM Studio** (port 1234).

Missing one? [Suggest it](https://github.com/kayzaa/ZaRemba-AI-Watcher-Official/issues/new?template=feature_request.yml).

## Trusted programs
```bash
zaremba net allow "node"                 # by name
zaremba net allow "/opt/mytool/bin/agent"  # or by full path (stricter)
zaremba net allowed                      # show the list
zaremba net disallow "node"              # remove again
```

## History
`zaremba net watch` records every report. Show it with `zaremba net history`.

## Privacy
- Only connection **metadata** is used: remote address, port and the owning program – the same information the system's
  own tools (`netstat`, Resource Monitor, Activity Monitor) show. Traffic content is never read.
- To recognise AI services, ZaRemba looks up their public addresses (DNS). Nothing about you is sent.

## Good to know
- Some AI services share addresses with other websites (e.g. Google). Such matches are marked
  *"shared address – possible match"*.
- `zaremba net watch` checks every 2 seconds; a connection that opens and closes in between can be missed. The v1.0
  desktop app will use system network events instead.
- Admin rights are not required, but without them some systems hide the owning program of other users' connections.
