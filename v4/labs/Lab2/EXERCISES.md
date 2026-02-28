# Lab 2: Exercises & Deep Dive

## Exercise 1: Create Agent Personas

### Task
Create agents with different personas and test them.

### Solution

```python
from autogen import AssistantAgent

# Persona 1: The Pirate
pirate = AssistantAgent(
    name="pirate",
    system_message="""You be a fearsome pirate captain! 
    Speak like a pirate usin' arrr and yer.
    Share tales of treasure and adventure on the high seas.""",
    llm_config={"config_list": config_list}
)

# Persona 2: The Shakespearean
shakespeare = AssistantAgent(
    name="shakespeare",
    system_message="""Thou art a noble bard of Elizabethan England!
    Speak in grand thees and thoues most fine.
    Weave poetry with fancy words aplenty.""",
    llm_config={"config_list": config_list}
)

# Persona 3: The Robot
robot = AssistantAgent(
    name="robot",
    system_message="""You are Robot 3000, a logical machine.
    Speak in a monotone, using numbers.
    End every response with 'PROCESSING...'""",
    llm_config={"config_list": config_list}
)

# Persona 4: The Valley Girl
valley = AssistantAgent(
    name="valley_girl",
    system_message="""You are like, totally a Valley Girl, ya know?
    Use like, like, OMG, and stuff.
    Be super enthusiastic about everything!""",
    llm_config={"config_list": config_list}
)
```

---

## Exercise 2: Temperature Experiments

### Task
Understand how temperature affects outputs.

```python
from autogen import AssistantAgent

def compare_temperatures(prompt, temps=[0, 0.5, 1, 1.5, 2]):
    """Compare responses across temperatures."""
    results = {}
    
    for temp in temps:
        agent = AssistantAgent(
            name=f"agent_{temp}",
            llm_config={
                "config_list": config_list,
                "temperature": temp
            }
        )
        
        response = agent.generate_reply(
            messages=[{"role": "user", "content": prompt}]
        )
        
        results[temp] = response
        print(f"\n=== Temperature {temp} ===")
        print(response[:200])
    
    return results

# Test with creative prompt
prompt = "Write a single sentence about a cat"
results = compare_temperatures(prompt)
```

### Expected Observations:
- **0.0**: Deterministic, same response every time
- **0.5**: Some variation, focused
- **1.0**: Balanced creativity
- **1.5**: Very creative, may be nonsensical
- **2.0**: Maximum creativity/randomness

---

## Exercise 3: Context Window Management

### Task
Understand and manage context windows.

```python
from autogen import AssistantAgent

# Create agent with custom context settings
agent = AssistantAgent(
    name="context_test",
    llm_config={
        "config_list": config_list,
        "max_tokens": 500,  # Limit response length
    }
)

# Test with long context
long_text = """
Write a detailed analysis of the following topic: 
Artificial Intelligence in Healthcare.

""" * 50  # Repeat to make it longer

response = agent.generate_reply(
    messages=[{"role": "user", "content": f"Summarize this: {long_text}"}]
)

print(f"Response length: {len(response)} characters")
print(f"Response: {response[:500]}...")
```

---

## Exercise 4: Building a Q&A Agent

### Task
Create a Q&A agent optimized for answering questions.

```python
from autogen import AssistantAgent

qa_agent = AssistantAgent(
    name="qa_assistant",
    system_message="""You are a helpful Q&A Assistant.

Your guidelines:
1. Answer questions clearly and accurately
2. If you don't know, say "I don't know" 
3. Provide sources when possible
4. Use examples to illustrate points
5. Keep answers concise but complete
6. Ask clarifying questions if needed

Format your responses:
- Direct answer first
- Supporting details
- Examples if helpful""",
    llm_config={"config_list": config_list}
)

# Test questions
questions = [
    "What is Python?",
    "How does machine learning work?",
    "What are the benefits of exercise?",
]

for q in questions:
    response = qa_agent.generate_reply(
        messages=[{"role": "user", "content": q}]
    )
    print(f"Q: {q}")
    print(f"A: {response}\n")
```

---

## Exercise 5: Chain of Thought Reasoning

### Task
Enable step-by-step reasoning.

```python
from autogen import AssistantAgent

cot_agent = AssistantAgent(
    name="cot_agent",
    system_message="""You solve problems step by step.

For each problem:
1. First, understand what is being asked
2. Break down into smaller steps
3. Solve each step explicitly
4. Combine steps to get final answer
5. Verify the answer

Show your thinking process.""",
    llm_config={"config_list": config_list}
)

# Test with math problem
problem = "If a train travels 60 miles per hour, how far will it travel in 45 minutes?"

response = cot_agent.generate_reply(
    messages=[{"role": "user", "content": problem}]
)
print(response)
```

---

## Exercise 6: Agent Memory Simulation

### Task
Simulate memory across messages.

```python
from autogen import AssistantAgent, UserProxyAgent

# Agent remembers context
assistant = AssistantAgent(
    name="memory_agent",
    system_message="""You remember all information from the conversation.
Refer back to previous messages when relevant.""",
    llm_config={"config_list": config_list}
)

user_proxy = UserProxyAgent(name="user", human_input_mode="NEVER")

# First message
user_proxy.initiate_chat(assistant, message="My favorite color is blue.")
print("Message 1 sent")

# Second message - agent should remember
user_proxy.initiate_chat(assistant, message="What's my favorite color?")
# Agent should say blue!
```

---

## Complete Example: Custom Agent Factory

```python
from autogen import AssistantAgent
import os

def create_agent(
    name: str,
    persona: str = None,
    system_message: str = None,
    temperature: float = 0.7,
    max_tokens: int = None,
    provider: str = "deepseek"
):
    """Factory function to create configured agents."""
    
    # Provider configs
    configs = {
        "ollama": {"model": "qwen2.5-coder:7b", "base_url": "http://localhost:11434/v1", "api_key": "ollama"},
        "deepseek": {"model": "deepseek-chat", "base_url": "https://api.deepseek.com/v1", "api_key": os.getenv("DEEPSEEK_API_KEY")},
        "minimax": {"model": "MiniMax-Text-01", "base_url": "https://api.minimax.io/anthropic/v1", "api_key": os.getenv("MINIMAX_API_KEY")},
    }
    
    config = configs.get(provider, configs["deepseek"])
    
    # Build system message
    if system_message is None and persona:
        system_message = f"You are {persona}."
    
    # Build llm_config
    llm_config = {
        "config_list": [config],
        "temperature": temperature,
    }
    
    if max_tokens:
        llm_config["max_tokens"] = max_tokens
    
    return AssistantAgent(name=name, system_message=system_message, llm_config=llm_config)


# Usage examples
if __name__ == "__main__":
    # Different personas
    coder = create_agent("coder", "a Python expert", temperature=0.2)
    creative = create_agent("writer", "a creative novelist", temperature=1.0)
    teacher = create_agent("teacher", "a patient tutor", temperature=0.5)
    
    print("Agents created successfully!")
```
