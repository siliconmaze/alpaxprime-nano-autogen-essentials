"""Lab 1: Hello AutoGen - MiniMax Walkthrough"""
import os
from autogen import AssistantAgent

# Load MiniMax from .env.local
from dotenv import load_dotenv
load_dotenv("/Users/stever/local-repos/github/_ALPAXPRIME_NANO/alpaxprime-nano-engine/.env.local")

minimax_key = os.getenv("MINIMAX_API_KEY")
minimax_url = os.getenv("MINIMAX_BASE_URL", "https://api.minimax.io/anthropic")

config_list = [
    {
        "model": "MiniMax-Text-01",
        "base_url": f"{minimax_url}/v1",
        "api_key": minimax_key,
    }
]

assistant = AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list}
)

response = assistant.generate_reply(messages=[{"role": "user", "content": "Say hello and introduce yourself"}])
print("=" * 50)
print("MINIMAX LAB 1 RESULT")
print("=" * 50)
print(f"Response: {response}")
print("=" * 50)
print("✓ Lab 1 Complete - MiniMax working!")
