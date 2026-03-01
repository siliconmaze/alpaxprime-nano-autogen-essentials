"""Lab 7 - Monitoring and Health Checks"""
import sys
import requests
sys.path.insert(0, '../../..')
from config import get_ollama_config
from autogen import AssistantAgent

def check_ollama():
    try:
        r = requests.get("http://localhost:11434/api/tags", timeout=5)
        return r.status_code == 200
    except:
        return False

def check_agent(agent):
    try:
        return agent.generate_reply(messages=[{"role": "user", "content": "hi"}]) is not None
    except:
        return False

print(f"Ollama: {'HEALTHY' if check_ollama() else 'DOWN'}")
agent = AssistantAgent("test", llm_config={"config_list": get_ollama_config()})
print(f"Agent: {'HEALTHY' if check_agent(agent) else 'DOWN'}")
