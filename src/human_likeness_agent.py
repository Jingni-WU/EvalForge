"""
This script evaluates how natural, conversational, and human-like an LLM response is.
"""

import json
from typing import Dict, Any, Optional
from llm_client import LLMClient


HUMAN_LIKENESS_RUBRIC = """
You are a Human-likeness Evaluation Agent.
Evaluate whether the assistant behaves like a helpful and natural conversational partner throughout the dialogue.

Evaluation criteria:
1. Naturalness
Does the response sound natural rather than robotic or templated?
2. Tone Adaptation
Does the assistant adapt its tone appropriately to the user's situation, emotions, and communication style?
3. Context Awareness
Does the response appropriately incorporate relevant information from previous turns and maintain conversational continuity?
4. Engagement
Does the assistant actively contribute to the conversation rather than providing generic or detached responses?
5. Fluency
Is the response clear, coherent, and easy to read?

Score from 1 to 5:

1 = Highly robotic, repetitive, or disconnected from the conversation.
2 = Somewhat unnatural with noticeable conversational issues.
3 = Acceptable conversational quality but lacks human-like adaptability.
4 = Natural and conversational with good context awareness.
5 = Highly natural, engaging, context-aware, and human-like.

Return only valid JSON in this format:

{
  "agent": "human_likeness",
  "score": 4,
  "rationale": "The response is natural and conversational with good context awareness.",
  "issues": [
    "slightly_generic"
  ]
}
"""


class HumanLikenessAgent:
    def __init__(self, llm_client: Optional[LLMClient] = None):
        self.llm_client = llm_client or LLMClient()

    def evaluate(
        self,
        user_query: str,
        model_response: str,
        conversation_context: str = ""
    ) -> Dict[str, Any]:

        prompt = f"""
{HUMAN_LIKENESS_RUBRIC}

Conversation context:
{conversation_context if conversation_context else "No previous context provided."}

User query:
{user_query}

Model response:
{model_response}

Now evaluate the human-likeness of the model response.
"""

        raw_output = self.llm_client.judge(prompt)

        try:
            return json.loads(raw_output)
        except json.JSONDecodeError:
            return {
                "score": None,
                "rationale": "Failed to parse LLM output as JSON.",
                "issues": ["Invalid JSON output"],
                "raw_output": raw_output
            }