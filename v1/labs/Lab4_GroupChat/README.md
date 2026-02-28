# Lab 4: GroupChat - Multiple Agents Working Together

## Objective
Learn to orchestrate multiple agents in a group conversation using GroupChat.

## Estimated Time
30 minutes

---

## Background

GroupChat enables multiple agents to collaborate in a single conversation. AutoGen handles:
- Speaker selection
- Message routing
- Conversation flow control

---

## Step 1: Create a Simple GroupChat

Create `groupchat_example.py`:

```python
"""Lab 4: GroupChat Multiple Agents"""
import os
from dotenv import load_dotenv
import autogen
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

config_list = [{"model": "gpt-4", "api_key": api_key}]

# Create multiple specialized agents
researcher = AssistantAgent(
    name="researcher",
    llm_config={"config_list": config_list},
    system_message="You are a research specialist. Find accurate information and cite sources."
)

writer = AssistantAgent(
    name="writer",
    llm_config={"config_list": config_list},
    system_message="You are a technical writer. Create clear, well-structured content."
)

editor = AssistantAgent(
    name="editor",
    llm_config={"config_list": config_list},
    system_message="You are an editor. Review content for accuracy, clarity, and grammar."
)

# Create UserProxyAgent for initiating
user_proxy = UserProxyAgent(
    name="user",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10
)

# Create GroupChat
groupchat = GroupChat(
    agents=[user_proxy, researcher, writer, editor],
    messages=[],
    max_round=10
)

# Create manager
manager = GroupChatManager(
    groupchat=groupchat,
    llm_config={"config_list": config_list}
)

# Start group conversation
user_proxy.initiate_chat(
    manager,
    message="""Create a short article about Artificial Intelligence.
    Have the researcher gather info, the writer create the content,
    and the editor review it."""
)
```

---

## Step 2: Run the GroupChat

```bash
python groupchat_example.py
```

---

## Step 3: Custom Speaker Selection

Control which agent speaks next:

```python
"""Lab 4b: Custom Speaker Selection"""
from autogen import GroupChat

# Speaker selection modes
groupchat = GroupChat(
    agents=[agent1, agent2, agent3],
    messages=[],
    max_round=15,
    
    # Speaker selection options:
    speaker_selection_method="round_robin"  # or "auto" or custom function
    
    # Allow agent to select next speaker?
    allow_repeat_speaker=True  # or False
)

# Custom speaker selection function
def custom_speaker_selection(last_speaker, agents, messages):
    """
    Custom logic to select next speaker.
    
    Args:
        last_speaker: The agent that just spoke
        agents: List of all agents
        messages: Conversation history
    
    Returns:
        The next agent to speak
    """
    # Example: alternate between agents
    last_idx = agents.index(last_speaker)
    next_idx = (last_idx + 1) % len(agents)
    return agents[next_idx]

groupchat = GroupChat(
    agents=[researcher, writer, editor],
    messages=[],
    speaker_selection_method=custom_speaker_selection
)
```

---

## Step 4: Nested Chats in GroupChat

Agents can have sub-conversations:

```python
"""Lab 4c: Nested Chats"""
# Agent can initiate a separate conversation
writer.initiate_chat(
    researcher,
    message="Can you research the latest trends in LLM fine-tuning?"
)
# Writer continues with main group after this completes
```

---

## Key Concepts

### GroupChat Parameters

| Parameter | Description |
|-----------|-------------|
| `agents` | List of agents in the group |
| `messages` | Initial messages list |
| `max_round` | Maximum conversation rounds |
| `speaker_selection_method` | How to pick next speaker |
| `allow_repeat_speaker` | Allow same agent twice |

### Speaker Selection Methods

- `"round_robin"` - Each agent speaks in turn
- `"auto"` - LLM decides who speaks next
- Custom function - Your own logic

### GroupChatManager

The manager orchestrates the conversation:
```python
manager = GroupChatManager(
    groupchat=groupchat,
    llm_config={"config_list": config_list}
)
```

---

## Challenge Exercise

Create a "Software Development Team" groupchat:
1. **Product Manager** - Defines requirements
2. **Developer** - Writes code
3. **Code Reviewer** - Reviews code
4. **Tester** - Creates tests

Have them collaborate to build a simple REST API.

---

## What You Learned

✓ Creating GroupChat with multiple agents
✓ Configuring speaker selection
✓ Managing group conversations
✓ Nested chats between agents

---

## Next Step

Proceed to **Lab 5: Human-in-the-Loop** to add human oversight to your agents!
