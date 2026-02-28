# Lab 3: Two-Agent Conversations

## Objectives

- Understand UserProxyAgent
- Set up two-agent conversations
- Build sequential chat workflows
- Create multi-step pipelines

---

## Key Concepts

### UserProxyAgent

Represents the user in conversations:
- `human_input_mode="NEVER"` - Auto-reply (no human input)
- `human_input_mode="ALWAYS"` - Always ask human
- `human_input_mode="TERMINATE"` - Ask at end

### Starting a Chat

```python
user_proxy.initiate_chat(assistant, message="Hello!")
```

---

## Examples

### Example 1: Simple Conversation

```python
from autogen import AssistantAgent, UserProxyAgent

assistant = AssistantAgent(name="assistant", llm_config={"config_list": config_list})
user_proxy = UserProxyAgent(name="user", human_input_mode="NEVER")

user_proxy.initiate_chat(assistant, message="Write a haiku")
```

### Example 2: Code Writer + Reviewer

```python
writer = AssistantAgent(name="writer", system_message="Write Python code.", llm_config={"config_list": config_list})
reviewer = AssistantAgent(name="reviewer", system_message="Review code for bugs.", llm_config={"config_list": config_list})

user_proxy.initiate_chat(writer, message="Write a function to reverse a string")
code = writer.last_message()["content"]
user_proxy.initiate_chat(reviewer, message=f"Review this: {code}")
```

---

## Exercises

1. Create translation pipeline (EN→FR→ES)
2. Build research workflow (Topic→Research→Summarize)
3. Create customer support flow (Triage→Resolve)

---

## Next Lab

[Lab 4: Tools & Functions](../Lab4/README.md)
