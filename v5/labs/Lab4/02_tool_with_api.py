"""Lab 4 - API Tool"""
import sys
sys.path.insert(0, '../../..')
import requests
from config import get_ollama_config
from autogen import AssistantAgent, UserProxyAgent

def get_github_stars(repo: str) -> str:
    """Get GitHub stars"""
    r = requests.get(f"https://api.github.com/repos/{repo}")
    return f"Stars: {r.json().get('stargazers_count', 0)}"

assistant = AssistantAgent("github_agent", llm_config={
    "config_list": get_ollama_config(),
    "tools": [get_github_stars]
})

user = UserProxyAgent("user", human_input_mode="NEVER")
user.initiate_chat(assistant, message="Stars for microsoft/autogen?")
