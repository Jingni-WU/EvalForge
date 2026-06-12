"""
This script defines the coherence evaluation agent for assessing context consistency in multi-turn dialogue responses.
Coherence evaluates whether a response is consistent with prior dialogue context, maintains topic continuity, 
correctly tracks entities and user intent across turns, and avoids contradictions.
"""

# This script evaluates dialogue coherence in multi-turn conversations.

import json
from typing import Dict, Any, Optional
from llm_client import LLMClient


COHERENCE_RUBRIC = """
You are a Coherence Evaluation Agent.

Evaluate the coherence of the assistant throughout the dialogue.

Coherence refers to whether the assistant maintains logical and contextual consistency across multiple turns.

Evaluation criteria:

1. Context Retention
Does the assistant correctly remember and use relevant information from previous turns?

2. Consistency
Does the assistant avoid contradicting itself or user-provided information?

3. Intent Tracking
Does the assistant stay aligned with the user's evolving goals?

4. Topic Continuity
Does the assistant maintain a coherent conversational flow?

5. Reference Resolution
Does the assistant correctly interpret references to earlier entities, events, preferences, or decisions?

Score from 1 to 5:

1 = Severe coherence failures or contradictions.

2 = Multiple context or consistency issues.

3 = Mostly coherent but misses important context.

4 = Coherent and context-aware with minor issues.

5 = Excellent dialogue coherence and context retention.

Allowed issue tags:
- lost_context
- contradiction
- intent_drift
- topic_shift
- incorrect_reference
- inconsistent_information

Return only valid JSON:

{
  "agent": "coherence",
  "score": 4,
  "rationale": "Brief explanation here.",
  "issues": ["lost_context"]
}
"""


class CoherenceAgent:
    def __init__(self, llm_client: Optional[LLMClient] = None):
        self.llm_client = llm_client or LLMClient()

    def evaluate(
        self,
        user_query: str,
        model_response: str,
        conversation_context: str = ""
    ) -> Dict[str, Any]:

        prompt = f"""
{COHERENCE_RUBRIC}

Conversation history:
{conversation_context}

Latest user message:
{user_query}

Assistant response:
{model_response}

Evaluate the coherence of the assistant response.
"""

        raw_output = self.llm_client.judge(prompt)

        try:
            return json.loads(raw_output)
        except json.JSONDecodeError:
            return {
                "agent": "coherence",
                "score": None,
                "rationale": "Failed to parse JSON output.",
                "issues": ["parse_error"],
                "raw_output": raw_output
            }