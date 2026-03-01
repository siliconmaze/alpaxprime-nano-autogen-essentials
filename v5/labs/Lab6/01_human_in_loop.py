"""Lab 6 - Human in the Loop"""
import sys
sys.path.insert(0, '../../..')
from config import get_ollama_config
from autogen import AssistantAgent, UserProxyAgent

assistant = AssistantAgent("assistant", llm_config={"config_list": get_ollama_config()})
user = UserProxyAgent("user", human_input_mode="TERMINATE")

print("Starting chat - will prompt for human input on TERMINATE")
user.initiate_chat(assistant, message="What is 2+2?")
