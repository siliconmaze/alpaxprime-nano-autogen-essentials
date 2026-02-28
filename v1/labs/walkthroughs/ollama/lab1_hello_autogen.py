"""Lab 1: Hello AutoGen - Modified for Ollama
This lab verifies AutoGen installation with Ollama as the LLM provider
"""

import sys
sys.path.insert(0, '/Users/stever/.pyenv/versions/3.12.8/envs/gen/lib/python3.12/site-packages')

from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_ext.models import OllamaChatCompletionClient

print("✓ Imports successful")

# Create Ollama client
ollama_client = OllamaChatCompletionClient(
    model="qwen2.5-coder:7b",
    base_url="http://localhost:11434",
)

print(f"✓ Configured Ollama model: qwen2.5-coder:7b")
print(f"✓ Base URL: http://localhost:11434")

# Create an AssistantAgent
assistant = AssistantAgent(
    name="assistant",
    model_client=ollama_client,
    system_message="You are a helpful AI assistant."
)

print("✓ Created AssistantAgent")

# Create a UserProxyAgent
user_proxy = UserProxyAgent(
    name="user_proxy",
)

print("✓ Created UserProxyAgent")

# Test the agent with a simple message
print("\n" + "="*50)
print("Testing agent with simple message...")
print("="*50)

import asyncio

async def main():
    try:
        result = await user_proxy.run_chat(
            messages=["Say hello and tell me what you are."],
            chat_agent=assistant,
        )
        print("\n" + "="*50)
        print("RESPONSE:")
        print("="*50)
        for msg in result.messages:
            print(f"{msg.source}: {msg.content}")
        print("\n✓ Lab 1 SUCCESS - AutoGen with Ollama is working!")
    except Exception as e:
        print(f"\n✗ Error during chat: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

asyncio.run(main())
