# Lab 4: Tools & Function Calling

## Objectives
- Register custom tools with agents
- Create Python function tools
- Enable agents to call external APIs
- Handle tool responses

**Provider**: Ollama (default)

---

## Concept: Tools in AutoGen

Tools extend agent capabilities beyond text generation:
- Execute code
- Call APIs
- Read/write files
- Run commands

```
Agent ──(calls)──▶ Tool ──(returns)──▶ Agent
```

---

## Sample Code

### 1. Simple Function Tool
```python
from config import get_ollama_config
from autogen import AssistantAgent, UserProxyAgent

# Define a function
def get_weather(location: str) -> str:
    """Get weather for a location."""
    # In real use, call weather API
    return f"Weather in {location}: 72°F, Sunny"

# Register the tool
assistant = AssistantAgent(
    name="weather_bot",
    llm_config={
        "config_list": get_ollama_config(),
        "tools": [
            {
                "function": get_weather,
                "description": "Get current weather for a city"
            }
        ]
    }
)

user = UserProxyAgent("user", human_input_mode="NEVER")
user.initiate_chat(assistant, message="What's the weather in Tokyo?")
```

### 2. Multi-Tool Agent
```python
"""Agent with multiple tools"""
from config import get_ollama_config
from autogen import AssistantAgent, UserProxyAgent
import json

def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

def save_to_file(filename: str, content: str) -> str:
    """Save content to a file"""
    with open(filename, 'w') as f:
        f.write(content)
    return f"Saved to {filename}"

assistant = AssistantAgent("tool_agent", llm_config={
    "config_list": get_ollama_config(),
    "tools": [add, multiply, save_to_file]
})

user = UserProxyAgent("user", human_input_mode="NEVER")
user.initiate_chat(assistant, message="Calculate 5 + 3, then multiply by 10")
```

### 3. API Tool
```python
"""Call external API"""
import requests
from config import get_ollama_config
from autogen import AssistantAgent, UserProxyAgent

def get_github_info(repo: str) -> str:
    """Get GitHub repository info"""
    response = requests.get(f"https://api.github.com/repos/{repo}")
    data = response.json()
    return f"Stars: {data.get('stargazers_count', 0)}, Forks: {data.get('forks_count', 0)}"

assistant = AssistantAgent("github_bot", llm_config={
    "config_list": get_ollama_config(),
    "tools": [get_github_info]
})

user = UserProxyAgent("user", human_input_mode="NEVER")
user.initiate_chat(assistant, message="How many stars does microsoft/autogen have?")
```

---

## Exercises

### Ex 4.1: Calculator Tool
Create an agent with calculator functions.

### Ex 4.2: Search Tool
Create a search agent using a mock search function.

### Ex 4.3: File Operations
Create tools for read/write file operations.

---

## Lab 4 Complete ✅
Next: [Lab 5: Group Chat](../Lab5/README.md)
