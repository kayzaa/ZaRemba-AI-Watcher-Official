# Privacy policy

_Applies to ZaRemba AI Watcher 0.x (command-line scanner and AI Tripwire). Last updated: October 2026._

**Short version: ZaRemba does not collect, send or store any of your data.**

| Question | Answer |
|---|---|
| Does ZaRemba connect to the internet? | **No.** Version 0.x works fully offline. The threat database is built into the program. |
| Does it send telemetry, crash reports or statistics? | **No.** |
| Do I need an account? | **No.** |
| What does it read? | Configuration files of AI tools, agent skill folders, shell profiles, `.env` files, installed package manifests, and the project folders you pass with `--project`. |
| Does it change my files? | **No.** The scan is read-only. AI Tripwire only creates its own decoy files (and `~/.zaremba/` for its manifest and alarm log) and never overwrites existing files. |
| What happens with API keys it finds? | They are never stored, sent or fully displayed. The report shows only a short hint such as `sk-pro…(33 chars)`. |
| Where does the report go? | Only to your screen, or to a file if you redirect the output yourself. |

Future versions with online features (for example automatic threat-database updates) will be **opt-in**, will be
described here before release, and will never upload your files or secrets.

Questions: open an issue labelled **privacy** or see [SUPPORT.md](SUPPORT.md).
