# Lab 2: Single Agent Fundamentals

## Objectives

- Create AssistantAgent instances
- Configure system messages for custom behavior
- Set LLM options (temperature, max_tokens)
- Send and receive messages
- Build different agent personas

---

## Key Concepts

### What is an AssistantAgent?

The `AssistantAgent` is the core AI agent in AutoGen. It's powered by an LLM and can:
- Understand and generate text
- Make decisions
- Call tools (covered in Lab 4)
- Maintain conversation context

### Creating an Agent

```python
from autogen import AssistantAgent

agent = AssistantAgent(
    name="my_agent",
    llm_config={"config_list": config_list}
)
```

### Configuration Structure

```python
config_list = [
    {
        "model": "deepseek-chat",
        "base_url": "https://api.deepseek.com/v1",
        "api_key": "your-api-key"
    }
]

agent = AssistantAgent(
    name="assistant",
    llm_config={
        "config_list": config_list,
        "temperature": 0.7,
        "max_tokens": 1000,
    }
)
```

---

## Part 1: Basic Agent

### Example: Hello World Agent

```python
"""Basic agent example."""
from autogen import AssistantAgent

config_list = [{
    "model": "deepseek-chat",
    "base_url": "https://api.deepseek.com/v1",
    "api_key": "your-key"
}]

assistant = AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list}
)

response = assistant.generate_reply(
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response)
```

---

## Part 2: Custom System Messages

### Example: Persona Agent

```python
"""Agent with custom persona."""
from autogen import AssistantAgent

# Create agent with specific persona
pirate_agent = AssistantAgent(
    name="pirate",
    system_message="""You are a pirate captain!
    Speak like a pirate using 'arrr' and 'yer'.
    Share tales of treasure and adventure.""",
    llm_config={"config_list": config_list}
)

response = pirate_agent.generate_reply(
    messages=[{"role": "user", "content": "Tell me about yourself"}]
)
print(response)
```

### Common Personas

1. **Coding Expert**
```python
system_message="""You are an expert Python developer.
- Write clean, readable code
- Include error handling
- Follow PEP 8"""
```

2. **Teacher**
```python
system_message="""You are a patient teacher.
- Explain concepts clearly
- Use examples
- Ask clarifying questions"""
```

3. **Professional Writer**
```python
system_message="""You are a professional writer.
- Write clear, engaging content
- Use proper grammar
- Structure your writing logically"""
```

---

## Part 3: LLM Options

### Temperature

Controls randomness:
- **0.0**: Deterministic, same output every time
- **0.5**: Somewhat focused
- **1.0**: Balanced
- **2.0**: Very creative/random

```python
# Focused, precise agent
precise_agent = AssistantAgent(
    name="precise",
    llm_config={
        "config_list": config_list,
        "temperature": 0.2
    }
)

# Creative agent
creative_agent = AssistantAgent(
    name="creative",
    llm_config={
        "config_list": config_list,
        "temperature": 1.5
    }
)
```

### max_tokens

Limits response length:
```python
short_agent = AssistantAgent(
    name="short",
    llm_config={
        "config_list": config_list,
        "max_tokens": 50  # Very short responses
    }
)
```

---

## Part 4: Complete Examples

### Example 1: Q&A Agent

```python
"""Q&A Agent with custom system message."""
from autogen import AssistantAgent

qa_agent = AssistantAgent(
    name="qa_assistant",
    system_message="""You are a helpful Q&A assistant.
    
Guidelines:
1. Answer questions clearly and accurately
2. If you don't know, say so
3. Provide examples when helpful
4. Keep answers concise but complete""",
    llm_config={"config_list": config_list}
)

questions = [
    "What is Python?",
    "How do lists work in Python?",
    "What is machine learning?"
]

for q in questions:
    response = qa_agent.generate_reply(
        messages=[{"role": "user", "content": q}]
    )
    print(f"Q: {q}")
    print(f"A: {response}\n")
```

### Example 2: Chain of Thought Reasoning

```python
"""Agent that shows reasoning steps."""
from autogen import AssistantAgent

cot_agent = AssistantAgent(
    name="cot_agent",
    system_message="""Solve problems step by step:
1. Understand the problem
2. Break into steps
3. Solve each step
4. Combine results
5. Verify answer
Show your thinking process.""",
    llm_config={"config_list": config_list}
)

problem = "If a train travels 60 mph, how far in 45 minutes?"

response = cot_agent.generate_reply(
    messages=[{"role": "user", "content": problem}]
)
print(response)
```

---

## Exercises

### Exercise 2.1: Create a Translator Agent
Create an agent that translates text to French.

**Solution**:
```python
translator = AssistantAgent(
    name="translator",
    system_message="""Translate English to French.
    Only output the translation, nothing else.
    Be idiomatic, not literal.""",
    llm_config={"config_list": config_list}
)

response = translator.generate_reply(
    messages=[{"role": "user", "content": "Hello, how are you?"}]
)
```

### Exercise 2.2: Temperature Comparison
Compare responses at different temperatures.

**Solution**:
```python
for temp in [0, 0.5, 1, 1.5, 2]:
    agent = AssistantAgent(
        name=f"agent_{temp}",
        llm_config={"config_list": config_list, "temperature": temp}
    )
    response = agent.generate_reply(
        messages=[{"role": "user", "content": "Write a short story opening"}]
    )
    print(f"\n=== Temperature {temp} ===")
    print(response[:200])
```

### Exercise 2.3: Conversation Memory
Demonstrate that agents remember context.

**Solution**:
```python
assistant = AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list}
)

# First message - set context
messages = [{"role": "user", "content": "My favorite food is pizza."}]
assistant.generate_reply(messages=messages)

# Second message - should remember
messages.append({"role": "assistant", "content": assistant.last_message()["content"]})
messages.append({"role": "user", "content": "What's my favorite food?"})
response = assistant.generate_reply(messages=messages)
print(response)
```

---

## Common Issues

### Response is Empty
- Check API key is valid
- Try increasing max_tokens
- Check model name is correct

### Agent Ignores System Message
- Make system message more explicit
- Add examples to the system message

### Responses Too Long/Short
- Adjust max_tokens parameter
- Modify system message to specify desired length

---

## Summary

You learned to:
- ✓ Create AssistantAgent instances
- ✓ Configure system messages
- ✓ Set LLM options (temperature, max_tokens)
- ✓ Send and receive messages
- ✓ Build custom agent personas

---

## Next Lab

[Lab 3: Two-Agent Conversations](../Lab3/README.md)
