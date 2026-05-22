# AI-Threat-Feed-Dashboard 🛡️

**Real-time visualization of AI-detected security anomalies from SIEM data.**

Built as a prototype for Bizecurity LLC dashboards, this tool ingests threat data exported from Splunk and renders it as an interactive bar chart using Python and matplotlib.

---

## What It Does

Reads a CSV export of AI-detected anomalies from a SIEM (Security Information and Event Management) system and visualizes threat patterns by category — giving security analysts an at-a-glance view of active threat types.

```python
threats = pd.read_csv("sample_threats.csv")
threats.plot(kind='bar')
plt.title("AI-Detected Anomalies (Splunk Export)")
plt.show()
```

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Pandas | CSV ingestion and data processing |
| Matplotlib | Threat visualization |
| Splunk (export) | SIEM data source |

---

## Real-World Context

This dashboard was built as an early prototype for Bizecurity — a cybersecurity app for small businesses. The concept: surface AI-detected threats in plain English visuals that non-technical business owners can actually understand.

It connects directly to the broader Bizecurity security stack:
- Threat detection → visualized here
- Network scanning → [Bizecurity App](https://github.com/sfreeman1sf/staceyfreeman)
- Incident reporting → [Bizecurity App](https://github.com/sfreeman1sf/staceyfreeman)

---

## Related Projects

- [LLM-Jailbreak-Scanner](https://github.com/sfreeman1sf/LLM-Jailbreak-Scanner) — Prompt injection detection
- [Zero-Trust-MFA-Simulator](https://github.com/sfreeman1sf/Zero-Trust-MFA-Simulator) — Access control enforcement
- [staceyfreeman](https://github.com/sfreeman1sf/staceyfreeman) — Full Bizecurity app (Claude AI powered)

---

## Author

**Stacey Freeman** — AI Quality Specialist & LLM Evaluator | Red-Teaming Expert
- M.S. Cybersecurity (GCU, 2024)
- M.S. AI & Machine Learning (CSU, expected 2027)
- Founder, [Bizecurity LLC](https://www.bizecurity.com)
