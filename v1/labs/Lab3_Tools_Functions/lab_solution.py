"""Lab 3 Solution: Tools and Functions"""
import os
from dotenv import load_dotenv
import autogen
from autogen import AssistantAgent, UserProxyAgent

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Define a custom function
def calculate(operation: str, a: float, b: float) -> str:
    """Perform basic mathematical operations."""
    ops = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else "Error: Division by zero"
    }
    
    op = operation.lower()
    if op not in ops:
        return f"Error: Unknown operation '{operation}'. Use: add, subtract, multiply, divide"
    
    result = ops[op](a, b)
    return f"{a} {operation} {b} = {result}"

# Register the function
autogen.agentchat.register_function(
    calculate,
    name="calculate",
    description="Perform basic mathematical calculations"
)

# Configuration
config_list = [{"model": "gpt-4", "api_key": api_key}]

# Create AssistantAgent with function
assistant = AssistantAgent(
    name="math_assistant",
    llm_config={
        "config_list": config_list,
        "functions": [
            {
                "name": "calculate",
                "description": "Perform basic mathematical calculations (add, subtract, multiply, divide)",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "operation": {
                            "type": "string",
                            "enum": ["add", "subtract", "multiply", "divide"],
                            "description": "The mathematical operation"
                        },
                        "a": {"type": "number", "description": "First number"},
                        "b": {"type": "number", "description": "Second number"}
                    },
                    "required": ["operation", "a", "b"]
                }
            }
        ]
    }
)

# Create UserProxyAgent
user_proxy = UserProxyAgent(
    name="user",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=5
)

# Start conversation
user_proxy.initiate_chat(
    assistant,
    message="Calculate 10 + 5, 20 - 8, 6 * 7, and 100 / 4 using the calculate function."
)

print("\n✓ Tool calling completed!")
