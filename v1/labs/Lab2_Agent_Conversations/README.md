# Lab 2: Agent Conversations - Your First Multi-Agent System

## Objective
Build a simple two-agent conversation system where a UserProxyAgent and AssistantAgent communicate to solve a task.

## Estimated Time
20 minutes

---

## Background

AutoGen's core strength is multi-agent communication. In this lab, you'll create:
- **AssistantAgent**: An AI-powered agent that generates responses using an LLM
- **UserProxyAgent**: A proxy for the human user that can execute code and continue conversations

---

## Step 1: Create the Basic Conversation

Create `basic_conversation.py`:

```python
"""Lab 2: Basic Two-Agent Conversation"""
import os
from dotenv import load_dotenv
import autogen
from autogen import AssistantAgent, UserProxyAgent

# Load environment
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Configuration
config_list = [
    {
        "model": "gpt-4",
        "api_key": api_key
    }
]

# Create the AssistantAgent
assistant = AssistantAgent(
    name="code_assistant",
    llm_config={"config_list": config_list},
    system_message="""You are a Python expert. Your role is to:
1. Write clean, well-documented code
2. Explain your code clearly
3. Provide complete, runnable solutions"""
)

# Create the UserProxyAgent
user_proxy = UserProxyAgent(
    name="human_user",
    human_input_mode="NEVER",  # NEVER = fully automated
    max_consecutive_auto_reply=10,
    code_execution_config={
        "work_dir": "code_output",
        "use_docker": False
    }
)

# Start the conversation
print("="*60)
print("Starting conversation with Code Assistant...")
print("="*60)

user_proxy.initiate_chat(
    assistant,
    message="""Create a Python class for managing a simple 
inventory system with the following requirements:
1. Add items to inventory
2. Remove items from inventory  
3. List all items
4. Check if an item exists
5. Get the total item count"""
)
```

---

## Step 2: Run the Conversation

```bash
python basic_conversation.py
```

**You'll see output like:**
```
============================================================
Starting conversation with Code Assistant...
============================================================
human_user (to code_assistant):

Create a Python class for managing a simple...

code_assistant (to human_user):

Here's a complete implementation of the Inventory class:

```python
class Inventory:
    def __init__(self):
        self._items = {}
    
    def add(self, item_name, quantity=1):
        if item_name in self._items:
            self._items[item_name] += quantity
        else:
            self._items[item_name] = quantity
        return f"Added {quantity} of {item_name}"
    
    # ... more methods
```

[human_user]: 

I've created a complete inventory management system...

[and so on...]
```

---

## Understanding the Flow

```
┌─────────────┐                         ┌─────────────────┐
│  UserProxy  │─── message ──────────►│                 │
│   Agent     │                        │    Assistant    │
│  (human)    │◄─── response ──────────│     Agent       │
└─────────────┘                        │   (LLM-powered) │
                                        └─────────────────┘
        │                                       │
        ▼                                       ▼
   Execute code?                        Generate response
   Continue conversation?               using LLM
```

---

## Key Concepts

### human_input_mode Options

| Mode | Behavior |
|------|----------|
| `"NEVER"` | Fully automated, no human input |
| `"ALWAYS"` | Always ask for human input |
| `"TERMINATE"` | Ask only when agent requests termination |

### code_execution_config

```python
code_execution_config={
    "work_dir": "code_output",      # Where to save/run code
    "use_docker": True,             # Run in Docker container
    "timeout": 120,                 # Execution timeout (seconds)
}
```

---

## Challenge Exercise

Modify the conversation to:
1. Ask the assistant to create a **unit test** for the inventory class
2. Have the UserProxyAgent **execute** the tests
3. Report the results back to the assistant

---

## What You Learned

✓ Creating an AssistantAgent
✓ Creating a UserProxyAgent
✓ Initiating conversations between agents
✓ Configuring human input modes
✓ Code execution in conversations

---

## Next Step

Proceed to **Lab 3: Tools & Functions** to add custom functions to your agents!
