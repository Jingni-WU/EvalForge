"""
download 100 LMSYS data from mt bench 
"""

from datasets import load_dataset
import json

dataset = load_dataset("lmsys/mt_bench_human_judgments", split="human")

data = []

for i, item in enumerate(dataset.select(range(100))):
    data.append({
        "id": item["question_id"],
        "model_a": item["model_a"],
        "model_b": item["model_b"],
        "conversation_a": item["conversation_a"],
        "conversation_b": item["conversation_b"],
        "winner": item["winner"]
    })

with open("/Users/piggy/Desktop/AGENT_Project/data/LMSYS.json", "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)