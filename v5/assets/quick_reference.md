# AutoGen Quick Reference Card

## Installation
```bash
pip install pyautogen python-dotenv
```

## Basic Agent
```python
from autogen import AssistantAgent
agent = AssistantAgent(name="bot", llm_config={"config_list": config})
```

## Two-Agent Chat
```python
from autogen import AssistantAgent, UserProxyAgent
user = UserProxyAgent("user", human_input_mode="NEVER")
user.initiate_chat(assistant, message="Hello")
```

## Tools
```python
agent = AssistantAgent(llm_config={"tools": [{"function": my_func, "description": "..."}]})
```

## Group Chat
```python
from autogen import GroupChat, GroupChatManager
chat = GroupChat(agents=[agent1, agent2])
manager = GroupChatManager(groupchat=chat)
```

## Human-in-the-Loop
```python
UserProxyAgent("user", human_input_mode="ALWAYS")  # Always ask
UserProxyAgent("user", human_input_mode="TERMINATE")  # When needed
UserProxyAgent("user", human_input_mode="NEVER")  # Never ask
```

## LLM Options
```python
llm_config={
    "temperature": 0.7,
    "max_tokens": 2000,
    "top_p": 0.9
}
```

## Providers
- Ollama: `http://localhost:11434/v1`
- DeepSeek: `https://api.deepseek.com/v1`
- MiniMax: `https://api.minimax.io/anthropic/v1`
