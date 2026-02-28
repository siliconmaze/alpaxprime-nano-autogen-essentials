"""Lab 1: Hello AutoGen - DeepSeek Walkthrough"""
import os
from autogen import AssistantAgent

# Load DeepSeek from .env.local
from dotenv import load_dotenv
load_dotenv("/Users/stever/local-repos/github/_ALPAXPRIME_NANO/alpaxprime-nano-engine/.env.local")

deepseek_key = os.getenv("DEEPSEEK_API_KEY")
deepseek_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")

config_list = [
    {
        "model": "deepseek-chat",
        "base_url": f"{deepseek_url}/v1",
        "api_key": deepseek_key,
    }
]

assistant = AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list}
)

response = assistant.generate_reply(messages=[{"role": "user", "content": "Say hello and introduce yourself"}])
print("=" * 50)
print("DEEPSEEK LAB 1 RESULT")
print("=" * 50)
print(f"Response: {response}")
print("=" * 50)
print("✓ Lab 1 Complete - DeepSeek working!")
