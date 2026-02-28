"""Lab 3 Starter: Tools and Functions
Your task: Create a custom function and register it with an agent
"""

import os
from dotenv import load_dotenv
import autogen
from autogen import AssistantAgent, UserProxyAgent

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Define a custom function
def calculate(operation: str, a: float, b: float) -> str:
    """
    Perform basic mathematical operations.
    
    Args:
        operation: One of add, subtract, multiply, divide
        a: First number
        b: Second number
    
    Returns:
        Result of the operation
    """
    # TODO: Implement the math operations


# TODO: Register the function with AutoGen
# hint: autogen.agentchat.register_function(...)

# Configuration
config_list = [{"model": "gpt-4", "api_key": api_key}]

# TODO: Create AssistantAgent with the function in llm_config["functions"]


# TODO: Create UserProxyAgent with human_input_mode="NEVER"


# TODO: Start conversation asking to calculate 10 + 5 and 20 * 3

print("Run this script to test your tool!")
