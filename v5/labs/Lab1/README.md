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

### Create config.py

```python
"""AutoGen v5 Configuration - Ollama First"""
import os
from dotenv import load_dotenv
load_dotenv()

def get_ollama_config(model=None):
    model = model or os.getenv("OLLAMA_MODEL", "qwen2.5-coder:7b")
    return [{
        "model": model,
        "base_url": os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1"),
        "api_key": "ollama",
        "api_type": "openai"
    }]

def get_deepseek_config():
    key = os.getenv("DEEPSEEK_API_KEY")
    if not key:
        raise ValueError("DEEPSEEK_API_KEY required")
    return [{"model": "deepseek-chat", "base_url": "https://api.deepseek.com/v1", "api_key": key}]

def get_config(provider="auto"):
    if provider == "auto":
        try: return get_ollama_config()
        except: pass
        if os.getenv("DEEPSEEK_API_KEY"): return get_deepseek_config()
        raise ValueError("No provider available")
    return {"ollama": get_ollama_config, "deepseek": get_deepseek_config}.get(provider, get_ollama_config)()
```

---

## Part 4: Your First Agent

### Sample 1: Basic Agent

```python
"""Your first AutoGen agent with Ollama"""
from config import get_ollama_config
from autogen import AssistantAgent

config = get_ollama_config()
agent = AssistantAgent(name="hello_agent", llm_config={"config_list": config})

response = agent.generate_reply(
    messages=[{"role": "user", "content": "Say 'Hello, World!' exactly"}]
)
print(f"Agent: {response}")
```

### Sample 2: Agent with System Message

```python
"""Custom personality agent"""
from config import get_ollama_config
from autogen import AssistantAgent

agent = AssistantAgent(
    name="poet",
    system_message="You are a haiku poet. Write 5-7-5 haikus.",
    llm_config={"config_list": get_ollama_config(), "temperature": 0.9}
)

response = agent.generate_reply(
    messages=[{"role": "user", "content": "Write about coding"}]
)
print(response)
```

---

## Exercises

### Exercise 1.1: Verify Installation
```python
"""Verify dependencies"""
for pkg in ["autogen", "dotenv", "requests"]:
    try:
        __import__(pkg.replace("-", "_"))
        print(f"OK: {pkg}")
    except:
        print(f"MISSING: {pkg}")
```

### Exercise 1.2: Test Ollama
```python
"""Test Ollama connection"""
import requests
try:
    r = requests.get("http://localhost:11434/api/tags")
    models = r.json().get("models", [])
    print(f"Ollama running with {len(models)} models")
except Exception as e:
    print(f"Error: {e}")
```

---

## Troubleshooting

| Error | Solution |
|-------|----------|
| Connection refused | Run `ollama serve` |
| Model not found | Run `ollama pull qwen2.5-coder:7b` |
| API key error | Check .env file exists |

---

## Lab 1 Complete ✅

Next: [Lab 2: Single Agent Fundamentals](../Lab2/README.md)
