# 🪤 AI Tripwire

Thieves – human, malware or a hijacked AI agent – all go for the same things: crypto wallets, password lists,
`.env` files and API keys. AI Tripwire lays out **fake** versions of exactly these files. You never use them, so if
anything touches them, it is almost certainly up to no good.

## Quick start
```bash
zaremba tripwire install     # lay out the decoys
zaremba tripwire watch       # keep this running for live alarms (Ctrl+C to stop)
```
Any time later:
```bash
zaremba tripwire status      # were decoys changed or deleted?
zaremba tripwire alerts      # every recorded alarm
zaremba scan                 # the normal scan also reports tripwire alarms
```

## Where the decoys go
| Decoy | Default location |
|---|---|
| Crypto wallet recovery phrase | `Documents/Crypto/wallet-recovery-phrase.txt` |
| Password list | `Documents/Passwords/passwords-backup.csv` |
| Production `.env` file | `Documents/Projects/payment-service/.env.production` |
| API keys | `Documents/API-keys.txt` |

Prefer one folder? `zaremba tripwire install --dir /path/to/folder`

**Safety:** decoys contain only random, fake data. ZaRemba never overwrites an existing file (it skips that decoy and
tells you), never places decoys in real credential folders such as `.ssh` or `.aws`, and only ever removes files it
created itself.

## What triggers an alarm
| | Windows | macOS | Linux |
|---|---|---|---|
| Decoy changed | ✅ | ✅ | ✅ |
| Decoy moved / renamed | ✅ | ✅ | ✅ |
| Decoy deleted | ✅ | ✅ | ✅ |
| Decoy only **opened / read** | 🗓️ desktop app | 🗓️ desktop app | ✅ |
| Shows which program did it | 🗓️ | 🗓️ | ✅ (best effort) |

Detecting pure reads on Windows and macOS needs a system driver / Apple's Endpoint Security framework. That comes with
the signed v1.0 desktop app.

## Avoiding false alarms
Some legitimate programs open many files: search indexing (Windows Search, Spotlight, tracker), backup tools, cloud sync
and antivirus scanners. If an alarm names one of these, it is most likely harmless. Tips:
- Exclude the decoy folders from cloud sync if you can, or use `--dir` with a folder outside synced locations.
- Don't open the decoys yourself – `zaremba tripwire status` checks them without opening them.

## When an alarm is real
1. Note the program name and PID from the alarm.
2. Disconnect from the internet if you suspect active theft.
3. Run a full scan with your antivirus and `zaremba scan --all`.
4. Change important passwords from a different, clean device and move crypto funds to a new wallet if a real wallet
   was on the same computer.

## Remove
```bash
zaremba tripwire remove          # removes untouched decoys, keeps changed ones as evidence
zaremba tripwire remove --force  # removes everything
zaremba tripwire alerts --clear  # clears the alarm history
```
