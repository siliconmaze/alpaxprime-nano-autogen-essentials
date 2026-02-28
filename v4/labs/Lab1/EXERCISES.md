# Lab 1: Exercises & Solutions

## Exercise 1: Install and Verify AutoGen

### Task
Install AutoGen and verify the installation works.

### Solution
```bash
pip install pyautogen python-dotenv
python -c "import autogen; print(autogen.__version__)"
```

---

## Exercise 2: Configure Multiple Providers

### Task
Set up configuration for all three providers (Ollama, DeepSeek, MiniMax).

### Solution

Create `my_config.py`:

```python
import os
from dotenv import load_dotenv

load_dotenv()

def get_config(provider="deepseek"):
    """Get config for specified provider."""
    
    configs = {
        "ollama": [{
            "model": "qwen2.5-coder:7b",
            "base_url": "http://localhost:11434/v1",
            "api_key": "ollama",
            "api_type": "openai"
        }],
        "deepseek": [{
            "model": "deepseek-chat",
            "base_url": "https://api.deepseek.com/v1",
            "api_key": os.getenv("DEEPSEEK_API_KEY")
        }],
        "minimax": [{
            "model": "MiniMax-Text-01",
            "base_url": "https://api.minimax.io/anthropic/v1",
            "api_key": os.getenv("MINIMAX_API_KEY")
        }]
    }
    
    return configs.get(provider, configs["deepseek"])

# Usage
from autogen import AssistantAgent
config_list = get_config("ollama")
agent = AssistantAgent(name="test", llm_config={"config_list": config_list})
```

---

## Exercise 3: Environment Variable Best Practices

### Task
Create a robust .env file with all needed variables.

### Solution

```bash
# .env file

# === Required for at least one provider ===
DEEPSEEK_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
MINIMAX_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx  
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxxxxxx

# === Optional: Service Configuration ===
TELEGRAM_BOT_TOKEN=1234567890:xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
GMAIL_CLIENT_ID=xxxxxxxxxxxxx.apps.googleusercontent.com
GMAIL_CLIENT_SECRET=xxxxxxxxxxxxxxxxxxxx

# === Optional: Database ===
DATABASE_URL=file:prime-agent.db

# === Optional: Server ===
PORT=3901
DEBUG=false
```

### Python loader:

```python
from dotenv import load_dotenv
import os

class EnvConfig:
    """Load and validate environment variables."""
    
    _loaded = False
    
    @classmethod
    def load(cls):
        if cls._loaded:
            return
        load_dotenv()
        cls._loaded = True
    
    @classmethod
    def get(cls, key, default=None, required=False):
        cls.load()
        value = os.getenv(key, default)
        if required and not value:
            raise ValueError(f"Required env var {key} not set")
        return value
    
    @classmethod
    def get_api_key(cls, provider):
        """Get API key for provider."""
        keys = {
            "deepseek": cls.get("DEEPSEEK_API_KEY", required=True),
            "minimax": cls.get("MINIMAX_API_KEY", required=True),
            "openai": cls.get("OPENAI_API_KEY", required=True),
            "anthropic": cls.get("ANTHROPIC_API_KEY", required=True),
        }
        return keys.get(provider.lower())
```

---

## Exercise 4: Test All Providers

### Task
Write a script that tests all available providers.

### Solution:

```python
import os
from dotenv import load_dotenv
from autogen import AssistantAgent

load_dotenv()

PROVIDERS = {
    "ollama": {
        "model": "qwen2.5-coder:7b",
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama"
    },
    "deepseek": {
        "model": "deepseek-chat", 
        "base_url": "https://api.deepseek.com/v1",
        "api_key": os.getenv("DEEPSEEK_API_KEY")
    },
    "minimax": {
        "model": "MiniMax-Text-01",
        "base_url": "https://api.minimax.io/anthropic/v1", 
        "api_key": os.getenv("MINIMAX_API_KEY")
    }
}

def test_provider(name, config):
    """Test a provider configuration."""
    print(f"\nTesting {name}...")
    
    if not config.get("api_key"):
        print(f"  ✗ No API key for {name}")
        return False
    
    try:
        agent = AssistantAgent(
            name=f"test_{name}",
            llm_config={"config_list": [config]}
        )
        response = agent.generate_reply(
            messages=[{"role": "user", "content": "Say 'OK' if you can hear me."}]
        )
        print(f"  ✓ {name} works: {response}")
        return True
    except Exception as e:
        print(f"  ✗ {name} failed: {e}")
        return False

# Test all
print("=" * 50)
print("Testing All Providers")
print("=" * 50)

results = {}
for name, config in PROVIDERS.items():
    results[name] = test_provider(name, config)

print("\n" + "=" * 50)
print("Summary:")
print("=" * 50)
for name, success in results.items():
    status = "✓ Working" if success else "✗ Failed"
    print(f"  {name}: {status}")
```

---

## Exercise 5: Compare Provider Performance

### Task
Benchmark different providers.

### Solution:

```python
import time
import os
from dotenv import load_dotenv
from autogen import AssistantAgent

load_dotenv()

def benchmark(provider_config, prompt="Count to 10", runs=3):
    """Benchmark a provider."""
    times = []
    
    for i in range(runs):
        agent = AssistantAgent(
            name="bench",
            llm_config={"config_list": [provider_config]}
        )
        
        start = time.time()
        agent.generate_reply(messages=[{"role": "user", "content": prompt}])
        elapsed = time.time() - start
        times.append(elapsed)
    
    avg = sum(times) / len(times)
    return avg, times

# Benchmark each
providers = [
    ("ollama", {"model": "qwen2.5-coder:7b", 
                "base_url": "http://localhost:11434/v1", 
                "api_key": "ollama"}),
]

if os.getenv("DEEPSEEK_API_KEY"):
    providers.append(("deepseek", {
        "model": "deepseek-chat",
        "base_url": "https://api.deepseek.com/v1", 
        "api_key": os.getenv("DEEPSEEK_API_KEY")
    }))

print("Provider Benchmark")
print("-" * 30)

for name, config in providers:
    avg, times = benchmark(config)
    print(f"{name}: {avg:.2f}s avg ({runs} runs)")
```
