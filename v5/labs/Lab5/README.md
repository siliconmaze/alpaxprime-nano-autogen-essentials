# Lab 5: Group Chat & Orchestration

## Objectives
- Create GroupChat with multiple agents
- Configure speaker selection
- Implement custom selection strategies
- Manage complex multi-agent workflows

**Provider**: Ollama (default)

---

## Concept: Group Chat

GroupChat enables multiple agents to collaborate:
- Sequential or parallel message passing
- Custom speaker selection
- Flexible conversation flow

```
┌─────────────────────────────────────┐
│           GroupChat                  │
│  ┌─────────┐ ┌─────────┐ ┌────────┐  │
│  │ Agent 1 │ │ Agent 2 │ │Agent 3 │  │
│  └────┬────┘ └────┬────┘ └───┬────┘  │
│       └──────────┼──────────┘        │
│            ┌─────▼─────┐              │
│            │  Speaker  │              │
│            │ Selection │              │
│            └───────────┘              │
└─────────────────────────────────────┘
```

---

## Sample Code

### 1. Basic Group Chat
```python
from config import get_ollama_config
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager

# Create multiple agents
writer = AssistantAgent(
    name="writer",
    system_message="You write creative content.",
    llm_config={"config_list": get_ollama_config()}
)

editor = AssistantAgent(
    name="editor",
    system_message="You edit and improve content.",
    llm_config={"config_list": get_ollama_config()}
)

# Create group chat
groupchat = GroupChat(
    agents=[writer, editor],
    messages=[],
    max_round=5
)

# Create manager
manager = GroupChatManager(
    groupchat=groupchat,
    llm_config={"config_list": get_ollama_config()}
)

# Start
user = UserProxyAgent("user", human_input_mode="NEVER")
user.initiate_chat(manager, message="Write a short story about a robot")
```

### 2. Custom Speaker Selection
```python
"""Custom selection logic"""
from config import get_ollama_config
from autogen import AssistantAgent, GroupChat, GroupChatManager

researcher = AssistantAgent("researcher", llm_config={"config_list": get_ollama_config()})
analyst = AssistantAgent("analyst", llm_config={"config_list": get_ollama_config()})
presenter = AssistantAgent("presenter", llm_config={"config_list": get_ollama_config()})

def select_speaker(last_speaker, last_message):
    """Custom selection: researcher → analyst → presenter"""
    if last_speaker is None or last_speaker.name == "presenter":
        return researcher
    elif last_speaker.name == "researcher":
        return analyst
    return presenter

groupchat = GroupChat(
    agents=[researcher, analyst, presenter],
    messages=[],
    speaker_selection_method=select_speaker,
    max_round=3
)

manager = GroupChatManager(groupchat=groupchat, llm_config={"config_list": get_ollama_config()})

user = UserProxyAgent("user", human_input_mode="NEVER")
user.initiate_chat(manager, message="Research AI trends, analyze, then present")
```

### 3. Sequential Pipeline
```python
"""Pipeline pattern"""
from config import get_ollama_config
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager

collector = AssistantAgent("collector", llm_config={"config_list": get_ollama_config()})
processor = AssistantAgent("processor", llm_config={"config_list": get_ollama_config()})
formatter = AssistantAgent("formatter", llm_config={"config_list": get_ollama_config()})

groupchat = GroupChat(
    agents=[collector, processor, formatter],
    messages=[],
    max_round=3
)

manager = GroupChatManager(groupchat=groupchat, llm_config={"config_list": get_ollama_config()})

user = UserProxyAgent("user", human_input_mode="NEVER")
user.initiate_chat(manager, message="Collect facts about Python, process them, format as list")
```

---

## Exercises

### Ex 5.1: Team Brainstorm
Create 3 agents: idea generator, evaluator, prioritizer.

### Ex 5.2: Review Chain
Create a code review pipeline with reviewer and fixer.

### Ex 5.3: Debate Group
Create multiple agents with different perspectives.

---

## Lab 5 Complete ✅
Next: [Lab 6: Human-in-the-Loop](../Lab6/README.md)
