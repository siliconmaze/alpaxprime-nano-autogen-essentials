% AutoGen v5 Course - Complete Lab Guide
% Alpax Prime
% Version 5.0 - Ollama-First Edition

# Microsoft AutoGen: The Complete Course v5

## Building Production-Ready Multi-Agent AI Systems

---

**Version**: 5.0 (Ollama-First Edition)  
**Author**: Alpax Prime 🦙  
**Prerequisites**: Python 3.10+, Basic understanding of LLMs

---

# Lab 1: Environment Setup

## Objectives

By the end of this lab, you will be able to:
- Install and configure Python environment
- Set up Ollama (primary, no API key required)
- Configure optional cloud providers
- Create and run your first AutoGen agent

**Primary Provider**: Ollama (no API key required)

---

## Part 1: Python & Dependencies

### Install Dependencies

```bash
pip install pyautogen python-dotenv requests
```

Verify:
```bash
python -c "import autogen; print(f'AutoGen: {autogen.__version__}')"
```

---

## Part 2: Ollama Setup (No API Key Required)

### Install Ollama

**macOS/Linux:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

**Windows:**
Download from https://ollama.ai/download

### Pull a Model

```bash
ollama pull qwen2.5-coder:7b
```

### Start Server

```bash
ollama serve &
```

---

## Part 3: Configuration

### Create .env File

```bash
OLLAMA_BASE_URL=http://localhost:11434/v1
OLLAMA_MODEL=qwen2.5-coder:7b
# Optional: DEEPSEEK_API_KEY=your-key
```

---

# Lab 2: Single Agent Fundamentals

## Objectives
- Create and configure AssistantAgent
- Use system messages for custom behavior
- Control LLM parameters (temperature, max_tokens)
- Handle agent responses

**Provider**: Ollama (default)

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
agent = AssistantAgent(
    name="code_expert",
    system_message="You are a Python expert. Provide code examples.",
    llm_config={"config_list": get_ollama_config(), "temperature": 0.5}
)
```

---

# Lab 3: Two-Agent Conversations

## Objectives
- Create UserProxyAgent for user input
- Set up two-agent conversations
- Implement sequential message passing
- Handle multi-turn dialogues

**Provider**: Ollama (default)

---

## Sample Code

### Basic Two-Agent Chat
```python
from autogen import AssistantAgent, UserProxyAgent

assistant = AssistantAgent(
    name="assistant",
    llm_config={"config_list": get_ollama_config()}
)

user_proxy = UserProxyAgent(
    name="user",
    human_input_mode="NEVER"
)

user_proxy.initiate_chat(
    assistant,
    message="Explain AutoGen in one sentence."
)
```

---

# Lab 4: Tools & Function Calling

## Objectives
- Register custom tools with agents
- Create Python function tools
- Enable agents to call external APIs
- Handle tool responses

**Provider**: Ollama (default)

---

## Sample Code

### Simple Function Tool
```python
def get_weather(location: str) -> str:
    """Get weather for a location."""
    return f"Weather in {location}: 72°F, Sunny"

assistant = AssistantAgent(
    name="weather_bot",
    llm_config={
        "config_list": get_ollama_config(),
        "tools": [
            {"function": get_weather, "description": "Get weather info"}
        ]
    }
)
```

---

# Lab 5: Group Chat & Orchestration

## Objectives
- Create GroupChat with multiple agents
- Configure speaker selection
- Implement custom selection strategies
- Manage complex multi-agent workflows

**Provider**: Ollama (default)

---

## Sample Code

### Basic Group Chat
```python
from autogen import GroupChat, GroupChatManager

writer = AssistantAgent("writer", llm_config={"config_list": get_ollama_config()})
editor = AssistantAgent("editor", llm_config={"config_list": get_ollama_config()})

groupchat = GroupChat(agents=[writer, editor], messages=[], max_round=5)
manager = GroupChatManager(groupchat=groupchat, llm_config={"config_list": get_ollama_config()})

user = UserProxyAgent("user", human_input_mode="NEVER")
user.initiate_chat(manager, message="Write and edit a story")
```

---

# Lab 6: Human-in-the-Loop Patterns

## Objectives
- Enable human input in agent conversations
- Configure human input modes
- Build approval workflows
- Handle human feedback

**Provider**: Ollama (default)

---

## Sample Code

### Input Modes
```python
# NEVER - Fully automated
auto_agent = UserProxyAgent("auto", human_input_mode="NEVER")

# ALWAYS - Always asks for input
always_agent = UserProxyAgent("always", human_input_mode="ALWAYS")

# TERMINATE - Only asks when agent requests
terminate_agent = UserProxyAgent("terminate", human_input_mode="TERMINATE")
```

---

# Lab 7: Production Patterns

## Objectives
- Error handling and retry logic
- Logging and monitoring
- Configuration management
- Performance optimization

**Provider**: Ollama (default)

---

## Sample Code

### Error Handling
```python
def create_agent_with_retry(max_retries=3, delay=2):
    for attempt in range(max_retries):
        try:
            agent = AssistantAgent("agent", llm_config={"config_list": get_ollama_config()})
            return agent
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(delay)
    raise Exception("Failed after retries")
```

---

# Course Complete! 🎉

You have completed the AutoGen Essentials course!

### What You Learned
- Environment setup with Ollama (no API keys needed)
- Single agent creation and configuration
- Two-agent conversations
- Tools and function calling
- Group chat orchestration
- Human-in-the-loop patterns
- Production best practices

---

*Built with Microsoft AutoGen*
*Part of the Alpax Prime Training Series*
*Version 5.0 - Ollama-First Edition*
