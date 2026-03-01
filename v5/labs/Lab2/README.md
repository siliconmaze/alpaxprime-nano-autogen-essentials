# Lab 2: Single Agent Fundamentals

## Objectives
- Create and configure AssistantAgent
- Use system messages for custom behavior
- Control LLM parameters (temperature, max_tokens)
- Handle agent responses

**Provider**: Ollama (default)

---

## Concept: What is an Agent?

An AutoGen agent is an AI assistant that:
- Receives messages
- Uses an LLM to generate responses
- Can use tools (covered in Lab 4)
- Maintains conversation context

---

## Sample Code

### 1. Basic Agent
```python
from config import get_ollama_config
from autogen import AssistantAgent

agent = AssistantAgent(
    name="assistant",
    llm_config={"config_list": get_ollama_config()}
)

response = agent.generate_reply(
    messages=[{"role": "user", "content": "What is Python?"}]
)
print(response)
```

### 2. Custom System Message
```python
from config import get_ollama_config
from autogen import AssistantAgent

agent = AssistantAgent(
    name="code_expert",
    system_message="""You are a Python expert.
    Always provide code examples.
    Keep explanations brief.""",
    llm_config={"config_list": get_ollama_config(), "temperature": 0.5}
)

response = agent.generate_reply(
    messages=[{"role": "user", "content": "How do I read a file?"}]
)
print(response)
```

### 3. Parameter Tuning
```python
"""Different temperature settings"""
from config import get_ollama_config
from autogen import AssistantAgent
import json

configs = {
    "creative": {"temperature": 1.0, "max_tokens": 200},
    "balanced": {"temperature": 0.7, "max_tokens": 150},
    "precise": {"temperature": 0.2, "max_tokens": 100}
}

for name, params in configs.items():
    agent = AssistantAgent(name=name, llm_config={
        "config_list": get_ollama_config(),
        **params
    })
    resp = agent.generate_reply(
        messages=[{"role": "user", "content": "Tell me a joke"}]
    )
    print(f"\n=== {name.upper()} ===\n{resp}")
```

---

## Exercises

### Ex 2.1: Build a Math Tutor Agent
Create an agent that explains math concepts simply.

### Ex 2.2: Build a Translator Agent
Create an agent that translates text to different languages.

### Ex 2.3: Compare Temperature Effects
Test the same prompt with temperature 0.1 vs 0.9

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Empty response | Check model is loaded in Ollama |
| Slow responses | Use smaller model (qwen2.5:3b) |
| Same output | Increase temperature |

---

## Lab 2 Complete ✅
Next: [Lab 3: Two-Agent Conversations](../Lab3/README.md)
