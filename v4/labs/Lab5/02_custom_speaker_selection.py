"""
Lab 5: Custom Speaker Selection
================================

Control how agents take turns in group chat.

Key Concepts:
- allowed_or_disallowed_speaker_transitions
- speaker_selection_method
- Custom speaker logic

Run with:
    python 02_custom_speaker_selection.py
"""

import os
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager

load_dotenv()

print("=" * 60)
print("Lab 5: Custom Speaker Selection")
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
# TEAM: RESEARCH → WRITE → REVIEW
# ============================================================================

researcher = AssistantAgent(
    name="researcher",
    system_message="Research topics thoroughly.",
    llm_config={"config_list": config_list}
)

writer = AssistantAgent(
    name="writer", 
    system_message="Write content based on research.",
    llm_config={"config_list": config_list}
)

reviewer = AssistantAgent(
    name="reviewer",
    system_message="Review and critique content.",
    llm_config={"config_list": config_list}
)

# ============================================================================
# CUSTOM SPEAKER RULES
# ============================================================================

print("\n[1] Setting up custom speaker transitions...")

# Define who can speak after whom
# Format: {speaker: [allowed_next_speakers]}
allowed_transitions = {
    "researcher": ["writer"],
    "writer": ["reviewer"],
    "reviewer": ["writer", "researcher"],  # Can loop back
}

groupchat = GroupChat(
    agents=[researcher, writer, reviewer],
    messages=[],
    max_round=8,
    allowed_or_disallowed_speaker_transitions=allowed_transitions,
    speaker_selection_method="round_robin",  # Or "auto"
)

print("    Speaker transitions configured")

manager = GroupChatManager(
    groupchat=groupchat,
    llm_config={"config_list": config_list}
)

# ============================================================================
# RUN
# ============================================================================

user_proxy = UserProxyAgent(name="user", human_input_mode="NEVER")

print("\n[2] Running workflow...")
user_proxy.initiate_chat(
    manager,
    message="Research the topic 'machine learning' and write a summary, then have it reviewed."
)

print("\n    ✓ Workflow complete!")

print("\n" + "=" * 60)
print("✓ Custom Speaker Selection Complete!")
print("=" * 60)
