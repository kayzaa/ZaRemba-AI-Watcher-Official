# Privacy policy

_Applies to ZaRemba AI Watcher 0.x (scanner, AI Tripwire, AI Network Watch, Agent Guard and MCP Firewall). Last updated: October 2026._

**Short version: ZaRemba does not collect, send or store any of your data.**

| Question | Answer |
|---|---|
| Does ZaRemba connect to the internet? | `zaremba scan` and `zaremba tripwire` work fully offline. `zaremba net` only performs DNS lookups of public AI service host names (like `api.openai.com`) to learn their addresses. Nothing about you or your device is sent. |
| Does it send telemetry, crash reports or statistics? | **No.** |
| Do I need an account? | **No.** |
| What does it read? | Configuration files of AI tools, agent skill folders, shell profiles, `.env` files, installed package manifests, and the project folders you pass with `--project`. |
| What is stored? | Only in the `.zaremba` folder in your home directory: tripwire manifest and alarms, trusted programs, Network Watch history, Agent Guard and MCP Firewall logs (blocked actions, shortened to 200 characters) and pinned MCP tool fingerprints. Delete the folder to remove everything. |
| Does the Agent Guard / MCP Firewall send my prompts or files anywhere? | **No.** Every decision is made on your computer. |
| Does it change my files? | **No.** The scan is read-only. AI Tripwire only creates its own decoy files (and `~/.zaremba/` for its manifest and alarm log) and never overwrites existing files. |
| What happens with API keys it finds? | They are never stored, sent or fully displayed. The report shows only a short hint such as `sk-pro…(33 chars)`. |
| Does Network Watch read my traffic? | **No.** It only sees which program is connected to which address – the same information as the system's own network tools. Content is never read. |
| Where does the report go? | Only to your screen, or to a file if you redirect the output yourself. |

Future versions with online features (for example automatic threat-database updates) will be **opt-in**, will be
described here before release, and will never upload your files or secrets.

Questions: open an issue labelled **privacy** or see [SUPPORT.md](SUPPORT.md).
