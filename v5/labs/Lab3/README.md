# Lab 3: Two-Agent Conversations

## Objectives
- Create UserProxyAgent for user input
- Set up two-agent conversations
- Implement sequential message passing
- Handle multi-turn dialogues

**Provider**: Ollama (default)

---

## Concept: Two-Agent Architecture

```
┌──────────────┐    Messages    ┌──────────────┐
│ UserProxy    │ ──────────────▶│ Assistant    │
│   Agent      │◀────────────── │   Agent      │
└──────────────┘                └──────────────┘
     (you)                          (AI)
```

The UserProxyAgent represents the user and can:
- Send messages to AssistantAgent
- Execute code (in later labs)
- Receive and process responses

---

## Sample Code

### 1. Basic Two-Agent Chat
```python
from config import get_ollama_config
from autogen import AssistantAgent, UserProxyAgent

# Create agents
assistant = AssistantAgent(
    name="assistant",
    llm_config={"config_list": get_ollama_config()}
)

user_proxy = UserProxyAgent(
    name="user",
    human_input_mode="NEVER"  # Fully automated
)

# Start conversation
user_proxy.initiate_chat(
    assistant,
    message="Explain what AutoGen is in one sentence."
)
```

### 2. Sequential Chat
```python
"""Multi-turn conversation"""
from config import get_ollama_config
from autogen import AssistantAgent, UserProxyAgent

assistant = AssistantAgent(
    name="helper",
    llm_config={"config_list": get_ollama_config()}
)

user = UserProxyAgent(name="user", human_input_mode="NEVER")

# First message
user.initiate_chat(assistant, message="What is 5 + 5?")

# Follow-up (continues conversation)
user.send(
    assistant,
    message="Now multiply that by 3"
)
```

### 3. Two-Agent Research
```python
"""Two agents working together"""
from config import get_ollama_config
from autogen import AssistantAgent, UserProxyAgent

researcher = AssistantAgent(
    name="researcher",
    system_message="You research topics thoroughly. Provide facts and sources.",
    llm_config={"config_list": get_ollama_config()}
)

summarizer = AssistantAgent(
    name="summarizer", 
    system_message="You summarize long text into brief key points.",
    llm_config={"config_list": get_ollama_config()}
)

user = UserProxyAgent(name="user", human_input_mode="NEVER")

# Research task
user.initiate_chat(researcher, message="What is quantum computing?")

# Summarize result
user.send(summarizer, message="Summarize the previous response in 3 bullet points")
```

---

## Exercises

### Ex 3.1: Q&A Bot
Create a two-agent conversation where one agent answers questions.

### Ex 3.2: Editor-Rewriter
Create an editor that reviews text and a rewriter that makes changes.

### Ex 3.3: Debate
Create two agents with opposing views debating a topic.

---

## Lab 3 Complete ✅
Next: [Lab 4: Tools & Function Calling](../Lab4/README.md)
