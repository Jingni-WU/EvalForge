"""
This script runs all evaluation agents on a multi-turn dialogue example.
"""

import json
from src.coherence_agent import CoherenceAgent
from src.human_likeness_agent import HumanLikenessAgent
from src.safety_agent import SafetyAgent
from src.task_completion import TaskCompletionAgent
from src.metrics import build_evaluation_summary


def run_evaluation(conversation_context, user_query, model_response):
    agents = [
        CoherenceAgent(),
        TaskCompletionAgent(),
        SafetyAgent(),
        HumanLikenessAgent(),
    ]

    results = []

    for agent in agents:
        result = agent.evaluate(
            user_query=user_query,
            model_response=model_response,
            conversation_context=conversation_context,
        )
        results.append(result)

    summary = build_evaluation_summary(results)

    return {
        "summary": summary,
        "agent_results": results,
    }


if __name__ == "__main__":
    conversation_context = """
User: I want to write a short and polite email to my professor.
Assistant: Sure, I can help with that. What do you want to say?
User: I want to tell him I cannot attend class today because I feel sick.
"""

    user_query = "Make it brief and not too dramatic."

    model_response = """
Dear Professor,

I hope you are doing well. I wanted to let you know that I am not feeling well today and will not be able to attend class. I apologize for the inconvenience and will catch up on any missed material.

Best,
[Your Name]
"""

    evaluation = run_evaluation(
        conversation_context=conversation_context,
        user_query=user_query,
        model_response=model_response,
    )

    print(json.dumps(evaluation, indent=2, ensure_ascii=False))