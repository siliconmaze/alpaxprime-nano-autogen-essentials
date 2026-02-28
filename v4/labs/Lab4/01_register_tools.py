"""
Lab 4: Tools & Function Calling
=================================

This lab covers registering and using custom tools with AutoGen agents.

Key Concepts:
- register_for_execution: Make function callable by agent
- register_for_llm: Let LLM know about function
- ToolNode: Executes tools
- Function schemas: JSON descriptions of tools

Run with:
    python 01_register_tools.py
"""

import os
import json
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent

load_dotenv()

print("=" * 60)
print("Lab 4: Tools & Function Calling")
print("=" * 60)

api_key = os.getenv("DEEPSEEK_API_KEY", "")
if not api_key:
    api_key = "ollama"
    model = "qwen2.5-coder:7b"
    base_url = "http://localhost:11434/v1"
else:
    model = "deepseek-chat"
    base_url = "https://api.deepseek.com/v1"

config_list = [{"model": model, "base_url": base_url, "api_key": api_key}]

# ============================================================================
# DEFINE CUSTOM TOOLS
# ============================================================================

def get_weather(location: str) -> str:
    """
    Get weather for a location.
    
    Args:
        location: City name (e.g., "Tokyo", "London")
    
    Returns:
        Weather description
    """
    # Simulated weather data
    weather_db = {
        "tokyo": "72°F, partly cloudy",
        "london": "55°F, rainy",
        "new york": "65°F, sunny",
        "san francisco": "62°F, foggy",
        "paris": "60°F, clear",
    }
    
    location_lower = location.lower()
    if location_lower in weather_db:
        return f"Weather in {location.title()}: {weather_db[location_lower]}"
    return f"Weather data not available for {location}"


def calculate(expression: str) -> str:
    """
    Calculate a mathematical expression.
    
    Args:
        expression: Math expression (e.g., "2+2", "sqrt(16)")
    
    Returns:
        Result
    """
    try:
        # WARNING: eval is dangerous in production!
        # Use a proper math parser in production
        allowed = set("0123456789+-*/.() ")
        if all(c in allowed for c in expression):
            result = eval(expression)
            return f"{expression} = {result}"
        return "Invalid expression"
    except Exception as e:
        return f"Error: {str(e)}"


def get_time(city: str) -> str:
    """
    Get current time for a city.
    
    Args:
        city: City name
    
    Returns:
        Current time
    """
    # Simulated times
    times = {
        "tokyo": "9:30 PM",
        "london": "1:30 PM",
        "new york": "8:30 AM",
        "san francisco": "5:30 AM",
        "paris": "2:30 PM",
    }
    
    city_lower = city.lower()
    if city_lower in times:
        return f"Time in {city.title()}: {times[city_lower]}"
    return f"Unknown city: {city}"

# ============================================================================
# REGISTER TOOLS WITH AGENT
# ============================================================================

print("\n[1] Creating agent with tools...")

assistant = AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list}
)

# Register tools
assistant.register_for_execution()(get_weather)
assistant.register_for_execution()(calculate)
assistant.register_for_execution()(get_time)

print(f"    Registered tools: get_weather, calculate, get_time")

# ============================================================================
# TEST TOOL CALLING
# ============================================================================

print("\n[2] Testing tool calls...")

user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER"
)

# Test weather
print("\n    [Weather Tool]")
user_proxy.initiate_chat(
    assistant,
    message="What's the weather in Tokyo?"
)

# Test calculator
print("\n    [Calculator Tool]")
user_proxy.initiate_chat(
    assistant,
    message="Calculate 15 * 8 + 3"
)

# Test time
print("\n    [Time Tool]")
user_proxy.initiate_chat(
    assistant,
    message="What time is it in London?"
)

print("\n" + "=" * 60)
print("✓ Tools & Function Calling Complete!")
print("=" * 60)
