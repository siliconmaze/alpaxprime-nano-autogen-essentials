"""Lab 7 - Production Patterns: Error Handling"""
import sys
import time
sys.path.insert(0, '../../..')
from config import get_ollama_config
from autogen import AssistantAgent

def create_with_retry(max_retries=3):
    for i in range(max_retries):
        try:
            agent = AssistantAgent("agent", llm_config={"config_list": get_ollama_config()})
            print("Agent created successfully!")
            return agent
        except Exception as e:
            print(f"Attempt {i+1} failed: {e}")
            time.sleep(2)
    raise Exception("Failed after retries")

agent = create_with_retry()
