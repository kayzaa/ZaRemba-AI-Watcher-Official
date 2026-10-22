# 🧠 ZaRemba threat intelligence

`threats.json` is the live list of known malicious MCP servers, agent skills and packages that ZaRemba AI Watcher
checks for. It is maintained by the ZaRemba research team and updated as new attacks become public.

- Every entry links to a public source (vendor research, advisory, CERT).
- Every version of the file is **signed** (`threats.json.sig`). ZaRemba verifies the signature with the key built into
  the app and ignores anything that is not signed or fails the quality checks.
- ZaRemba downloads updates automatically (desktop app: every 4 hours; command line: `zaremba update`).

Found something we are missing? [Report a threat](https://github.com/kayzaa/ZaRemba-AI-Watcher-Official/issues/new?template=threat_report.yml).
