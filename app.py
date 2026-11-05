"""Simple multi-agent research assistant with transparent local sources."""
import sys
from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Source:
    title: str
    url: str
    text: str


SOURCES = [
    Source("3GPP: 5G system overview", "https://www.3gpp.org/technologies/5g-system-overview",
           "5G systems support diverse services and require efficient network management and automation."),
    Source("Ericsson: AI and automation", "https://www.ericsson.com/en/ai",
           "AI can help communication service providers automate operations and improve network performance."),
    Source("ITU: AI for networks", "https://www.itu.int/itu-t/recommendations/",
           "AI techniques can assist network analysis, optimisation and operational decision support."),
]


class ResearchAgent:
    """Ranks local source cards. Replace this with web search or a vector database later."""
    def retrieve(self, question: str) -> List[Source]:
        words = set(question.lower().replace("?", "").split())
        return sorted(SOURCES, key=lambda s: len(words & set(s.text.lower().split())), reverse=True)


class AnalystAgent:
    def analyse(self, sources: List[Source]) -> List[str]:
        return [source.text for source in sources[:3]]


class CriticAgent:
    def check(self, findings: List[str], sources: List[Source]) -> List[str]:
        # A simple traceability check: every finding must be backed by one source card.
        valid = []
        source_text = " ".join(s.text for s in sources).lower()
        for finding in findings:
            if any(word in source_text for word in finding.lower().split() if len(word) > 5):
                valid.append(finding)
        return valid


class WriterAgent:
    def write(self, question: str, findings: List[str], sources: List[Source]) -> str:
        lines = [f"# Research brief\n\n**Question:** {question}\n", "## Evidence-backed findings"]
        lines.extend(f"- {finding}" for finding in findings)
        lines.append("\n## Sources")
        lines.extend(f"- [{source.title}]({source.url})" for source in sources[:3])
        lines.append("\n*This is a prototype. Verify sources before using the report for decisions.*")
        return "\n".join(lines)


def run_workflow(question: str) -> str:
    sources = ResearchAgent().retrieve(question)
    findings = AnalystAgent().analyse(sources)
    checked_findings = CriticAgent().check(findings, sources)
    return WriterAgent().write(question, checked_findings, sources)


if __name__ == "__main__":
    question = " ".join(sys.argv[1:]) or "How can AI improve 5G network optimisation?"
    print(run_workflow(question))
