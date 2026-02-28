"""Lab 4 Solution: GroupChat"""
import os
from dotenv import load_dotenv
import autogen
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

config_list = [{"model": "gpt-4", "api_key": api_key}]

# Create specialized agents
researcher = AssistantAgent(
    name="researcher",
    llm_config={"config_list": config_list},
    system_message="You are a research specialist. Find accurate information and cite sources."
)

writer = AssistantAgent(
    name="writer",
    llm_config={"config_list": config_list},
    system_message="You are a technical writer. Create clear, engaging content."
)

editor = AssistantAgent(
    name="editor",
    llm_config={"config_list": config_list},
    system_message="You are an editor. Review and improve content for clarity and accuracy."
)

# Create UserProxyAgent
user_proxy = UserProxyAgent(
    name="user",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10
)

# Create GroupChat
groupchat = GroupChat(
    agents=[user_proxy, researcher, writer, editor],
    messages=[],
    max_round=12
)

# Create manager
manager = GroupChatManager(
    groupchat=groupchat,
    llm_config={"config_list": config_list}
)

# Start group conversation
user_proxy.initiate_chat(
    manager,
    message="Write a short paragraph about quantum computing. Researcher finds info, Writer creates content, Editor reviews."
)

print("\n✓ GroupChat completed!")
