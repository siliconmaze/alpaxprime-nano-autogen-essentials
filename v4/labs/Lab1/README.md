# Lab 1: Environment Setup

## Objectives

By the end of this lab, you will be able to:
- Install Python and required packages
- Configure at least one LLM provider
- Create and run your first AutoGen agent
- Understand the configuration system

## Prerequisites

- Python 3.10 or higher
- A code editor (VS Code recommended)
- At least one LLM provider account

---

## Part 1: Installing Python and Dependencies

### Step 1.1: Check Python Version

```bash
python3 --version
```

You should see something like:
```
Python 3.10.12
```

If you don't have Python, install it:
- **macOS**: `brew install python3`
- **Linux**: `sudo apt install python3` or `sudo yum install python3`
- **Windows**: Download from python.org

### Step 1.2: Create Virtual Environment (Recommended)

```bash
# Create a virtual environment
python3 -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### Step 1.3: Install AutoGen

```bash
pip install pyautogen python-dotenv
```

Verify installation:
```bash
python -c "import autogen; print(f'AutoGen version: {autogen.__version__}')"
```

---

## Part 2: Provider Setup

### Option A: Ollama (Local, Free)

**Pros**: Free, private, no internet required
**Cons**: Requires hardware, slower than cloud

```bash
# Install Ollama
brew install ollama

# Pull a model
ollama pull qwen2.5-coder:7b
# Or: ollama pull llama3

# Start the server
ollama serve
```

In a new terminal or background process.

### Option B: DeepSeek (Cloud, Cheap)

**Pros**: Cheap, fast, good quality
**Cons**: Requires internet, costs money

1. Go to https://platform.deepseek.com
2. Sign up for free account
3. Create API key
4. Add to `.env` file:

```bash
DEEPSEEK_API_KEY=your_key_here
```

### Option C: MiniMax (Cloud, Long Context)

**Pros**: 200K context window, competitive pricing
**Cons**: Less known

1. Go to https://platform.minimax.io
2. Sign up
3. Get API key
4. Add to `.env`:

```bash
MINIMAX_API_KEY=your_key_here
```

---

## Part 3: Configuration Files

### Creating .env File

Create a file named `.env` in your project root:

```bash
# Required for at least one provider
DEEPSEEK_API_KEY=sk-your-deepseek-key
MINIMAX_API_KEY=sk-your-minimax-key

# Optional
OPENAI_API_KEY=sk-your-openai-key
ANTHROPIC_API_KEY=sk-ant-your-anthropic-key

# Server (if needed)
PORT=3901
DEBUG=true
```

### Configuration Helper Module

Create `config.py`:

```python
"""Configuration module for AutoGen course."""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_ollama_config(model: str = "qwen2.5-coder:7b"):
    """Get Ollama configuration."""
    return [{
        "model": model,
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama",
        "api_type": "openai"
    }]

def get_deepseek_config(model: str = "deepseek-chat"):
    """Get DeepSeek configuration."""
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError("DEEPSEEK_API_KEY not set")
    return [{
        "model": model,
        "base_url": "https://api.deepseek.com/v1",
        "api_key": api_key
    }]

def get_minimax_config(model: str = "MiniMax-Text-01"):
    """Get MiniMax configuration."""
    api_key = os.getenv("MINIMAX_API_KEY")
    if not api_key:
        raise ValueError("MINIMAX_API_KEY not set")
    return [{
        "model": model,
        "base_url": "https://api.minimax.io/anthropic/v1",
        "api_key": api_key
    }]

def get_config(provider: str = "auto"):
    """
    Get configuration for specified provider.
    
    Args:
        provider: "ollama", "deepseek", "minimax", or "auto" (first available)
    
    Returns:
        config_list for AutoGen
    """
    if provider == "auto":
        # Try each provider in order
        for p in ["deepseek", "minimax", "ollama"]:
            try:
                return get_config(p)
            except:
                continue
        raise ValueError("No valid provider found")
    
    providers = {
        "ollama": get_ollama_config,
        "deepseek": get_deepseek_config,
        "minimax": get_minimax_config
    }
    
    if provider not in providers:
        raise ValueError(f"Unknown provider: {provider}")
    
    return providers[provider]()
```

---

## Part 4: Your First Agent

### Basic Example

Create `first_agent.py`:

```python
"""Your first AutoGen agent."""
import os
from dotenv import load_dotenv
from autogen import AssistantAgent

# Load configuration
load_dotenv()

# Try to get a working config
def get_config():
    # Try DeepSeek first
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if api_key:
        return [{
            "model": "deepseek-chat",
            "base_url": "https://api.deepseek.com/v1",
            "api_key": api_key
        }]
    
    # Fall back to Ollama
    return [{
        "model": "qwen2.5-coder:7b",
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama",
        "api_type": "openai"
    }]

