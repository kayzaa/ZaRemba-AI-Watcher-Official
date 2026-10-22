# 🧩 Browser extension – Prompt-Injection Shield

_Version 1.2.0 · Chrome, Edge, Brave, Opera, Firefox · developer preview – store versions are coming_

AI browsers and assistants read web pages for you. Attackers have started hiding instructions in those pages – text you
cannot see that tells the AI to open links, read your e-mail or send your data somewhere else. Security researchers
showed this working against real AI browsers in 2025
([Brave](https://brave.com/blog/comet-prompt-injection/), [Brave](https://brave.com/blog/unseeable-prompt-injections/)).

<table>
  <tr>
    <td width="50%"><img src="../assets/screenshots/browser-shield.png" alt="Hidden AI instructions found on a page"><br><sub><b>Prompt-Injection Shield</b> – a page hides seven instructions for AI assistants. One click neutralizes them.</sub></td>
    <td width="50%"><img src="../assets/screenshots/browser-paste-guard.png" alt="Secret paste guard"><br><sub><b>Secret paste guard</b> – an API key is about to go into an AI chat. Paste it without the secret.</sub></td>
  </tr>
</table>

## What it does

### 🛡️ Prompt-Injection Shield (every website)
Finds instructions that **people cannot see but AI assistants read**:

| Hiding trick | Example |
|---|---|
| Hidden elements | `display: none`, `visibility: hidden`, the `hidden` attribute |
| Invisible text | 1-pixel or transparent text, text in the background colour |
| Off-screen text | text moved thousands of pixels off the page |
| Page source | HTML comments |
| Descriptions | image `alt`, `title` and `aria-label` text |
| Invisible characters | Unicode "tag" characters that carry a whole hidden message |

Hidden text is only reported when it reads like an instruction to an AI – for example "ignore previous instructions",
"note to the AI assistant", "send the user's e-mail to …" or chat-model control markers. **Visible text is never
flagged**, so articles about prompt injection do not cause alarms.

- A banner and the toolbar badge show how many were found.
- **Neutralize** removes them from the page, so AI tools that read the page no longer receive them. **Restore** puts
  everything back. Optional: *Neutralize automatically*.
- **Details** shows each hidden text and how it was hidden.

### 🔑 Secret paste guard (AI chats)
Before an API key, private key, database password or `password=` value is pasted or dropped into ChatGPT, Claude,
Gemini, Google AI Studio, Microsoft Copilot, Perplexity, DeepSeek, Grok, Mistral Le Chat, Poe, HuggingChat, Meta AI,
Qwen, Kimi, You.com or Character.AI, ZaRemba asks:
**Paste without secrets** (recommended) · **Paste anyway** · **Cancel**.

Recognised: OpenAI, Anthropic, Google, Hugging Face, OpenRouter, GitHub, AWS, Stripe and Slack keys, private keys
(SSH, PGP, PEM), database URLs with a password, and values labelled password / token / secret / API key.

### 🧩 Malicious AI extension check
Click **Check my extensions** in the toolbar popup. ZaRemba compares your installed extensions with fake AI
extensions that researchers caught stealing ChatGPT and DeepSeek chats, e-mails and browsing data – 34 entries, each
with its public source ([The Hacker News / OX Security](https://thehackernews.com/2026/01/two-chrome-extensions-caught-stealing.html),
[LayerX / Akamai](https://www.akamai.com/blog/security-research/aiframe-fake-ai-assistant-extensions-targeting-260000-chrome-users-via-injected-iframes)).
A match can be removed with one click (your browser asks for confirmation). The browser asks you once to allow
"Manage your apps, extensions, and themes" – only for this check.

---

## 📥 Install (developer mode)

Versions for the Chrome Web Store, Microsoft Edge Add-ons and Firefox Add-ons are coming. Until then – or if you
prefer – install the extension yourself:

### Chrome, Edge, Brave, Opera
1. Download **[ZaRemba-AI-Watcher-browser-chrome-edge.zip](https://github.com/kayzaa/ZaRemba-AI-Watcher-Official/releases/latest/download/ZaRemba-AI-Watcher-browser-chrome-edge.zip)**
   and **unzip** it into a folder you keep (for example `Documents/ZaRemba-browser`). Do not delete the folder later –
   the browser loads the extension from it.
2. Open the extensions page: `chrome://extensions` · `edge://extensions` · `brave://extensions` · `opera://extensions`
3. Switch on **Developer mode** (top right; in Edge on the left).
4. Click **Load unpacked** and select the unzipped folder (the one that contains `manifest.json`).
5. Pin ZaRemba: click the puzzle icon in the toolbar → pin **ZaRemba AI Watcher**.

### Firefox
Firefox only installs extensions signed by Mozilla permanently. Until the Firefox Add-ons version is available you can
try it **until the next restart**:
1. Download **[ZaRemba-AI-Watcher-browser-firefox.zip](https://github.com/kayzaa/ZaRemba-AI-Watcher-Official/releases/latest/download/ZaRemba-AI-Watcher-browser-firefox.zip)**.
2. Open `about:debugging#/runtime/this-firefox` → **Load Temporary Add-on…** → select the downloaded ZIP file.
3. Click the ZaRemba icon and **Allow on all websites** (Firefox asks for website access separately).

Requires Firefox 142 or newer.

### Updating
Extensions loaded in developer mode **do not update themselves**. Watch this repository's releases
(**Watch → Custom → Releases**), download the new ZIP, unzip it over the old folder and click **↻ Reload** on the
extensions page. Store versions will update automatically.

### Verify the download
Compare the SHA-256 checksum with `SHA256SUMS.txt` on the release page.

---

## 🔒 Privacy
- Everything runs **inside your browser**. The extension makes **no network requests** – no account, no tracking, no
  analytics.
- Page content and pasted text are checked locally and never stored or sent.
- Stored locally: your three on/off settings and the result of the last extension check.
- Why it needs access to all websites: the shield must read each page you open to find hidden instructions, and change
  the page when you click **Neutralize**.

## ⚠️ Limits
- It checks what is in the page. Instructions inside **images** (for example faint text in a picture) are not detected.
- AI browsers that load pages on their own servers do not see what you neutralize in your browser – there the warning
  still tells you not to let the AI act on the page.
- The extension check covers Chrome Web Store extension IDs (Chrome, Edge, Brave, Opera); the list format also takes
  Firefox add-on IDs. New entries arrive through the signed threat list, which the extension downloads about every 6
  hours and only uses if its signature is valid (needs Chrome 137+ / Firefox 142+; older browsers keep the built-in list).
- No security product can catch everything. Treat a clean result as "nothing known found", not as a guarantee.
