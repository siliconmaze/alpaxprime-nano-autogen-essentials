# Lab 7: Production Patterns

## Objectives
- Error handling and retry logic
- Logging and monitoring
- Configuration management
- Performance optimization
- Deployment best practices

**Provider**: Ollama (default)

---

## Concept: Production Readiness

Production systems need:
- Error handling
- Logging
- Monitoring
- Graceful degradation
- Resource management

---

## Sample Code

### 1. Error Handling
```python
"""Robust error handling"""
import sys
import time
from config import get_ollama_config
from autogen import AssistantAgent, UserProxyAgent

def create_agent_with_retry(max_retries=3, delay=2):
    """Create agent with retry logic"""
    for attempt in range(max_retries):
        try:
            agent = AssistantAgent(
                "robust_agent",
                llm_config={"config_list": get_ollama_config()}
            )
            return agent
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(delay)
            else:
                raise

# Use
agent = create_agent_with_retry()
print("Agent created successfully!")
```

### 2. Logging Configuration
```python
"""Proper logging setup"""
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('autogen.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("autogen")

from config import get_ollama_config
from autogen import AssistantAgent

agent = AssistantAgent("logged_agent", llm_config={"config_list": get_ollama_config()})
logger.info("Agent created")

response = agent.generate_reply(messages=[{"role": "user", "content": "test"}])
logger.info(f"Response received: {response[:50]}...")
```

### 3. Configuration Management
```python
"""Environment-based config"""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))
    TIMEOUT = int(os.getenv("TIMEOUT", "60"))
    
    @classmethod
    def is_production(cls):
        return not cls.DEBUG

config = Config()
print(f"Running in {'DEBUG' if config.DEBUG else 'PRODUCTION'} mode")
```

### 4. Health Checks
```python
"""Health check system"""
import requests
from config import get_ollama_config
from autogen import AssistantAgent

def check_ollama():
    """Check if Ollama is running"""
    try:
        r = requests.get("http://localhost:11434/api/tags", timeout=5)
        return r.status_code == 200
    except:
        return False

def check_agent(agent):
    """Check if agent can respond"""
    try:
        response = agent.generate_reply(
            messages=[{"role": "user", "content": "OK"}]
        )
        return response is not None
    except:
        return False

# Run health checks
print(f"Ollama: {'OK' if check_ollama() else 'FAILED'}")
agent = AssistantAgent("test", llm_config={"config_list": get_ollama_config()})
print(f"Agent: {'OK' if check_agent(agent) else 'FAILED'}")
```

---

## Exercises

### Ex 7.1: Add Error Handling
Add retry logic to any previous lab.

### Ex 7.2: Implement Logging
Add proper logging to your agents.

### Ex 7.3: Health Monitor
Create a health check script.

---

## Course Complete! 🎉

You have completed the AutoGen Essentials course!

### What You Learned
- Environment setup with Ollama (no API keys needed)
- Single agent creation and configuration
- Two-agent conversations
- Tools and function calling
- Group chat orchestration
- Human-in-the-loop patterns
- Production best practices

### Next Steps
- Build your own multi-agent applications
- Explore advanced AutoGen features
- Contribute to the AutoGen community

---

*Course Complete! 🚀*
