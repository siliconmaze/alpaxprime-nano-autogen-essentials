# AutoGen Course - Quick Reference

## Installation
```bash
pip install pyautogen python-dotenv
```

## Basic Agents
```python
from autogen import AssistantAgent, UserProxyAgent

# AI-powered agent
assistant = AssistantAgent(name="assistant", llm_config={"config_list": config_list})

# Human proxy
user_proxy = UserProxyAgent(name="user", human_input_mode="NEVER")
```

## Start Conversation
```python
user_proxy.initiate_chat(assistant, message="Hello!")
```

## GroupChat
```python
from autogen import GroupChat, GroupChatManager

groupchat = GroupChat(agents=[agent1, agent2, agent3])
manager = GroupChatManager(groupchat=groupchat, llm_config={"config_list": config_list})
```

## Human Input Modes
- `NEVER` - Fully automated
- `ALWAYS` - Always ask human
- `TERMINATE` - Ask at termination

## Tools
Register functions:
```python
autogen.agentchat.register_function(my_function, name="func_name", description="...")
```

## Code Execution
```python
user_proxy = UserProxyAgent(
    code_execution_config={"work_dir": "output", "use_docker": False}
)
```
