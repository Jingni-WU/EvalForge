"""
call LLM APIs (with retries, rate limiting, etc.) so the system can run tasks at scale without breaking.
"""

import time
from openai import OpenAI

class LLMClient:
    def __init__(self, model="gpt-4.1-mini", max_retries=3, sleep_seconds=2):
        self.client = OpenAI(max_retries=0)  
        self.model = model
        self.max_retries = max_retries
        self.sleep_seconds = sleep_seconds

    def judge(self, prompt: str) -> str:
        for attempt in range(self.max_retries):
            try:
                response = self.client.responses.create(
                    model=self.model,
                    input=prompt,
                    timeout=60,
                )
                return response.output_text

            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                time.sleep(self.sleep_seconds * (2 ** attempt))

        raise RuntimeError("LLM request failed after retries")