"""
This script evaluates whether the assistant completes the user's task across a multi-turn dialogue.
"""

import json
from typing import Dict, Any, Optional
from llm_client import LLMClient


TASK_COMPLETION_RUBRIC = """
You are a Task Completion Evaluation Agent.

Evaluate whether the assistant successfully helps the user complete their task across the dialogue.

Task completion refers to whether the assistant understands the user's goal, follows instructions, addresses constraints, and moves the task forward over multiple turns.

Evaluation criteria:

1. Goal Understanding
Does the assistant correctly understand what the user is trying to accomplish?
2. Instruction Following
Does the assistant follow the user's explicit instructions and constraints?
3. Progress Across Turns
Does the assistant build on previous turns and move the task closer to completion?
4. Completeness
Does the response address the user's current request sufficiently?
5. Adaptation to Feedback
Does the assistant incorporate corrections, refinements, or new requirements from the user?

Score from 1 to 5:

1 = Fails to understand or address the task.
2 = Partially addresses the task but misses major requirements.
3 = Generally useful but incomplete or missing some important constraints.
4 = Mostly completes the task with only minor gaps.
5 = Fully completes the task and effectively incorporates the dialogue context.

Allowed issue tags:
- misunderstood_goal
- ignored_instruction
- missed_constraint
- incomplete_answer
- no_progress
- poor_feedback_adaptation
- overly_generic
- unnecessary_clarification

Return only valid JSON:

{
  "agent": "task_completion",
  "score": 4,
  "rationale": "Brief explanation here.",
  "issues": ["missed_constraint"]
}
"""


class TaskCompletionAgent:
    def __init__(self, llm_client: Optional[LLMClient] = None):
        self.llm_client = llm_client or LLMClient()

    def evaluate(
        self,
        user_query: str,
        model_response: str,
        conversation_context: str = ""
    ) -> Dict[str, Any]:

        prompt = f"""
{TASK_COMPLETION_RUBRIC}

Conversation history:
{conversation_context if conversation_context else "No previous context provided."}

Latest user message:
{user_query}

Assistant response:
{model_response}

Evaluate the assistant's task completion.
"""

        raw_output = self.llm_client.judge(prompt)

        try:
            return json.loads(raw_output)
        except json.JSONDecodeError:
            return {
                "agent": "task_completion",
                "score": None,
                "rationale": "Failed to parse JSON output.",
                "issues": ["parse_error"],
                "raw_output": raw_output
            }