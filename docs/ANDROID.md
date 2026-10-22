# 📱 ZaRemba AI Watcher for Android

_Version 1.0 · Android 8.0 or newer · free · developer preview outside Google Play_

Fake AI apps are one of the easiest ways criminals get onto phones: an app called "DeepSeek" or "ChatGPT" from a link,
which then asks for access to your screen and installs a banking trojan. Security researchers documented exactly this
with a fake DeepSeek app that delivered the OctoV2 banking trojan
([K7 Security Labs, March 2025](https://labs.k7computing.com/index.php/android-banking-trojan-octov2-masquerading-as-deepseek-ai/)).

ZaRemba for Android checks your phone for this – on the phone, without uploading anything.

## What it checks

| Check | What it finds |
|---|---|
| 🎭 **Fake AI apps** | Apps that present themselves as ChatGPT, Claude, Google Gemini, DeepSeek, Grok, Microsoft Copilot, Perplexity, Meta AI, Le Chat / Vibe (Mistral), Poe, Character.AI, Kimi or Qwen but are **not** the official app of that company. The official package names were checked on Google Play. |
| ☠️ **Known malicious apps** | Apps named in public malware reports, with the source. |
| 👁️ **Screen control** | Apps from outside an app store that have **Accessibility** access – they can read everything on screen and tap for you. This is how banking trojans take over phones. |
| 🔐 **Other dangerous access** | Device administrators, apps that read all notifications or your SMS (one-time banking codes), apps allowed to install other apps. |
| 🤖 **AI apps overview** | Every AI app on the phone: official or not, installed from a store or not, and what it can access (screen, microphone, camera, location, contacts, SMS, photos). |
| 💬 **Check a text** | Paste or share (Share → *Check with ZaRemba*) a message, e-mail or web text: finds hidden instructions aimed at AI assistants, invisible characters, secrets such as API keys, and links to app files (`.apk`). |
| 🔔 **Background checks** | Re-checks every few hours and notifies you about new fake AI apps or new dangerous access. |

Every finding comes with the fix: **Uninstall**, open the app's settings, or switch off the access – Android asks you
to confirm, ZaRemba never removes anything on its own.

## 📥 Install

1. On your phone, download **[ZaRemba-AI-Watcher-android.apk](https://github.com/kayzaa/ZaRemba-AI-Watcher-Official/releases/latest/download/ZaRemba-AI-Watcher-android.apk)**.
2. Open the downloaded file. Android asks whether your browser may install apps – allow it **for this install**
   (*Settings → Install unknown apps*), then tap **Install**.
3. Open ZaRemba. Allow notifications if you want alerts.
4. Recommended: switch *Install unknown apps* off again for your browser afterwards – ZaRemba will remind you.

Google Play Protect may show a warning because the app is not from Google Play. You can check that your download is
genuine: the SHA-256 checksum is listed on the release page, and every ZaRemba APK is signed with the same release key
(certificate SHA-256 `FE:D4:BF:3D:77:BB:5E:D5:81:0C:E8:8C:99:20:0C:20:35:3F:D2:F7:BC:7C:48:F5:40:66:94:2A:5D:E6:E1:8B`).
Android only installs updates signed with that same key.

### Updates
ZaRemba checks the official release page for a newer version (you can switch this off in Settings) and shows a
**Download** button. Updates install over the old version and keep your settings.

## 🔒 Privacy and permissions

| Permission | Why |
|---|---|
| See all installed apps | To find fake and dangerous apps. The list never leaves the phone. |
| Request to uninstall apps | Only opens Android's own *Uninstall?* dialog when **you** tap Uninstall. |
| Notifications | Alerts about new threats (optional). |
| Internet | Only to check the official GitHub release page for updates. Nothing about you is sent. |

No account, no tracking, no analytics. Texts you check are checked on the phone and not stored.

## ⚠️ Honest limits
- Android does not let normal apps look inside other apps, watch their network traffic or scan their files. ZaRemba
  checks what Android allows: which apps are installed, where they came from and what access they have.
- A brand-new fake with a harmless-looking name and no special access may not be recognised.
- No security app can catch everything. Install apps only from your app store and keep Android up to date.

## Why not on Google Play (yet)?
Google Play requires a developer account and a review, which is in preparation. Until then the app is published here,
signed with ZaRemba's release key.
