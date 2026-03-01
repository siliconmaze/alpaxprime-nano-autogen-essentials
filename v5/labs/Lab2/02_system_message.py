"""Lab 2 - Agent with System Message"""
import sys
sys.path.insert(0, '../../..')
from config import get_ollama_config
from autogen import AssistantAgent

agent = AssistantAgent(
    name="python_expert",
    system_message="You are a Python expert. Provide brief, clear answers with code examples.",
    llm_config={"config_list": get_ollama_config()}
)

response = agent.generate_reply(
    messages=[{"role": "user", "content": "How do I sort a list?"}]
)
print(response)
