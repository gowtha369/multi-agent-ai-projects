# Multi-Agent 5G Network Operations Assistant

This portfolio project simulates an AI-assisted network-operations workflow. It does **not** modify a network; all actions require human approval.

## Agents

1. Monitoring Agent detects abnormal latency, packet loss, CPU use and handover failure rate.
2. Diagnosis Agent identifies a likely cause.
3. Optimisation Agent proposes a safe next step.
4. Safety Agent labels every output as recommendation-only.

## Run

```bash
python app.py
```

## Next improvements

- Read live/simulated KPI data from CSV.
- Train an anomaly-detection model with Isolation Forest.
- Add a Streamlit dashboard.
- Replace the Diagnosis Agent with an LLM, while retaining safety review.
