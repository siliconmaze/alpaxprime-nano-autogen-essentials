# Lab 6: Human-in-the-Loop Patterns

## Objectives
- Enable human input in agent conversations
- Configure human input modes
- Build approval workflows
- Handle human feedback

**Provider**: Ollama (default)

---

## Concept: Human-in-the-Loop (HITL)

HITL allows humans to:
- Approve/reject agent actions
- Provide feedback mid-conversation
- Guide agent behavior
- Control dangerous operations

```
Agent ──(request)──▶ Human ──(approval)──▶ Execute
```

---

## Sample Code

### 1. Request Human Input
```python
from config import get_ollama_config
from autogen import AssistantAgent, UserProxyAgent

assistant = AssistantAgent(
    name="assistant",
    llm_config={"config_list": get_ollama_config()}
)

# Human input mode: ALWAYS prompts for input
user = UserProxyAgent(
    name="user",
    human_input_mode="ALWAYS"
)

# Run - will pause for human input
user.initiate_chat(assistant, message="Write a poem")
```

### 2. Input Modes
```python
"""Different human input modes"""
from autogen import UserProxyAgent

# NEVER - Fully automated (no human input)
auto_agent = UserProxyAgent("auto", human_input_mode="NEVER")

# ALWAYS - Always asks for input
always_agent = UserProxyAgent("always", human_input_mode="ALWAYS")

# TERMINATE - Only asks when agent requests
terminate_agent = UserProxyAgent("terminate", human_input_mode="TERMINATE")
```

### 3. Approval Workflow
```python
"""Human approval before execution"""
from config import get_ollama_config
from autogen import AssistantAgent, UserProxyAgent

assistant = AssistantAgent(
    name="writer",
    system_message="You write code. Wait for approval before finalizing.",
    llm_config={"config_list": get_ollama_config()}
)

user = UserProxyAgent(
    name="approver",
    human_input_mode="TERMINATE"
)

# This will pause and ask for approval
user.initiate_chat(assistant, message="Write a Python function to calculate fibonacci")
```

---

## Exercises

### Ex 6.1: Content Moderator
Create a system where human approves content before posting.

### Ex 6.2: Decision Maker
Build an agent that asks human for decisions.

### Ex 6.3: Feedback Loop
Create an agent that incorporates human feedback.

---

## Lab 6 Complete ✅
Next: [Lab 7: Production Patterns](../Lab7/README.md)
