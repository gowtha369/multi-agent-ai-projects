"""Multi-Agent 5G Network Operations Assistant (simulated data, no API key)."""
from dataclasses import dataclass, asdict
from typing import Dict, List


@dataclass
class CellMetrics:
    cell_id: str
    latency_ms: float
    packet_loss_pct: float
    cpu_pct: float
    handover_fail_pct: float


class MonitoringAgent:
    """Detects cells whose metrics exceed simple service thresholds."""
    def detect(self, metrics: List[CellMetrics]) -> List[Dict]:
        alerts = []
        for item in metrics:
            reasons = []
            if item.latency_ms > 50: reasons.append("high latency")
            if item.packet_loss_pct > 2: reasons.append("packet loss")
            if item.cpu_pct > 85: reasons.append("high CPU")
            if item.handover_fail_pct > 3: reasons.append("handover failures")
            if reasons:
                alerts.append({"cell_id": item.cell_id, "reasons": reasons, "metrics": asdict(item)})
        return alerts


class DiagnosisAgent:
    """Explains likely causes from the abnormal metrics."""
    def diagnose(self, alerts: List[Dict]) -> List[Dict]:
        diagnoses = []
        for alert in alerts:
            m = alert["metrics"]
            if m["cpu_pct"] > 85 and m["latency_ms"] > 50:
                cause = "Cell congestion or overloaded edge compute"
            elif m["handover_fail_pct"] > 3:
                cause = "Mobility or neighbour-cell configuration issue"
            elif m["packet_loss_pct"] > 2:
                cause = "Radio interference or backhaul degradation"
            else:
                cause = "Needs deeper performance investigation"
            diagnoses.append({**alert, "likely_cause": cause})
        return diagnoses


class OptimisationAgent:
    """Proposes a recommendation; it never makes network changes."""
    def recommend(self, diagnoses: List[Dict]) -> List[Dict]:
        output = []
        for item in diagnoses:
            cause = item["likely_cause"]
            if "congestion" in cause:
                action = "Review traffic balancing and capacity allocation for this cell."
            elif "Mobility" in cause:
                action = "Review neighbour relations and handover parameters in a test environment."
            elif "interference" in cause:
                action = "Run spectrum/interference analysis and inspect backhaul health."
            else:
                action = "Collect additional KPIs and create an engineering investigation ticket."
            output.append({**item, "recommendation": action})
        return output


class SafetyAgent:
    """Requires human approval before a recommendation can be acted on."""
    def review(self, recommendations: List[Dict]) -> List[Dict]:
        for item in recommendations:
            item["safety_status"] = "Human engineer approval required — recommendation only"
        return recommendations


def sample_metrics() -> List[CellMetrics]:
    return [
        CellMetrics("SE-STO-001", 27, 0.3, 62, 0.8),
        CellMetrics("SE-STO-002", 78, 3.1, 93, 1.2),
        CellMetrics("SE-GOT-011", 32, 0.5, 71, 5.7),
        CellMetrics("SE-MAL-004", 45, 4.5, 65, 1.4),
    ]


def run_workflow(metrics: List[CellMetrics]) -> List[Dict]:
    alerts = MonitoringAgent().detect(metrics)
    diagnoses = DiagnosisAgent().diagnose(alerts)
    recommendations = OptimisationAgent().recommend(diagnoses)
    return SafetyAgent().review(recommendations)


if __name__ == "__main__":
    results = run_workflow(sample_metrics())
    print("5G Network Operations Assistant\n")
    for result in results:
        print(f"{result['cell_id']}: {result['likely_cause']}")
        print(f"  Recommendation: {result['recommendation']}")
        print(f"  Safety: {result['safety_status']}\n")
