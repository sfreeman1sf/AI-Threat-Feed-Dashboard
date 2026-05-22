# stacey-calendar-assistant 📅🤖

**A privacy-first personal AI assistant connecting Google Calendar to a local Ollama model — with persistent memory. Zero cloud dependency.**

Built to demonstrate that AI assistants don't need to send your data to the cloud. All inference runs locally on your machine using Ollama, with a clean tkinter GUI and Google Calendar integration for real scheduling tasks.

---

## What It Does

- 🗓️ **Reads your Google Calendar** — fetches upcoming events via the Google Calendar API
- 🧠 **Local AI reasoning** — sends calendar context to a local Ollama model for natural language responses
- 💾 **Persistent memory** — remembers past interactions across sessions
- 🖥️ **Desktop GUI** — clean tkinter interface, no browser required
- 🔒 **100% private** — no data ever leaves your machine

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Ollama | Local LLM inference (zero cloud) |
| Google Calendar API | Real calendar data |
| tkinter | Desktop GUI |
| JSON | Persistent memory storage |

---

## Why Local AI Matters

Most AI assistants send your conversations — including your schedule, contacts, and habits — to remote servers. This assistant runs entirely on your local machine:

- Your calendar data stays on your device
- Your conversations are never transmitted externally
- Works offline after initial setup
- No API keys, no subscriptions, no data harvesting

This project directly inspired the **Ollama local AI mode** planned for [Bizecurity](https://github.com/sfreeman1sf/staceyfreeman) — giving small businesses AI-powered security advice with zero data leaving their network.

---

## Related Projects

- [Ollama-Projects](https://github.com/sfreeman1sf/Ollama-Projects) — More local LLM experiments
- [staceyfreeman](https://github.com/sfreeman1sf/staceyfreeman) — Bizecurity app (Claude AI powered, Ollama roadmap)
- [LLM-Jailbreak-Scanner](https://github.com/sfreeman1sf/LLM-Jailbreak-Scanner) — Prompt injection detection

---

## Author

**Stacey Freeman** — AI Quality Specialist & LLM Evaluator | Red-Teaming Expert
- M.S. Cybersecurity (GCU, 2024)
- M.S. AI & Machine Learning (CSU, expected 2027)
- Founder, [Bizecurity LLC](https://www.bizecurity.com)
