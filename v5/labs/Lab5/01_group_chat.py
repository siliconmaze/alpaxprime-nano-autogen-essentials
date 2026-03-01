"""Lab 5 - Basic Group Chat"""
import sys
sys.path.insert(0, '../../..')
from config import get_ollama_config
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager

writer = AssistantAgent("writer", llm_config={"config_list": get_ollama_config()})
editor = AssistantAgent("editor", llm_config={"config_list": get_ollama_config()})

groupchat = GroupChat(agents=[writer, editor], messages=[], max_round=4)
manager = GroupChatManager(groupchat=groupchat, llm_config={"config_list": get_ollama_config()})

user = UserProxyAgent("user", human_input_mode="NEVER")
user.initiate_chat(manager, message="Write and edit a haiku")
