"""Lab 4 - Register Tools"""
import sys
sys.path.insert(0, '../../..')
from config import get_ollama_config
from autogen import AssistantAgent, UserProxyAgent

def get_weather(city: str) -> str:
    """Get weather for a city"""
    return f"Weather in {city}: 72°F, sunny"

assistant = AssistantAgent("weather_bot", llm_config={
    "config_list": get_ollama_config(),
    "tools": [{"function": get_weather, "description": "Get weather info"}]
})

user = UserProxyAgent("user", human_input_mode="NEVER")
user.initiate_chat(assistant, message="What's the weather in Paris?")
