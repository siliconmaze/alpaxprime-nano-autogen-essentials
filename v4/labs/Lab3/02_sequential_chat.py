"""
Lab 3: Sequential Chat Patterns
================================

Chain multiple conversations together.

Key Concepts:
- Sequential messages passing context
- Multi-step workflows
- Context preservation

Run with:
    python 02_sequential_chat.py
"""

import os
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent

load_dotenv()

print("=" * 60)
print("Lab 3: Sequential Chat Patterns")
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
# RESEARCH + SUMMARIZE WORKFLOW
# ============================================================================

print("\n[1] Research → Summarize Workflow")

researcher = AssistantAgent(
    name="researcher",
    system_message="You research topics thoroughly. Provide detailed information.",
    llm_config={"config_list": config_list}
)

summarizer = AssistantAgent(
    name="summarizer",
    system_message="You summarize content briefly in 3 sentences.",
    llm_config={"config_list": config_list}
)

user = UserProxyAgent(name="user", human_input_mode="NEVER")

# Step 1: Research
print("    Step 1: Researching...")
user.initiate_chat(researcher, message="What is quantum computing?")
research_result = researcher.last_message()["content"]
print(f"    Research done: {len(research_result)} chars")

# Step 2: Summarize (with context from step 1)
print("    Step 2: Summarizing...")
# Note: In this simple version, we pass the research as context
summary = summarizer.generate_reply(
    messages=[
        {"role": "user", "content": f"Summarize this:\n{research_result[:500]}..."}
    ]
)
print(f"    Summary: {summary}")

# ============================================================================
# DRAFT → EDIT → FINALIZE
# ============================================================================

print("\n[2] Draft → Edit → Finalize Workflow")

writer = AssistantAgent(
    name="writer",
    system_message="Write creative, engaging content.",
    llm_config={"config_list": config_list}
)

editor = AssistantAgent(
    name="editor",
    system_message="Edit content for clarity and grammar. Keep it concise.",
    llm_config={"config_list": config_list}
)

finalizer = AssistantAgent(
    name="finalizer",
    system_message="Polish content to perfection. Output final version.",
    llm_config={"config_list": config_list}
)

user = UserProxyAgent(name="user", human_input_mode="NEVER")

# Draft
user.initiate_chat(writer, message="Write a short paragraph about the ocean")
draft = writer.last_message()["content"]
print(f"    Draft: {draft[:60]}...")

# Edit
user.initiate_chat(editor, message=f"Edit this:\n{draft}")
edited = editor.last_message()["content"]
print(f"    Edited: {edited[:60]}...")

# Finalize
user.initiate_chat(finalizer, message=f"Polish this:\n{edited}")
final = finalizer.last_message()["content"]
print(f"    Final: {final[:60]}...")

print("\n" + "=" * 60)
print("✓ Sequential Chat Complete!")
print("=" * 60)
