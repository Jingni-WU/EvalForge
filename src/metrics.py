"""
This script contains utility functions for aggregating evaluation agent results.
"""

from collections import Counter
from typing import Dict, List, Any, Optional


def get_valid_scores(agent_results: List[Dict[str, Any]]) -> List[float]:
    return [
        result["score"]
        for result in agent_results
        if isinstance(result.get("score"), (int, float))
    ]


def calculate_overall_score(agent_results: List[Dict[str, Any]]) -> Optional[float]:
    scores = get_valid_scores(agent_results)

    if not scores:
        return None

    return round(sum(scores) / len(scores), 2)


def collect_issue_tags(agent_results: List[Dict[str, Any]]) -> Dict[str, int]:
    all_issues = []

    for result in agent_results:
        issues = result.get("issues", [])
        if isinstance(issues, list):
            all_issues.extend(issues)

    return dict(Counter(all_issues))


def summarize_agent_scores(agent_results: List[Dict[str, Any]]) -> Dict[str, Any]:
    summary = {}

    for result in agent_results:
        agent_name = result.get("agent", "unknown")
        summary[agent_name] = {
            "score": result.get("score"),
            "issues": result.get("issues", []),
        }

    return summary


def build_evaluation_summary(agent_results: List[Dict[str, Any]]) -> Dict[str, Any]:
    return {
        "overall_score": calculate_overall_score(agent_results),
        "agent_scores": summarize_agent_scores(agent_results),
        "issue_summary": collect_issue_tags(agent_results),
    }