# Privacy policy

_Applies to ZaRemba AI Watcher 1.x (desktop app, command line and browser extension). Last updated: October 2026 (v1.1)._

**Short version: ZaRemba does not collect, send or store any of your data.** The only exception is the optional
*Bring your own AI* feature: when **you** connect an AI and click **Send to AI**, the text you were shown goes to the AI
provider **you** chose – never to ZaRemba.

| Question | Answer |
|---|---|
| Does ZaRemba connect to the internet? | Only to **download**: (1) signed app updates and the update information from this GitHub repository, (2) the signed threat-intelligence file from this GitHub repository, (3) DNS lookups of public AI service names for Network Watch. These are ordinary downloads – like opening a web page on GitHub, GitHub sees your IP address. Nothing about you, your files or your AI usage is sent. `zaremba scan` and `zaremba tripwire` work fully offline. |
| Does it send telemetry, crash reports or statistics? | **No.** |
| Do I need an account? | **No.** |
| What does it read? | Configuration files of AI tools, agent skill folders, shell profiles, `.env` files, installed package manifests, and the project folders you pass with `--project`. |
| What is stored? | Only in the `.zaremba` folder in your home directory: tripwire manifest and alarms, trusted programs, Network Watch history, Agent Guard and MCP Firewall logs (blocked actions, shortened to 200 characters) pinned MCP tool fingerprints, quarantined items and app settings (including which AI you connected – never the key). Delete the folder to remove everything. |
| Does the Agent Guard / MCP Firewall send my prompts or files anywhere? | **No.** Every decision is made on your computer. |
| Does it change my files? | The scan is read-only. AI Tripwire only creates its own decoy files (and `~/.zaremba/` for its manifest and alarm log) and never overwrites existing files. **Quarantine** moves an item only when you click *Quarantine* or switch on automatic quarantine (critical threat-database matches only); it keeps the item in `~/.zaremba/quarantine/` so you can restore it. Items are deleted only when you click *Delete* twice. |
| What does *Bring your own AI* send, and to whom? | Nothing unless you connect an AI **and** click **Send to AI**. Then the text shown in the window – the finding, and for a second opinion the skill's instruction files or the MCP server's settings entry – goes directly to the provider you chose (Anthropic, OpenAI, Google, your local Ollama, or Anthropic through your installed Claude Code). Known API keys and values labelled password, token, secret or key are replaced with `[REDACTED]` first. That provider's own privacy policy applies. ZaRemba never receives it. |
| Where is my AI API key stored? | In your system's keychain (Windows Credential Manager, macOS Keychain, Linux Secret Service). It is sent only to the provider it belongs to. **Disconnect** deletes it. |
| What happens with API keys it finds? | They are never stored, sent or fully displayed. The report shows only a short hint such as `sk-pro…(33 chars)`. |
| Does Network Watch read my traffic? | **No.** It only sees which program is connected to which address – the same information as the system's own network tools. Content is never read. |
| Where does the report go? | Only to your screen, or to a file if you redirect the output yourself. |

## Browser extension

| Question | Answer |
|---|---|
| Does the extension send anything? | **No.** It makes no network requests at all – no account, no analytics, no tracking. |
| Why can it read all websites? | The Prompt-Injection Shield must read each page you open to find hidden instructions aimed at AI assistants, and change the page when you click **Neutralize**. Page content is checked in your browser and never stored or sent. |
| What happens with text I paste into AI chats? | On the supported AI chat sites it is checked for secrets inside your browser, at the moment you paste. It is not stored or sent anywhere by ZaRemba. |
| Why does it ask to "manage your extensions"? | Only when you click **Check my extensions**: it compares the IDs of your installed extensions with a built-in list of known malicious AI extensions and lets you remove a match. The list of your extensions never leaves the browser. |
| What is stored? | In the browser's extension storage on your device: your on/off settings and the result of the last extension check. Removing the extension deletes it. |

New online features will be described here before release and will never upload your files or secrets without your
explicit action.

Questions: open an issue labelled **privacy** or see [SUPPORT.md](SUPPORT.md).
