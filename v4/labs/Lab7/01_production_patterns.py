"""
Lab 7: Production Patterns
============================

Best practices for production AutoGen deployments.

Key Concepts:
- Error handling and recovery
- Logging and monitoring
- Retry logic
- Session management

Run with:
    python 01_production_patterns.py
"""

import os
import time
import logging
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("autogen")

load_dotenv()

print("=" * 60)
print("Lab 7: Production Patterns")
print("=" * 60)

api_key = os.getenv("DEEPSEEK_API_KEY", "")
if not api_key:
    api_key = "ollama"
    model = "qwen2.5-coder:7b"
    base_url = "http://localhost:11434/v1"
else:
    model = "deepseek-chat"
    base_url = "https://api.deepseek.com/v1"

config_list = [{"model": model, "base_url": base_url, "api_key": api_key}]

# ============================================================================
# PATTERN 1: RETRY LOGIC
# ============================================================================

print("\n[1] Retry Logic Pattern")

def retry_with_backoff(func, max_retries=3, backoff=1):
    """Retry with exponential backoff."""
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            wait = backoff * (2 ** attempt)
            logger.warning(f"Attempt {attempt+1} failed: {e}. Retrying in {wait}s...")
            time.sleep(wait)

assistant = AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list, "timeout": 60}
)

user_proxy = UserProxyAgent(name="user", human_input_mode="NEVER")

def make_request():
    return user_proxy.generate_reply(
        messages=[{"role": "user", "content": "Hello!"}],
        sender=assistant
    )

# Try with retry
try:
    result = retry_with_backoff(make_request, max_retries=3)
    print(f"    ✓ Request succeeded: {str(result)[:40]}...")
except Exception as e:
    print(f"    ✗ All retries failed: {e}")

# ============================================================================
# PATTERN 2: ERROR HANDLING
# ============================================================================

print("\n[2] Error Handling Pattern")

def safe_agent_call(agent, user_proxy, message):
    """Safe wrapper with error handling."""
    try:
        response = user_proxy.generate_reply(
            messages=[{"role": "user", "content": message}],
            sender=agent
        )
        return {"success": True, "result": response}
    except Exception as e:
        logger.error(f"Agent call failed: {e}")
        return {"success": False, "error": str(e)}

# Test with error handling
result = safe_agent_call(assistant, user_proxy, "Hello!")
print(f"    Result: success={result['success']}")

result = safe_agent_call(assistant, user_proxy, "invalid request!!!")
print(f"    Result: success={result['success']}")

# ============================================================================
# PATTERN 3: SESSION MANAGEMENT
# ============================================================================

print("\n[3] Session Management Pattern")

class AgentSession:
    """Manage agent sessions with state."""
    
    def __init__(self, session_id, config_list):
        self.session_id = session_id
        self.config_list = config_list
        self.agent = AssistantAgent(
            name=f"agent_{session_id}",
            llm_config={"config_list": config_list}
        )
        self.message_count = 0
        self.created_at = time.time()
        
    def send(self, message):
        """Send message and track stats."""
        self.message_count += 1
        logger.info(f"Session {self.session_id}: message {self.message_count}")
        
        user_proxy = UserProxyAgent(
            name=f"user_{self.session_id}",
            human_input_mode="NEVER"
        )
        
        return user_proxy.generate_reply(
            messages=[{"role": "user", "content": message}],
            sender=self.agent
        )
    
    def get_stats(self):
        """Get session statistics."""
        return {
            "session_id": self.session_id,
            "messages": self.message_count,
            "age_seconds": time.time() - self.created_at
        }

# Create session
session = AgentSession("session_001", config_list)
response = session.send("Hello!")
print(f"    Response: {str(response)[:40]}...")
print(f"    Stats: {session.get_stats()}")

print("\n" + "=" * 60)
print("✓ Production Patterns Complete!")
print("=" * 60)
