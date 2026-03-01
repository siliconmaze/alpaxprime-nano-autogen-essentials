"""Lab 2 - Basic Single Agent"""
import sys
sys.path.insert(0, '../../..')
from config import get_ollama_config
from autogen import AssistantAgent

print("Creating agent with Ollama...")
agent = AssistantAgent(
    name="basic_agent",
    llm_config={"config_list": get_ollama_config()}
)

response = agent.generate_reply(
    messages=[{"role": "user", "content": "What is 2 + 2?"}]
)
print(f"Response: {response}")
