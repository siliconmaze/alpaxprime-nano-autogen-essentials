"""Lab 1 Solution: Verify AutoGen Installation"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the OPENAI_API_KEY from environment
api_key = os.getenv("OPENAI_API_KEY")

# Check if API key exists
if not api_key:
    print("⚠️  WARNING: OPENAI_API_KEY not found in environment")
    print("Please set your API key in .env or export OPENAI_API_KEY")
    exit(1)

# Import autogen
import autogen

# Create a config_list with your API key
config_list = [
    {
        "model": "gpt-4",
        "api_key": api_key
    }
]

# Create an AssistantAgent
assistant = autogen.AssistantAgent(
    name="test_agent",
    llm_config={"config_list": config_list}
)

print("\n" + "="*50)
print("✓ AutoGen version:", autogen.__version__)
print("✓ AssistantAgent created successfully!")
print("🎉 All checks passed! AutoGen is ready to use.")
print("="*50)
