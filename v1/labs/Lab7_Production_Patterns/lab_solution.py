"""Lab 7 Solution: Production Patterns - Error Handling"""
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

# Create agents
assistant = AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list}
)

user_proxy = UserProxyAgent(
    name="user",
    human_input_mode="NEVER"
)

# Wrap conversation in try-except
try:
    user_proxy.initiate_chat(
        assistant,
        message="Explain what AutoGen is in one sentence."
    )
    print("\n✓ Conversation completed successfully!")
except Exception as e:
    logger.error(f"Conversation failed: {e}")
    print("\n⚠️ Something went wrong, but we handled it gracefully!")

print("\n✓ Error handling pattern demonstrated!")
