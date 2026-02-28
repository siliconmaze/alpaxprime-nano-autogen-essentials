# Lab 5: Human-in-the-Loop Patterns

## Objective
Learn to incorporate human oversight and input into your AutoGen applications.

## Estimated Time
25 minutes

---

## Background

Human-in-the-loop (HITL) is crucial for:
- Approving critical actions
- Providing domain-specific guidance
- Handling edge cases
- Ensuring safety and compliance

---

## Step 1: Always Ask for Human Input

Create `hitl_always.py`:

```python
"""Lab 5a: Always Ask for Human Input"""
import os
from dotenv import load_dotenv
import autogen
from autogen import AssistantAgent, UserProxyAgent

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

config_list = [{"model": "gpt-4", "api_key": api_key}]

# Create assistant
assistant = AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list},
    system_message="You are a helpful assistant."
)

# UserProxyAgent that ALWAYS asks for human input
user_proxy = UserProxyAgent(
    name="user",
    human_input_mode="ALWAYS",  # Always ask human
    max_consecutive_auto_reply=3
)

# Start conversation
user_proxy.initiate_chat(
    assistant,
    message="Explain what AutoGen is in one sentence."
)
```

---

## Step 2: Terminate with Human Approval

Create `hitl_terminate.py`:

```python
"""Lab 5b: Terminate with Human Approval"""
import os
from dotenv import load_dotenv
import autogen
from autogen import AssistantAgent, UserProxyAgent

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

config_list = [{"model": "gpt-4", "api_key": api_key}]

assistant = AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list},
    system_message="""You are a helpful assistant.
    When you've completed your task, reply with 'APPROVE' to get human approval.
    If human says 'reject', you must try again."""
)

# TERMINATE mode - asks for input when agent wants to terminate
user_proxy = UserProxyAgent(
    name="user",
    human_input_mode="TERMINATE",  # Ask at termination
    max_consecutive_auto_reply=10
)

user_proxy.initiate_chat(
    assistant,
    message="Write a haiku about programming."
)
```

---

## Step 3: Selective Human Intervention

Create `hitl_selective.py`:

```python
"""Lab 5c: Selective Human Intervention"""
import os
from dotenv import load_dotenv
import autogen
from autogen import AssistantAgent, UserProxyAgent

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

config_list = [{"model": "gpt-4", "api_key": api_key}]

# Custom function that checks if human input is needed
def should_request_human(message):
    """Check if message requires human approval."""
    approval_keywords = [
        "delete", "remove", "cancel", "refund", 
        "approve", "confirm", "send", "execute"
    ]
    return any(keyword in message.lower() for keyword in approval_keywords)

# Assistant that can request human input
assistant = AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list},
    system_message="""You are a helpful assistant.
    If you need human approval for a critical action, 
    ask the user explicitly."""
)

# UserProxyAgent with selective intervention
user_proxy = UserProxyAgent(
    name="user",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").find("APPROVE") >= 0
)

user_proxy.initiate_chat(
    assistant,
    message="I need to send an important email. Can you help me draft it?"
)
```

---

## Step 4: Complete Workflow Example

Create `approval_workflow.py`:

```python
"""Lab 5d: Complete Approval Workflow"""
import os
from dotenv import load_dotenv
import autogen
from autogen import AssistantAgent, UserProxyAgent

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

config_list = [{"model": "gpt-4", "api_key": api_key}]

# Assistant that proposes actions
proposer = AssistantAgent(
    name="proposer",
    llm_config={"config_list": config_list},
    system_message="""You suggest actions to take.
    Format your response as:
    ACTION: [description of action]
    APPROVAL_NEEDED: [yes/no]"""
)

# Reviewer that approves/rejects
reviewer = UserProxyAgent(
    name="reviewer",
    human_input_mode="ALWAYS",
    system_message="You are a reviewer. Approve or reject proposed actions."
)

# Executor that carries out approved actions
executor = AssistantAgent(
    name="executor",
    llm_config={"config_list": config_list},
    system_message="You execute approved actions."
)

# User starts the workflow
user_proxy = UserProxyAgent(
    name="user",
    human_input_mode="NEVER"
)

# Propose
user_proxy.initiate_chat(
    proposer,
    message="Propose a marketing campaign for a new product."
)
```

---

## Key Concepts

### Human Input Modes

| Mode | When to Ask |
|------|-------------|
| `"NEVER"` | Never ask, fully automated |
| `"ALWAYS"` | Always ask for each response |
| `"TERMINATE"` | Ask when agent wants to end |

### Termination Detection

```python
# Custom termination message detection
is_termination_msg=lambda x: x.get("content", "").find("DONE") >= 0

# Or with regex
import re
is_termination_msg=lambda x: bool(re.search(r'\b(DONE|APPROVE|EXIT)\b', x.get("content", "")))
```

### Using Human Input in Tools

```python
def process_with_approval(data):
    # Process data
    result = process(data)
    
    # Request approval
    approval = input(f"Approve result? {result} (yes/no): ")
    
    if approval.lower() == "yes":
        return result
    else:
        return "Rejected"
```

---

## Challenge Exercise

Create a "Deployment Approval System":
1. Developer proposes deployment
2. Security reviewer checks for vulnerabilities
3. Manager approves/rejects
4. If approved, deployment executes

---

## What You Learned

✓ Always ask for human input (ALWAYS mode)
✓ Terminate with approval (TERMINATE mode)
✓ Selective human intervention
✓ Building approval workflows

---

## Next Step

Proceed to **Lab 6: Real-World Applications** to build production systems!
