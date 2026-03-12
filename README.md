# ◈ The Data Leader
### Executive Data Governance Guide — Sports & Entertainment Edition

A personal Streamlit app for mastering data governance concepts as an executive
in the sports and entertainment industry. Runs fully offline and locally.

---

## Setup (One-Time)

**Prerequisites:** Python 3.9+ installed on your machine.

### 1. Install dependencies

```bash
cd dg_exec_app
pip install -r requirements.txt
```

### 2. Run the app

```bash
streamlit run app.py
```

This opens the app at `http://localhost:8501` in your browser.

---

## Access from Your iPhone

As long as your phone and computer are on the **same Wi-Fi network**:

1. Run `streamlit run app.py` on your Mac
2. In your terminal, note the **Network URL** (e.g. `http://192.168.1.42:8501`)
3. Open that URL in Safari on your iPhone
4. Tap the **Share** button → **Add to Home Screen**
5. It will behave like a native app icon on your home screen

> The app does not require an internet connection after the initial font load.

---

## What's Inside

| Section | Content |
|---|---|
| 🏠 Home | Overview and module index |
| 📚 Learning Path | 5 structured modules — Foundation → Structure → Problems → Culture → Future |
| ⚡ Quick Reference | 4 executive reference cards for meetings |

### The 5 Modules
1. **What Is Data Governance?** — Plain-language definition, why it matters in the AI era, the three governance layers
2. **The Governance Org Structure** — CDO role, DMO, Data Council, full stakeholder map
3. **The Five Core Problems** — Biometric data, fan monetization, regulatory patchwork, ownership disputes, AI risk
4. **Building a Data Governance Culture** — The four culture levers, real-world playbook, what's actually worked
5. **Where the Industry Is Headed** — Five open frontiers and how to position ahead of them

### The 4 Reference Cards
- **Governance Vocabulary Cheat Sheet** — 15 terms to use confidently
- **Regulatory Quick Reference** — GDPR, CCPA, BIPA, COPPA, HIPAA + more
- **Governance Maturity Signals** — How to read where an org stands
- **The Governance Conversation: What to Ask** — 8 questions for any executive meeting

---

## Auto-Start on Mac (Optional)

To have the app launch automatically when you open your Mac:

1. Open **Automator** → New Document → **Application**
2. Add a **Run Shell Script** action
3. Paste: `cd /path/to/dg_exec_app && streamlit run app.py`
4. Save as an app and add it to your Login Items

---

*Source material: Data Governance & Privacy in Sports and Entertainment, Research Brief, March 2026.*
*Built for personal executive development use only.*
