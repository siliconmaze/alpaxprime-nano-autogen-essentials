# Lab 5: Group Chat & Orchestration

## Objectives

- Create multi-agent group conversations
- Configure GroupChatManager
- Control speaker selection
- Build collaborative workflows

---

## Key Concepts

### GroupChat

```python
from autogen import GroupChat

groupchat = GroupChat(
    agents=[agent1, agent2, agent3],
    messages=[],
    max_round=10
)
```

### GroupChatManager

```python
manager = GroupChatManager(
    groupchat=groupchat,
    llm_config={"config_list": config_list}
)
```

---

## Examples

### Example 1: Three-Agent Team

```python
writer = AssistantAgent(name="writer", ...)
editor = AssistantAgent(name="editor", ...)
critic = AssistantAgent(name="critic", ...)

groupchat = GroupChat(agents=[writer, editor, critic], max_round=6)
manager = GroupChatManager(groupchat=groupchat, llm_config={"config_list": config_list})

user_proxy.initiate_chat(manager, message="Write about AI")
```

---

## Exercises

1. Create code review team
2. Build content pipeline
3. Implement debate team

---

## Next Lab

[Lab 6: Human-in-the-Loop](../Lab6/README.md)
