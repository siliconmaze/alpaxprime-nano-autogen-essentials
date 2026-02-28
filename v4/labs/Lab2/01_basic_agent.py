"""
Lab 2: Single Agent Fundamentals
================================

This lab covers creating and using a basic AutoGen AssistantAgent.

Key Concepts:
- AssistantAgent: The AI-powered agent
- llm_config: Model configuration
- generate_reply: Synchronous message handling
- Messages: List of message dictionaries

Run with:
    python 01_basic_agent.py
"""

import os
from dotenv import load_dotenv
from autogen import AssistantAgent

# Load environment
load_dotenv()

print("=" * 60)
print("Lab 2: Single Agent Fundamentals")
print("=" * 60)

# ============================================================================
# CONFIGURATION
# ============================================================================

# Get API key - modify this for your provider
api_key = os.getenv("DEEPSEEK_API_KEY", "")
model = "deepseek-chat"
base_url = "https://api.deepseek.com/v1"

# Fallback to Ollama if no API key
if not api_key:
    print("⚠️  No DEEPSEEK_API_KEY, using Ollama")
    model = "qwen2.5-coder:7b"
    base_url = "http://localhost:11434/v1"
    api_key = "ollama"

# Create config list
config_list = [
    {
        "model": model,
        "base_url": base_url,
        "api_key": api_key,
    }
]

print(f"\nUsing model: {model}")

# ============================================================================
# CREATE AGENT
# ============================================================================

print("\n[1] Creating AssistantAgent...")

# Basic agent
assistant = AssistantAgent(
    name="my_assistant",
    llm_config={"config_list": config_list}
)

print(f"    Created: {assistant.name}")
print(f"    Type: {type(assistant).__name__}")

# ============================================================================
# SEND MESSAGE
# ============================================================================

print("\n[2] Sending message to agent...")

# Method 1: Using generate_reply (simple)
response = assistant.generate_reply(
    messages=[{"role": "user", "content": "What is 2 + 2? Answer with just the number."}]
)

print(f"    Response: {response}")

# ============================================================================
# MORE EXAMPLES
# ============================================================================

print("\n[3] More examples...")

# Example 1: Coding task
response1 = assistant.generate_reply(
    messages=[{"role": "user", "content": "Write a Python function that returns True if a string is a palindrome."}]
)
print(f"\n    [Coding] {response1[:100]}...")

# Example 2: Explanation
response2 = assistant.generate_reply(
    messages=[{"role": "user", "content": "Explain what a transformer model is in one sentence."}]
)
print(f"\n    [Explanation] {response2}")

print("\n" + "=" * 60)
print("✓ Lab 2 Complete!")
print("=" * 60)
