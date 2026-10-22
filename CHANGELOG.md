# Changelog

All notable changes to ZaRemba AI Watcher are listed here.
Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [0.2.0] – Developer Preview – 2026-10
### Added
- **AI Tripwire**: `zaremba tripwire install | status | watch | alerts | remove`.
  - Four fake decoys: wallet recovery phrase, password list, production `.env`, API keys. Existing files are never overwritten.
  - Live alarms on change, move and delete (all platforms); on Linux also on open, with the responsible program.
  - Status checks never open the decoys, so checking does not trip the alarm.
  - Changed decoys are kept as evidence on `remove` unless `--force` is used.
- New scan rules `ZRW-TRP-001` … `ZRW-TRP-004`.

## [0.1.0] – Developer Preview – 2026-10
### Added
- `zaremba scan`: read-only AI Inventory scanner for Windows, macOS and Linux.
- AI agent inventory: Claude Code, Claude Desktop, Cursor, Windsurf, GitHub Copilot, Cline, Roo Code, Continue,
  Gemini CLI, Gemini Code Assist, Codex CLI, Amazon Q Developer CLI, OpenClaw, Ollama, LM Studio.
- MCP server audit across Claude Desktop, Claude Code, Cursor, Windsurf, Gemini CLI, VS Code and project configs.
- Skill audit for OpenClaw and Claude Code skills.
- Risky-setting checks for Claude Code and Codex CLI.
- Plain-text AI key detection (redacted output).
- Known-malicious npm package detection (global and per project).
- Built-in threat database, text and JSON reports, exit codes.
