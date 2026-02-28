# Lab 7: Production Patterns

## Objective
Learn production-ready patterns for error handling, state management, and async support.

## Estimated Time
35 minutes

---

## Pattern 1: Error Handling

Create `error_handling.py`:

```python
"""Lab 7a: Error Handling Patterns"""
import os
import logging
from dotenv import load_dotenv
import autogen
from autogen import AssistantAgent, UserProxyAgent

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

config_list = [{"model": "gpt-4", "api_key": api_key}]

# Custom error handling agent
class SafeAssistantAgent(AssistantAgent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_retries = 3
        
    def receive(self, message, sender):
        try:
            super().receive(message, sender)
        except Exception as e:
            logger.error(f"Error receiving message: {e}")
            # Handle error gracefully
            self._handle_error(e, message, sender)
    
    def _handle_error(self, error, message, sender):
        """Custom error handling logic."""
        error_msg = f"I encountered an error: {str(error)}. Let me try again."
        self.send(error_msg, sender)

# Or use try-except in conversation
assistant = AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list}
)

user_proxy = UserProxyAgent(
    name="user",
    human_input_mode="NEVER"
)

try:
    user_proxy.initiate_chat(
        assistant,
        message="Explain quantum computing."
    )
except Exception as e:
    print(f"Conversation failed: {e}")
    # Handle gracefully - maybe retry or notify
```

---

## Pattern 2: Conversation State Management

Create `state_management.py`:

```python
"""Lab 7b: State Management"""
import os
import json
from dotenv import load_dotenv
import autogen
from autogen import AssistantAgent, UserProxyAgent

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# State manager for conversations
class ConversationState:
    def __init__(self):
        self.conversations = {}
        self.metadata = {}
        
    def save(self, conversation_id, messages):
        """Save conversation messages."""
        self.conversations[conversation_id] = messages
        
    def load(self, conversation_id):
        """Load conversation messages."""
        return self.conversations.get(conversation_id, [])
    
    def add_metadata(self, key, value):
        """Add metadata about conversation."""
        self.metadata[key] = value
        
    def export(self, filepath):
        """Export conversation to file."""
        with open(filepath, 'w') as f:
            json.dump({
                'conversations': self.conversations,
                'metadata': self.metadata
            }, f, indent=2)

# Usage
state = ConversationState()
conversation_id = "conv_001"

config_list = [{"model": "gpt-4", "api_key": api_key}]

assistant = AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list}
)

user_proxy = UserProxyAgent(
    name="user",
    human_input_mode="NEVER"
)

# Track messages
messages = []

def track_messages(sender, recipient, message):
    messages.append({
        "from": sender.name,
        "to": recipient.name,
        "message": message
    })

# Start conversation
user_proxy.initiate_chat(assistant, message="Hello!")

# Save state
state.save(conversation_id, messages)
state.add_metadata("topic", "greeting")
state.export(f"{conversation_id}.json")

print(f"Saved {len(messages)} messages")
```

---

## Pattern 3: Async Support

Create `async_support.py`:

```python
"""Lab 7c: Async Support (Python 3.7+)"""
import os
import asyncio
from dotenv import load_dotenv
import autogen
from autogen import AssistantAgent, UserProxyAgent

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

config_list = [{"model": "gpt-4", "api_key": api_key}]

async def run_conversation(topic):
    """Run a conversation asynchronously."""
    assistant = AssistantAgent(
        name=f"assistant_{topic}",
        llm_config={"config_list": config_list}
    )
    
    user_proxy = UserProxyAgent(
        name="user",
        human_input_mode="NEVER"
    )
    
    await user_proxy.a_initiate_chat(
        assistant,
        message=f"Tell me about {topic}."
    )

async def main():
    """Run multiple conversations concurrently."""
    topics = ["AI", "Python", "Cloud Computing"]
    
    # Run all conversations in parallel
    tasks = [run_conversation(topic) for topic in topics]
    await asyncio.gather(*tasks)
    
    print("All conversations completed!")

# Run async
# asyncio.run(main())

# Note: AutoGen supports async methods:
# - a_initiate_chat()
# - a_send()
# - a_receive()
```

---

## Pattern 4: Caching and Performance

Create `caching.py`:

```python
"""Lab 7d: Caching and Performance"""
import os
from dotenv import load_dotenv
import autogen
from autogen import AssistantAgent, UserProxyAgent

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Enable response caching
config_list = [
    {
        "model": "gpt-4",
        "api_key": api_key,
        "cache_seed": 42  # Same seed = cached responses
    }
]

# Or disable caching
config_list_no_cache = [
    {
        "model": "gpt-4",
        "api_key": api_key,
        "cache_seed": None  # No caching
    }
]

# Streaming responses
assistant = AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list}
)

# For streaming (if supported by model):
# response = assistant.generate(
#     messages,
#     stream=True,
#     callback=lambda chunk: print(chunk, end="")
# )

print("Caching and performance patterns ready!")
```

---

## Pattern 5: Rate Limiting

Create `rate_limiting.py`:

```python
"""Lab 7e: Rate Limiting"""
import time
import os
from dotenv import load_dotenv
import autogen
from autogen import AssistantAgent, UserProxyAgent

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

class RateLimitedAssistant:
    def __init__(self, calls_per_minute=60):
        self.calls_per_minute = calls_per_minute
        self.calls = []
        
    def wait_if_needed(self):
        """Wait if rate limit would be exceeded."""
        now = time.time()
        # Remove calls older than 1 minute
        self.calls = [t for t in self.calls if now - t < 60]
        
        if len(self.calls) >= self.calls_per_minute:
            wait_time = 60 - (now - self.calls[0])
            print(f"Rate limit reached. Waiting {wait_time:.1f}s...")
            time.sleep(wait_time)
        
        self.calls.append(time.time())
        
    def chat(self, agent, message):
        """Send message with rate limiting."""
        self.wait_if_needed()
        return agent.chat(message)

# Usage
rate_limiter = RateLimitedAssistant(calls_per_minute=50)

config_list = [{"model": "gpt-4", "api_key": api_key}]
assistant = AssistantAgent(name="assistant", llm_config={"config_list": config_list})
user_proxy = UserProxyAgent(name="user", human_input_mode="NEVER")

# Messages will be rate-limited
for i in range(10):
    user_proxy.initiate_chat(assistant, message=f"Message {i}")
    rate_limiter.wait_if_needed()
```

---

## What You Learned

✓ Error handling in agent conversations
✓ State management and persistence
✓ Async conversation support
✓ Caching for performance
✓ Rate limiting strategies

---

## Congratulations!

You've completed all labs in the AutoGen course! 

## Next Steps

1. Build your own multi-agent applications
2. Explore the AutoGen documentation
3. Join the AutoGen community
4. Contribute to the project

---

## Resources

- AutoGen GitHub: https://github.com/microsoft/autogen
- Documentation: https://microsoft.github.io/autogen/
- Discord: https://discord.gg/pAbnFJrkgjw
