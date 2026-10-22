# Installation guide

ZaRemba AI Watcher 0.1 is a single program file. There is nothing to install and nothing runs in the background.

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
Preview builds are not yet code-signed. Code signing and notarization come with the v1.0 desktop app.

- **Windows SmartScreen** ("Windows protected your PC"): click **More info → Run anyway** – only after verifying the checksum.
- **macOS Gatekeeper** ("cannot be opened because the developer cannot be verified"): run
  `xattr -d com.apple.quarantine zaremba` once, or open **System Settings → Privacy & Security** and click **Open Anyway**.

## Uninstall
Delete the `zaremba` file. ZaRemba 0.1 stores nothing else on your computer.

## Need help?
See [SUPPORT.md](../SUPPORT.md).
