# Lab 7: Exercises & Deep Dive

## Exercise 1: Complete Production System

```python
import logging
import time
from datetime import datetime
from functools import wraps

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("production_agent")

class AgentMetrics:
    """Track agent performance metrics."""
    
    def __init__(self):
        self.requests = []
        self.errors = []
        
    def record(self, success, duration, tokens=None, error=None):
        self.requests.append({
            "timestamp": datetime.now().isoformat(),
            "success": success,
            "duration_ms": duration,
            "tokens": tokens
        })
        if error:
            self.errors.append({"timestamp": datetime.now(), "error": str(error)})
    
    def get_stats(self):
        total = len(self.requests)
        successful = sum(1 for r in self.requests if r["success"])
        return {
            "total_requests": total,
            "success_rate": successful / total if total else 0,
            "total_errors": len(self.errors)
        }

def with_metrics(metrics: AgentMetrics):
    """Decorator to track metrics."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            try:
                result = func(*args, **kwargs)
                duration = (time.time() - start) * 1000
                metrics.record(True, duration)
                return result
            except Exception as e:
                duration = (time.time() - start) * 1000
                metrics.record(False, duration, error=e)
                raise
        return wrapper
    return decorator

# Usage
metrics = AgentMetrics()

@with_metrics(metrics)
def call_agent(agent, message):
    return agent.generate_reply(messages=[{"role": "user", "content": message}])

# Run
assistant = AssistantAgent(name="prod_agent", llm_config={"config_list": config_list})
call_agent(assistant, "Hello!")

print(metrics.get_stats())
```

---

## Exercise 2: Error Recovery

```python
import time

class ResilientAgent:
    """Agent with automatic error recovery."""
    
    def __init__(self, agent, max_retries=3):
        self.agent = agent
        self.max_retries = max_retries
        
    def send_message(self, message: str):
        last_error = None
        
        for attempt in range(self.max_retries):
            try:
                return self.agent.generate_reply(
                    messages=[{"role": "user", "content": message}]
                )
            except Exception as e:
                last_error = e
                wait_time = 2 ** attempt  # Exponential backoff
                logger.warning(f"Attempt {attempt+1} failed: {e}. Retrying in {wait_time}s")
                time.sleep(wait_time)
                
        raise last_error  # All retries failed

# Usage
resilient = ResilientAgent(assistant)
result = resilient.send_message("Hello!")
```
