"""Lab 2 Starter: Two-Agent Conversation
Your task: Create a conversation between UserProxyAgent and AssistantAgent
"""

import os
from dotenv import load_dotenv
import autogen
from autogen import AssistantAgent, UserProxyAgent

# Load environment
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Configuration
config_list = [
    {
        "model": "gpt-4",
        "api_key": api_key
    }
]

# TODO: Create AssistantAgent named "code_assistant"
# with system_message: "You are a helpful Python coding assistant."


# TODO: Create UserProxyAgent named "human_user"
# - human_input_mode: "NEVER"
# - max_consecutive_auto_reply: 10


# TODO: Start the conversation with a message asking for a Python class
# hint: user_proxy.initiate_chat(assistant, message="...")

print("Conversation started! Check the output above.")
