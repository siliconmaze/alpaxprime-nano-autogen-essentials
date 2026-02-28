"""Lab 7 Starter: Production Patterns
Your task: Add error handling to a conversation
"""

import os
import logging
from dotenv import load_dotenv
import autogen
from autogen import AssistantAgent, UserProxyAgent

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

config_list = [{"model": "gpt-4", "api_key": api_key}]

# TODO: Create an AssistantAgent


# TODO: Create a UserProxyAgent


# TODO: Wrap the conversation in a try-except block to handle errors gracefully

# Hint: 
# try:
#     user_proxy.initiate_chat(assistant, message="...")
# except Exception as e:
#     logger.error(f"Error: {e}")
#     print("Something went wrong, but we handled it!")

print("Production patterns demo!")
