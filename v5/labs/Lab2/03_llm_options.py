"""Lab 2 - LLM Parameter Options"""
import sys
sys.path.insert(0, '../../..')
from config import get_ollama_config
from autogen import AssistantAgent

test_prompt = "Tell me a short story"

settings = [
    {"temperature": 0.2, "name": "precise"},
    {"temperature": 0.7, "name": "balanced"},
    {"temperature": 1.0, "name": "creative"}
]

for s in settings:
    agent = AssistantAgent(name=s["name"], llm_config={
        "config_list": get_ollama_config(),
        "temperature": s["temperature"],
        "max_tokens": 100
    })
    print(f"\n=== {s['name']} (temp={s['temperature']}) ===")
    print(agent.generate_reply(messages=[{"role": "user", "content": test_prompt}]))
