"""Lab 3 - Basic Two-Agent Conversation"""
import sys
sys.path.insert(0, '../../..')
from config import get_ollama_config
from autogen import AssistantAgent, UserProxyAgent

assistant = AssistantAgent("assistant", llm_config={"config_list": get_ollama_config()})
user_proxy = UserProxyAgent("user", human_input_mode="NEVER")

user_proxy.initiate_chat(assistant, message="What is Python in one line?")
