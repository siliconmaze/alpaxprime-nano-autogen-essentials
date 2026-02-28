"""Lab 5 Solution: Human-in-the-Loop"""
import os
from dotenv import load_dotenv
import autogen
from autogen import AssistantAgent, UserProxyAgent

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

config_list = [{"model": "gpt-4", "api_key": api_key}]

# Create assistant
assistant = AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list},
    system_message="You are a helpful assistant. When complete, say 'FINISHED'."
)

# Create UserProxyAgent with TERMINATE mode
user_proxy = UserProxyAgent(
    name="user",
    human_input_mode="TERMINATE",  # Ask for input when agent wants to end
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: "FINISHED" in x.get("content", "")
)

# Start conversation
user_proxy.initiate_chat(
    assistant,
    message="Write a haiku about coding."
)

print("\n✓ Human-in-the-loop workflow completed!")
