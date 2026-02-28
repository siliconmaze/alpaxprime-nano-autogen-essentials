"""
Lab 2: Agent with Custom System Message
=========================================

Customize agent behavior using system_message parameter.

Key Concepts:
- system_message: Defines agent persona and instructions
- Temperature: Controls randomness (0-2)
- max_tokens: Limits response length
- Top_p: Nucleus sampling

Run with:
    python 02_agent_with_system_message.py
"""

import os
from dotenv import load_dotenv
from autogen import AssistantAgent

load_dotenv()

print("=" * 60)
print("Lab 2: Custom System Message")
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
# EXAMPLE 1: Helpful Coding Assistant
# ============================================================================

print("\n[1] Coding Assistant Persona")

coding_assistant = AssistantAgent(
    name="coder",
    system_message="""You are an expert Python developer.
- Write clean, readable code with comments
- Always handle errors appropriately
- Prefer Pythonic solutions
- Explain your code briefly""",
    llm_config={"config_list": config_list}
)

response = coding_assistant.generate_reply(
    messages=[{"role": "user", "content": "Write a function to calculate fibonacci numbers"}]
)
print(f"    Response: {response[:200]}...")

# ============================================================================
# EXAMPLE 2: Concise Summary Expert
# ============================================================================

print("\n[2] Concise Summary Persona")

summarizer = AssistantAgent(
    name="summarizer",
    system_message="""You summarize content in exactly 3 sentences.
- First sentence: main topic
- Second sentence: key points
- Third sentence: conclusion
- Be direct and brief""",
    llm_config={"config_list": config_list}
)

response = summarizer.generate_reply(
    messages=[{"role": "user", "content": """Artificial intelligence (AI) is intelligence demonstrated by machines, 
    in contrast to the natural intelligence displayed by humans and animals. 
    Leading AI textbooks define the field as the study of "intelligent agents": 
    any device that perceives its environment and takes actions that maximize its chance 
    of successfully achieving its goals. AI applications include advanced web search engines, 
    recommendation systems, autonomous vehicles, generative AI tools, and more."""}]
)
print(f"    Summary: {response}")

# ============================================================================
# EXAMPLE 3: Technical Writer
# ============================================================================

print("\n[3] Technical Writer Persona")

tech_writer = AssistantAgent(
    name="tech_writer",
    system_message="""You write documentation for developers.
- Use clear, simple English
- Include code examples
- Follow Markdown format
- Be thorough but concise""",
    llm_config={"config_list": config_list}
)

response = tech_writer.generate_reply(
    messages=[{"role": "user", "content": "Document the Python 'print' function"}]
)
print(f"    Documentation: {response[:150]}...")

print("\n" + "=" * 60)
print("✓ Custom System Messages Complete!")
print("=" * 60)
