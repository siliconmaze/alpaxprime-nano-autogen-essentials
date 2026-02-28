"""Lab 4 Starter: GroupChat
Your task: Create a groupchat with multiple specialized agents
"""

import os
from dotenv import load_dotenv
import autogen
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

config_list = [{"model": "gpt-4", "api_key": api_key}]

# Create three specialized agents
# TODO: Create "researcher" - finds information


# TODO: Create "writer" - creates content  


# TODO: Create "editor" - reviews content


# TODO: Create UserProxyAgent


# TODO: Create GroupChat with all agents


# TODO: Create GroupChatManager


# TODO: Start conversation about a topic of your choice

print("GroupChat started! Watch the conversation.")
