# Microsoft AutoGen: Complete Labs Guide
## Build Multi-Agent AI Systems - Hands-On Course

---

# Lab 1: Hello AutoGen - Setting Up Your Environment

## Objective
Set up your development environment and verify AutoGen is working correctly.

## Prerequisites
- Python 3.8+
- OpenAI API Key

## Step 1: Install AutoGen

```bash
python -m venv autogen-env
source autogen-env/bin/activate
pip install pyautogen
pip install openai python-dotenv
```

## Step 2: Configure Your API Key

Create a `.env` file:
```bash
OPENAI_API_KEY=your-openai-api-key-here
```

## Step 3: Verify Your Setup

```python
"""Lab 1: Verify AutoGen Installation"""
import os
from dotenv import load_dotenv
import autogen

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("⚠️ WARNING: OPENAI_API_KEY not found")
    exit(1)

config_list = [{"model": "gpt-4", "api_key": api_key}]

assistant = autogen.AssistantAgent(
    name="test_agent",
    llm_config={"config_list": config_list}
)

print("✓ AutoGen version:", autogen.__version__)
print("✓ AssistantAgent created successfully!")
print("🎉 All checks passed!")
```

---

# Lab 2: Agent Conversations - Your First Multi-Agent System

## Objective
Build a simple two-agent conversation system.

## Step 1: Create the Basic Conversation

```python
"""Lab 2: Basic Two-Agent Conversation"""
import os
from dotenv import load_dotenv
import autogen
from autogen import AssistantAgent, UserProxyAgent

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

config_list = [{"model": "gpt-4", "api_key": api_key}]

# Create the AssistantAgent
assistant = AssistantAgent(
    name="code_assistant",
    llm_config={"config_list": config_list},
    system_message="You are a Python expert. Write clean, well-documented code."
)

# Create the UserProxyAgent
user_proxy = UserProxyAgent(
    name="human_user",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    code_execution_config={"work_dir": "code_output", "use_docker": False}
)

# Start the conversation
user_proxy.initiate_chat(
    assistant,
    message="Create a Python class for managing inventory with add, remove, and list operations."
)
```

## Key Concepts

### human_input_mode Options
| Mode | Behavior |
|------|----------|
| "NEVER" | Fully automated |
| "ALWAYS" | Always ask for input |
| "TERMINATE" | Ask at termination |

---

# Lab 3: Tools and Function Calling

## Objective
Learn to define and use custom functions/tools.

## Step 1: Define a Custom Function

```python
"""Lab 3: Using Tools with AutoGen"""
import autogen

def get_weather(location: str, unit: str = "celsius") -> str:
    """Get weather for a location."""
    weather_data = {
        "new york": {"celsius": 18, "condition": "Partly cloudy"},
        "london": {"celsius": 12, "condition": "Rainy"},
    }
    location_lower = location.lower()
    if location_lower in weather_data:
        data = weather_data[location_lower]
        return f"{location.title()}: {data['celsius']}°C, {data['condition']}"
    return f"Weather not available for {location}"

# Register function
autogen.agentchat.register_function(
    get_weather,
    name="get_weather",
    description="Get current weather for a city"
)

# Create agent with function
assistant = AssistantAgent(
    name="weather_assistant",
    llm_config={
        "config_list": config_list,
        "functions": [{
            "name": "get_weather",
            "description": "Get weather for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "City name"},
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
                },
                "required": ["location"]
            }
        }]
    }
)
```

---

# Lab 4: GroupChat - Multiple Agents Working Together

## Objective
Orchestrate multiple agents in a group conversation.

```python
"""Lab 4: GroupChat"""
from autogen import GroupChat, GroupChatManager

# Create agents
researcher = AssistantAgent(name="researcher", llm_config={"config_list": config_list})
writer = AssistantAgent(name="writer", llm_config={"config_list": config_list})
editor = AssistantAgent(name="editor", llm_config={"config_list": config_list})
user_proxy = UserProxyAgent(name="user", human_input_mode="NEVER")

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
    message="Create an article about AI. Researcher finds info, Writer creates content, Editor reviews."
)
```

---

# Lab 5: Human-in-the-Loop Patterns

## Objective
Incorporate human oversight into agents.

## Step 1: TERMINATE Mode

```python
"""Lab 5: Human-in-the-Loop"""
assistant = AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list},
    system_message="When done, say 'FINISHED'."
)

user_proxy = UserProxyAgent(
    name="user",
    human_input_mode="TERMINATE",  # Ask for approval to end
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: "FINISHED" in x.get("content", "")
)

user_proxy.initiate_chat(assistant, message="Write a haiku about coding.")
```

## Human Input Modes
- `NEVER` - Fully automated
- `ALWAYS` - Always ask for input  
- `TERMINATE` - Ask when agent signals done

---

# Lab 6: Real-World Applications

## Objective
Build production-ready multi-agent systems.

## Code Review System

```python
"""Lab 6: Code Review System"""
reviewer = AssistantAgent(
    name="reviewer",
    llm_config={"config_list": config_list},
    system_message="Review code for bugs, security issues, and quality."
)

security_expert = AssistantAgent(
    name="security_expert",
    llm_config={"config_list": config_list},
    system_message="Review for security vulnerabilities."
)

# Group chat for code review
groupchat = GroupChat(agents=[submitter, reviewer, security_expert])
manager = GroupChatManager(groupchat=groupchat, llm_config={"config_list": config_list})
```

---

# Lab 7: Production Patterns

## Error Handling

```python
"""Lab 7: Error Handling"""
try:
    user_proxy.initiate_chat(assistant, message="Hello!")
except Exception as e:
    print(f"Error: {e}")
    # Handle gracefully
```

## State Management

```python
class ConversationState:
    def __init__(self):
        self.conversations = {}
        
    def save(self, conv_id, messages):
        self.conversations[conv_id] = messages
        
    def export(self, filepath):
        import json
        with open(filepath, 'w') as f:
            json.dump(self.conversations, f)
```

---

# Quick Reference

## Basic Agents
```python
from autogen import AssistantAgent, UserProxyAgent

assistant = AssistantAgent(name="assistant", llm_config={"config_list": config_list})
user_proxy = UserProxyAgent(name="user", human_input_mode="NEVER")
```

## Start Conversation
```python
user_proxy.initiate_chat(assistant, message="Your message")
```

## GroupChat
```python
groupchat = GroupChat(agents=[agent1, agent2])
manager = GroupChatManager(groupchat=groupchat, llm_config={"config_list": config_list})
```

## Human Input Modes
- `NEVER` - Fully automated
- `ALWAYS` - Always ask human
- `TERMINATE` - Ask at termination

---

*Course by Steve Robinson - Alpaca Mango*
