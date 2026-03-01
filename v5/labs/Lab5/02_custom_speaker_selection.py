"""Lab 5 - Custom Speaker Selection"""
import sys
sys.path.insert(0, '../../..')
from config import get_ollama_config
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager

agent1 = AssistantAgent("A", llm_config={"config_list": get_ollama_config()})
agent2 = AssistantAgent("B", llm_config={"config_list": get_ollama_config()})
agent3 = AssistantAgent("C", llm_config={"config_list": get_ollama_config()})

def select_next(last_speaker, last_message):
    if last_speaker is None: return agent1
    if last_speaker.name == "A": return agent2
    if last_speaker.name == "B": return agent3
    return agent1

groupchat = GroupChat(
    agents=[agent1, agent2, agent3],
    messages=[],
    speaker_selection_method=select_next,
    max_round=3
)
manager = GroupChatManager(groupchat=groupchat, llm_config={"config_list": get_ollama_config()})

user = UserProxyAgent("user", human_input_mode="NEVER")
user.initiate_chat(manager, message="Each of you say hello")
