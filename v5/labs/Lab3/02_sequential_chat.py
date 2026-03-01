"""Lab 3 - Sequential Chat"""
import sys
sys.path.insert(0, '../../..')
from config import get_ollama_config
from autogen import AssistantAgent, UserProxyAgent

assistant = AssistantAgent("math_helper", llm_config={"config_list": get_ollama_config()})
user = UserProxyAgent("user", human_input_mode="NEVER")

user.initiate_chat(assistant, message="What is 10 + 5?")
user.send(assistant, message="Now square that number")
