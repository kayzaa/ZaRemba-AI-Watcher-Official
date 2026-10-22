# Installation guide

## Desktop app (recommended)

**Windows 10/11:** download `ZaRemba-AI-Watcher-windows-x64-setup.exe` and run it. No admin rights needed.
**macOS 11+:** download the `.dmg` for your Mac (Apple menu → About This Mac → "Chip: Apple M…" = Apple Silicon,
"Processor: Intel" = Intel), open it and drag **ZaRemba AI Watcher** into **Applications**.
**Linux:** download the `.AppImage` (make it executable: `chmod +x ZaRemba-AI-Watcher-linux-x64.AppImage`) or install the `.deb`.

Then open ZaRemba and click **Protect everything**. Restart your AI apps once so they load the protection.

ZaRemba lives in your tray (Windows: bottom right; macOS: menu bar). Closing the window keeps protection running – use
the tray icon to open or quit. Updates install themselves (only updates signed with ZaRemba's release key are accepted).

To uninstall: in ZaRemba, turn off the protections you enabled (or run *Protect everything* in reverse from the
settings), then uninstall like any app (Windows: Settings → Apps; macOS: drag to Trash). Your `.zaremba` folder in the
home directory holds logs and settings – delete it to remove everything.

---

## Command line

The command-line edition is a single program file. There is nothing to install and nothing runs in the background.

## 1. Download
Get the file for your system from the [latest release](https://github.com/kayzaa/ZaRemba-AI-Watcher-Official/releases/latest).

| System | File |
|---|---|
| Windows 10/11 (64-bit) | `zaremba-windows-x64.zip` |
| Mac with Apple chip (M-series) | `zaremba-macos-apple-silicon.tar.gz` |
| Mac with Intel chip | `zaremba-macos-intel.tar.gz` |
| Linux (64-bit) | `zaremba-linux-x64.tar.gz` |

Not sure which Mac you have? Apple menu → **About This Mac** → look for "Chip: Apple M…" or "Processor: Intel".

## 2. Verify the download (recommended)
Each release lists a SHA-256 checksum for every file.

**Windows (PowerShell)**
```powershell
Get-FileHash $HOME\Downloads\zaremba-windows-x64.zip -Algorithm SHA256
```
**macOS / Linux**
```bash
shasum -a 256 ~/Downloads/zaremba-*.tar.gz
```
The result must match the checksum on the release page exactly.

## 3. Run a scan

**Windows**
1. Right-click the ZIP → **Extract All…**
2. Open the extracted folder, click the address bar, type `powershell` and press Enter.
3. Run:
```powershell
.\zaremba.exe scan
```

**macOS**
```bash
cd ~/Downloads
tar -xzf zaremba-macos-*.tar.gz
xattr -d com.apple.quarantine zaremba   # only needed once, see below
./zaremba scan
```

**Linux**
```bash
cd ~/Downloads
tar -xzf zaremba-linux-x64.tar.gz
./zaremba scan
```

Optional: move the file to a folder in your `PATH` (e.g. `/usr/local/bin` or `C:\Tools`) to run `zaremba` from anywhere.

## First-launch warnings
The installers are not yet signed with a Microsoft or Apple developer certificate (planned for v1.1), so your system
asks once. Verify the SHA-256 checksum from the release page first.

- **Windows SmartScreen** ("Windows protected your PC"): click **More info → Run anyway** – only after verifying the checksum.
- **macOS Gatekeeper** ("cannot be opened because the developer cannot be verified" or "is damaged"): open
  **System Settings → Privacy & Security** and click **Open Anyway**, or run once in Terminal:
  `xattr -cr "/Applications/ZaRemba AI Watcher.app"` (command line: `xattr -d com.apple.quarantine zaremba`).

## Uninstall
Run `zaremba tripwire remove` if you installed the tripwire, then delete the `zaremba` file and the `.zaremba` folder in your home directory.

## Need help?
See [SUPPORT.md](../SUPPORT.md).
