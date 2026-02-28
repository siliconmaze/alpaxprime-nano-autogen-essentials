"""
Lab 5: Group Chat & Orchestration
==================================

This lab covers multi-agent group conversations using GroupChat.

Key Concepts:
- GroupChat: Container for multiple agents
- GroupChatManager: Orchestrates the conversation
- Speaker selection: How agents take turns
- max_round: Limit conversation length

Run with:
    python 01_group_chat.py
"""

import os
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager

load_dotenv()

print("=" * 60)
print("Lab 5: Group Chat & Orchestration")
print("=" * 60)

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
# CREATE AGENTS WITH DIFFERENT ROLES
# ============================================================================

print("\n[1] Creating agents...")

# Agent 1: Writer
writer = AssistantAgent(
    name="writer",
    system_message="""You are a creative writer.
Write engaging, descriptive content.
Keep responses concise.""",
    llm_config={"config_list": config_list}
)

# Agent 2: Editor
editor = AssistantAgent(
    name="editor",
    system_message="""You are an editor.
Improve clarity and grammar.
Suggest edits when needed.""",
    llm_config={"config_list": config_list}
)

# Agent 3: Fact Checker
fact_checker = AssistantAgent(
    name="fact_checker",
    system_message="""You verify facts.
Check claims for accuracy.
State clearly if something is incorrect.""",
    llm_config={"config_list": config_list}
)

print(f"    Created: {writer.name}, {editor.name}, {fact_checker.name}")

# ============================================================================
# CREATE GROUP CHAT
# ============================================================================

print("\n[2] Creating group chat...")

groupchat = GroupChat(
    agents=[writer, editor, fact_checker],
    messages=[],
    max_round=6,  # Limit conversation turns
)

print(f"    Group chat created with {len(groupchat.agents)} agents")

# ============================================================================
# CREATE MANAGER
# ============================================================================

print("\n[3] Creating manager...")

manager = GroupChatManager(
    groupchat=groupchat,
    llm_config={"config_list": config_list}
)

print("    Manager ready")

# ============================================================================
# START GROUP CONVERSATION
# ============================================================================

print("\n[4] Starting group conversation...")

user_proxy = UserProxyAgent(
    name="user",
    human_input_mode="NEVER"
)

# Start the group chat
user_proxy.initiate_chat(
    manager,
    message="Write a short paragraph about AI, then have the editor improve it, and fact checker verify any claims."
)

print("\n    ✓ Group conversation complete!")

# ============================================================================
# VIEW CONVERSATION
# ============================================================================

print("\n[5] Conversation summary:")
for i, msg in enumerate(groupchat.messages[-3:]):
    role = msg.get("role", "unknown")
    content = msg.get("content", "")[:80]
    print(f"    {i+1}. [{role}] {content}...")

print("\n" + "=" * 60)
print("✓ Group Chat Complete!")
print("=" * 60)
