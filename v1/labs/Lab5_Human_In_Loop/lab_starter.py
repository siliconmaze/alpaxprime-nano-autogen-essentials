"""Lab 5 Starter: Human-in-the-Loop
Your task: Create an agent workflow with human approval
"""

import os
from dotenv import load_dotenv
import autogen
from autogen import AssistantAgent, UserProxyAgent

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

config_list = [{"model": "gpt-4", "api_key": api_key}]

# Create an assistant agent
assistant = AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list},
    system_message="You are a helpful assistant. When done, say 'FINISHED'."
)

# TODO: Create a UserProxyAgent with human_input_mode="TERMINATE"
# hint: The agent will ask for human input when it wants to terminate


# TODO: Set a custom termination message check
# hint: is_termination_msg=lambda x: "FINISHED" in x.get("content", "")


# TODO: Start a conversation asking for something simple

print("Start the conversation and provide input when prompted!")
