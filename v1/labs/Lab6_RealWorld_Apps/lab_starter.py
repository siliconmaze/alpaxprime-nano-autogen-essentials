"""Lab 6 Starter: Real-World Applications
Your task: Build a simple code review system
"""

import os
from dotenv import load_dotenv
import autogen
from autogen import AssistantAgent, UserProxyAgent

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

config_list = [{"model": "gpt-4", "api_key": api_key}]

# TODO: Create a "reviewer" agent with system message about code quality


# TODO: Create a UserProxyAgent to act as the code submitter


# TODO: Write some sample code to review (with intentional issues)


# TODO: Start the conversation to review the code

# Hint: Include code with issues like:
# - Hardcoded passwords
# - SQL injection vulnerability  
# - No error handling

print("Starting code review...")
