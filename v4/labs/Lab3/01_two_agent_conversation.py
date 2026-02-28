"""
Lab 3: Two-Agent Conversations
================================

This lab covers setting up conversations between two agents:
- AssistantAgent: The AI that responds
- UserProxyAgent: Represents the user (can auto-reply or get human input)

Key Concepts:
- Two-agent chat flow
- UserProxyAgent with human_input_mode
- initiate_chat: Start a conversation
- Sequential message passing

Run with:
    python 01_two_agent_conversation.py
"""

import os
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent

load_dotenv()

print("=" * 60)
print("Lab 3: Two-Agent Conversations")
print("=" * 60)

# Configuration
api_key = os.getenv("DEEPSEEK_API_KEY", "")
if not api_key:
    api_key = "ollama"
    model = "qwen2.5-coder:7b"
    base_url = "http://localhost:11434/v1"
else:
    model = "deepseek-chat"
    base_url = "https://api.deepseek.com/v1"

config_list = [{"model": model, "base_url": base_url, "api_key": api_key}]

# ============================================================================
# EXAMPLE 1: SIMPLE TWO-AGENT CHAT
# ============================================================================

print("\n[1] Simple Two-Agent Conversation")

# Create the assistant agent (the AI)
assistant = AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list}
)

# Create the user proxy (represents the user)
user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER"  # No human needed, auto-reply
)

# Start conversation
print("    Starting conversation...")

user_proxy.initiate_chat(
    assistant,
    message="Write a haiku about AI"
)

print(f"    ✓ Conversation complete!")

# ============================================================================
# EXAMPLE 2: CODE WRITER + REVIEWER
# ============================================================================

print("\n[2] Code Writer + Code Reviewer")

# Code writer agent
code_writer = AssistantAgent(
    name="code_writer",
    system_message="""You are a Python code writer.
Write clean, efficient, well-commented code.
Only output the code, no explanations.""",
    llm_config={"config_list": config_list}
)

# Code reviewer agent
code_reviewer = AssistantAgent(
    name="code_reviewer",
    system_message="""You are a code reviewer.
Review the code and provide constructive feedback.
Focus on: bugs, performance, readability, best practices.""",
    llm_config={"config_list": config_list}
)

# User proxy to initiate
initiator = UserProxyAgent(
    name="initiator",
    human_input_mode="NEVER"
)

# Step 1: Generate code
print("    [Step 1] Writing code...")
initiator.initiate_chat(
    code_writer,
    message="Write a Python function to reverse a string"
)
code_response = code_writer.last_message()["content"]
print(f"    Code written: {code_response[:80]}...")

# Step 2: Review code
print("    [Step 2] Reviewing code...")
# Pass previous context manually for this example
reviewer_response = code_reviewer.generate_reply(
    messages=[
        {"role": "user", "content": f"Review this code:\n{code_response}"}
    ]
)
print(f"    Review: {reviewer_response[:100]}...")

print("\n" + "=" * 60)
print("✓ Two-Agent Conversations Complete!")
print("=" * 60)
