"""
Lab 6: Human-in-the-Loop Patterns
===================================

Add human approval and interaction to agent workflows.

Key Concepts:
- human_input_mode: ALWAYS, NEVER, TERMINATE
- Human intervention points
- Approval workflows

Run with:
    python 01_human_in_loop.py
"""

import os
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent

load_dotenv()

print("=" * 60)
print("Lab 6: Human-in-the-Loop Patterns")
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
# MODE 1: NEVER (Fully Automated)
# ============================================================================

print("\n[1] Mode: NEVER (Fully Automated)")

assistant = AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list}
)

user_auto = UserProxyAgent(
    name="user_auto",
    human_input_mode="NEVER"  # No human input needed
)

# This will run automatically
response = user_auto.generate_reply(
    messages=[{"role": "user", "content": "What is 2+2?"}],
    sender=assistant
)
print(f"    Auto response: {response}")

# ============================================================================
# MODE 2: TERMINATE (Ask at End)
# ============================================================================

print("\n[2] Mode: TERMINATE (Ask at End)")

# This mode would ask for human input when conversation ends
# Useful for approval workflows

approval_agent = AssistantAgent(
    name="approval_agent",
    system_message="You are an assistant that helps with approvals.",
    llm_config={"config_list": config_list}
)

# In practice, you would use:
# user_approval = UserProxyAgent(name="user", human_input_mode="TERMINATE")

print("    (TERMINATE mode would prompt at conversation end)")
print("    Use case: Approval before executing sensitive actions")

# ============================================================================
# SIMULATE APPROVAL WORKFLOW
# ============================================================================

print("\n[3] Simulated Approval Workflow")

# Agent suggests action
suggestion = approval_agent.generate_reply(
    messages=[{"role": "user", "content": "Suggest a file to delete (do not actually delete anything)"}]
)
print(f"    Agent suggestion: {suggestion[:60]}...")

# Human would approve here
print("    → Human reviews suggestion...")
print("    → Human approves or rejects...")

# Execute based on approval
print("    → Action executed (in real scenario)")

print("\n" + "=" * 60)
print("✓ Human-in-the-Loop Complete!")
print("=" * 60)
