"""
Lab 2: Agent with LLM Options
=============================

Configure agent with specific LLM options.

Key Concepts:
- temperature: Randomness (0=deterministic, 2=creative)
- max_tokens: Maximum response length
- top_p: Nucleus sampling
- timeout: Request timeout

Run with:
    python 03_agent_with_llm_options.py
"""

import os
from dotenv import load_dotenv
from autogen import AssistantAgent

load_dotenv()

print("=" * 60)
print("Lab 2: LLM Options")
print("=" * 60)

api_key = os.getenv("DEEPSEEK_API_KEY", "")
if not api_key:
    api_key = "ollama"
    model = "qwen2.5-coder:7b"
    base_url = "http://localhost:11434/v1"
else:
    model = "deepseek-chat"
    base_url = "https://api.deepseek.com/v1"

# ============================================================================
# EXAMPLE 1: LOW TEMPERATURE (Deterministic)
# ============================================================================

print("\n[1] Temperature=0 (Deterministic)")

config_list = [{"model": model, "base_url": base_url, "api_key": api_key}]

deterministic_agent = AssistantAgent(
    name="deterministic",
    llm_config={
        "config_list": config_list,
        "temperature": 0,  # Same input = same output
    }
)

# Ask same question twice
r1 = deterministic_agent.generate_reply(
    messages=[{"role": "user", "content": "What is 1+1?"}]
)
r2 = deterministic_agent.generate_reply(
    messages=[{"role": "user", "content": "What is 1+1?"}]
)
print(f"    Response 1: {r1}")
print(f"    Response 2: {r2}")

# ============================================================================
# EXAMPLE 2: HIGH TEMPERATURE (Creative)
# ============================================================================

print("\n[2] Temperature=1.5 (Creative)")

creative_agent = AssistantAgent(
    name="creative",
    llm_config={
        "config_list": config_list,
        "temperature": 1.5,  # More varied responses
    }
)

r1 = creative_agent.generate_reply(
    messages=[{"role": "user", "content": "Write a creative opening line for a story"}]
)
print(f"    Response: {r1[:100]}...")

# ============================================================================
# EXAMPLE 3: MAX TOKENS LIMIT
# ============================================================================

print("\n[3] max_tokens=50 (Short Response)")

short_agent = AssistantAgent(
    name="short",
    llm_config={
        "config_list": config_list,
        "max_tokens": 50,  # Limit response length
    }
)

r = short_agent.generate_reply(
    messages=[{"role": "user", "content": "Explain quantum computing"}]
)
print(f"    Response: {r}")

# ============================================================================
# EXAMPLE 4: ALL OPTIONS COMBINED
# ============================================================================

print("\n[4] All options combined")

balanced_agent = AssistantAgent(
    name="balanced",
    llm_config={
        "config_list": config_list,
        "temperature": 0.7,
        "max_tokens": 500,
        "top_p": 0.9,
        "timeout": 120,  # seconds
    }
)

r = balanced_agent.generate_reply(
    messages=[{"role": "user", "content": "What are the benefits of exercise?"}]
)
print(f"    Response: {r[:150]}...")

print("\n" + "=" * 60)
print("✓ LLM Options Complete!")
print("=" * 60)