config_list = get_config()

# Create your first agent
assistant = AssistantAgent(
    name="my_first_agent",
    llm_config={"config_list": config_list}
)

# Send a message
response = assistant.generate_reply(
    messages=[{"role": "user", "content": "Say 'Hello, World!' in exactly those words."}]
)

print(f"Agent response: {response}")
```

Run it:
```bash
python first_agent.py
```

---

## Exercises

### Exercise 1.1: Verify Installation
Create a script that verifies all dependencies are installed correctly.

**Solution**:
```python
"""Verify all dependencies are installed."""
import sys

def check_package(name):
    try:
        __import__(name)
        print(f"✓ {name} is installed")
        return True
    except ImportError:
        print(f"✗ {name} is NOT installed")
        return False

packages = ["autogen", "dotenv", "openai", "langchain"]
all_installed = all(check_package(p.replace("-", "_")) for p in packages)

if all_installed:
    print("\n✓ All dependencies installed!")
else:
    print("\n✗ Some dependencies are missing. Run: pip install pyautogen python-dotenv")
```

### Exercise 1.2: Test All Providers
Create a script that tries each provider and reports which works.

**Solution**:
```python
"""Test all configured providers."""
import os
from dotenv import load_dotenv
from autogen import AssistantAgent

load_dotenv()

def test_provider(name, config):
    """Test a provider configuration."""
    try:
        agent = AssistantAgent(name=f"test_{name}", llm_config={"config_list": [config]})
        response = agent.generate_reply(messages=[{"role": "user", "content": "OK"}])
        print(f"✓ {name}: Working")
        return True
    except Exception as e:
        print(f"✗ {name}: {str(e)[:50]}")
        return False

# Test Ollama
try:
    test_provider("ollama", {
        "model": "qwen2.5-coder:7b",
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama",
        "api_type": "openai"
    })
except:
    pass

# Test DeepSeek
if os.getenv("DEEPSEEK_API_KEY"):
    test_provider("deepseek", {
        "model": "deepseek-chat",
        "base_url": "https://api.deepseek.com/v1",
        "api_key": os.getenv("DEEPSEEK_API_KEY")
    })

# Test MiniMax
if os.getenv("MINIMAX_API_KEY"):
    test_provider("minimax", {
        "model": "MiniMax-Text-01",
        "base_url": "https://api.minimax.io/anthropic/v1",
        "api_key": os.getenv("MINIMAX_API_KEY")
    })
```

### Exercise 1.3: Compare Response Times
Create a benchmark script that compares provider speeds.

**Solution**:
```python
"""Benchmark provider response times."""
import time
import os
from dotenv import load_dotenv
from autogen import AssistantAgent

load_dotenv()

providers = []

# Add available providers
if os.getenv("DEEPSEEK_API_KEY"):
    providers.append(("deepseek", {
        "model": "deepseek-chat",
        "base_url": "https://api.deepseek.com/v1",
        "api_key": os.getenv("DEEPSEEK_API_KEY")
    }))

if os.getenv("MINIMAX_API_KEY"):
    providers.append(("minimax", {
        "model": "MiniMax-Text-01",
        "base_url": "https://api.minimax.io/anthropic/v1",
        "api_key": os.getenv("MINIMAX_API_KEY")
    }))

# Benchmark
print("Benchmarking providers...\n")
for name, config in providers:
    times = []
    for i in range(3):
        agent = AssistantAgent(name="bench", llm_config={"config_list": [config]})
        start = time.time()
        agent.generate_reply(messages=[{"role": "user", "content": "Count to 3"}])
        times.append(time.time() - start)
    
    avg = sum(times) / len(times)
    print(f"{name}: {avg:.2f}s average")
```

---

## Common Issues

### "ModuleNotFoundError: No module named 'autogen'"

**Solution**:
```bash
pip install pyautogen
```

### "Connection refused" (Ollama)

**Solution**:
```bash
# Start Ollama in a terminal
ollama serve
```

### "Invalid API key"

**Solution**:
1. Check your .env file exists in the right directory
2. Verify API key is correct (no extra spaces)
3. Check provider dashboard that key is active

### "Rate limit exceeded"

**Solution**:
- Wait a minute and try again
- Add retry logic (covered in Lab 7)
- Consider using a different provider

---

## Summary

In this lab, you learned to:
- ✓ Install Python and required packages
- ✓ Configure at least one LLM provider
- ✓ Create your first AutoGen agent
- ✓ Understand the configuration system

---

## Next Lab

[Lab 2: Single Agent Fundamentals](../Lab2/README.md)

---

*Lab 1 Complete!*
