# Lab 6: Exercises & Deep Dive

## Exercise 1: Approval Workflow

```python
from autogen import AssistantAgent, UserProxyAgent

class ApprovalWorkflow:
    """Human-in-the-loop approval workflow."""
    
    def __init__(self, config_list):
        self.agent = AssistantAgent(
            name="workflow_agent",
            system_message="""You help with workflows.
            When human approval is needed, state clearly what you want to do.""",
            llm_config={"config_list": config_list}
        )
        
    def run_with_approval(self, task: str, approver_input_fn) -> str:
        """Run task requiring approval."""
        # Get suggestion
        suggestion = self.agent.generate_reply(
            messages=[{"role": "user", "content": task}]
        )
        
        print(f"Suggested action: {suggestion}")
        
        # Get human approval
        approved = approver_input_fn(suggestion)
        
        if approved:
            # Execute
            result = self.agent.generate_reply(
                messages=[
                    {"role": "user", "content": f"Execute: {suggestion}"}
                ]
            )
            return result
        else:
            return "Action not approved."

# Usage
def ask_approval(suggestion):
    response = input(f"Approve this action? (y/n): {suggestion[:50]}...")
    return response.lower() == 'y'

workflow = ApprovalWorkflow(config_list)
result = workflow.run_with_approval("Send email to team", ask_approval)
```

---

## Exercise 2: Interactive Q&A

```python
from autogen import AssistantAgent, UserProxyAgent

# Agent that asks clarifying questions
clarifying_agent = AssistantAgent(
    name="clarifying_agent",
    system_message="""You ask clarifying questions when needed.
    Don't assume - verify understanding.
    Be thorough before giving advice.""",
    llm_config={"config_list": config_list}
)

user_proxy = UserProxyAgent(
    name="user",
    human_input_mode="ALWAYS"  # Always ask human
)

# This will prompt for input after each response
user_proxy.initiate_chat(clarifying_agent, message="How do I learn Python?")
```
