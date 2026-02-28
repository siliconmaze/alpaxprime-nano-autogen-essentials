# Lab 3: Tools and Function Calling

## Objective
Learn to define and use custom functions/tools that agents can call during conversations.

## Estimated Time
25 minutes

---

## Background

Tools extend agents' capabilities beyond text generation. Agents can:
- Execute Python code
- Call external APIs
- Perform calculations
- Access databases
- And more!

---

## Step 1: Define a Custom Function

Create `tools_example.py`:

```python
"""Lab 3: Using Tools with AutoGen"""
import os
from dotenv import load_dotenv
import autogen
from autogen import AssistantAgent, UserProxyAgent

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Define a custom function
def get_weather(location: str, unit: str = "celsius") -> str:
    """
    Get weather information for a location.
    
    Args:
        location: City name
        unit: Temperature unit (celsius or fahrenheit)
    
    Returns:
        Weather information string
    """
    # Simulated weather data (in real app, call a weather API)
    weather_data = {
        "new york": {"celsius": 18, "fahrenheit": 64, "condition": "Partly cloudy"},
        "london": {"celsius": 12, "fahrenheit": 54, "condition": "Rainy"},
        "tokyo": {"celsius": 22, "fahrenheit": 72, "condition": "Sunny"},
        "san francisco": {"celsius": 15, "fahrenheit": 59, "condition": "Foggy"},
    }
    
    location_lower = location.lower()
    if location_lower in weather_data:
        data = weather_data[location_lower]
        temp = data.get(unit, data["celsius"])
        return f"Weather in {location.title()}: {temp}° {unit.title()}, {data['condition']}"
    
    return f"Weather data not available for {location}"

# Register the function with AutoGen
autogen.agentchat.register_function(
    get_weather,
    name="get_weather",
    description="Get current weather information for a city"
)

# Configuration
config_list = [
    {
        "model": "gpt-4",
        "api_key": api_key
    }
]

# Create agent with function definitions
assistant = AssistantAgent(
    name="weather_assistant",
    llm_config={
        "config_list": config_list,
        "functions": [
            {
                "name": "get_weather",
                "description": "Get current weather information for a city",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "City name"
                        },
                        "unit": {
                            "type": "string",
                            "enum": ["celsius", "fahrenheit"],
                            "description": "Temperature unit"
                        }
                    },
                    "required": ["location"]
                }
            }
        ]
    }
)

# Create user proxy
user_proxy = UserProxyAgent(
    name="user",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=5
)

# Start conversation
user_proxy.initiate_chat(
    assistant,
    message="What's the weather like in New York and London? Please use Celsius."
)
```

---

## Step 2: Run the Tool Example

```bash
python tools_example.py
```

**Expected Output:**
```
user (to weather_assistant):

What's the weather like in New York and London? Please use Celsius?

weather_assistant (to user):

I'll check the weather for both cities using the get_weather function.
***** Suggested function call: get_weather *****
Call id: call_123
get_weather(location="New York", unit="celsius")
**************************************************

new york: 18° Celsius, Partly cloudy

***** Suggested function call: get_weather *****
Call id: call_124
get_weather(location="London", unit="celsius")
**************************************************

london: 12° Celsius, Rainy

The weather in New York is 18°C and partly cloudy, while London is 12°C with rain.
```

---

## Step 3: Code Execution Tool

AutoGen can also execute Python code directly:

```python
"""Lab 3b: Code Execution"""
user_proxy = UserProxyAgent(
    name="code_executor",
    human_input_mode="NEVER",
    code_execution_config={
        "work_dir": "code_output",
        "use_docker": False,  # Set True for Docker isolation
        "timeout": 120
    }
)

# The assistant can now request code execution
assistant = AssistantAgent(
    name="data_analyst",
    llm_config={"config_list": config_list}
)

user_proxy.initiate_chat(
    assistant,
    message="""Analyze this data and create a summary:
    
    sales_data = [
        {"month": "Jan", "revenue": 15000, "expenses": 8000},
        {"month": "Feb", "revenue": 18000, "expenses": 9500},
        {"month": "Mar", "revenue": 22000, "expenses": 10000},
    ]
    
    Calculate:
    1. Total revenue
    2. Total expenses
    3. Profit margin for each month"""
)
```

---

## Key Concepts

### Function Registration

```python
autogen.agentchat.register_function(
    my_function,
    name="function_name",
    description="What the function does"
)
```

### Function Schema

```python
"functions": [
    {
        "name": "function_name",
        "description": "What it does",
        "parameters": {
            "type": "object",
            "properties": {
                "param1": {"type": "string", "description": "..."},
                "param2": {"type": "integer", "description": "..."}
            },
            "required": ["param1"]
        }
    }
]
```

### Code Execution Config

```python
code_execution_config={
    "work_dir": "output_dir",     # Working directory
    "use_docker": True,          # Docker isolation
    "timeout": 120,              # Seconds
    "last_n_messages": 2,        # Messages to include
}
```

---

## Challenge Exercise

Create a multi-function agent that:
1. Has a `calculate` function for math operations
2. Has a `get_stock_price` function (simulated)
3. Can answer: "If I own 100 shares of AAPL at $150, what's my total investment?"

---

## What You Learned

✓ Defining custom functions
✓ Registering functions with AutoGen
✓ Function calling in conversations
✓ Code execution capabilities

---

## Next Step

Proceed to **Lab 4: GroupChat** to orchestrate multiple agents working together!
