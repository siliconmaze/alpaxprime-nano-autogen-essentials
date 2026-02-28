"""Lab 2 Solution: Two-Agent Conversation"""
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

# Create AssistantAgent
assistant = AssistantAgent(
    name="code_assistant",
    llm_config={"config_list": config_list},
    system_message="You are a helpful Python coding assistant. Write clean, well-documented code."
)

# Create UserProxyAgent
user_proxy = UserProxyAgent(
    name="human_user",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    code_execution_config={
        "work_dir": "code_output",
        "use_docker": False
    }
)

# Start conversation
user_proxy.initiate_chat(
    assistant,
    message="Create a Python class for managing a simple todo list with add, complete, and list operations."
)

print("\n✓ Conversation completed!")
