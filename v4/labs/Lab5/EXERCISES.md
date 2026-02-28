# Lab 5: Exercises & Deep Dive

## Exercise 1: Code Review Team

```python
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager

# Different roles for code review
syntax_checker = AssistantAgent(
    name="syntax_checker",
    system_message="You check Python code for syntax errors and style issues.",
    llm_config={"config_list": config_list}
)

logic_checker = AssistantAgent(
    name="logic_checker", 
    system_message="You review code logic and algorithms for bugs.",
    llm_config={"config_list": config_list}
)

security_checker = AssistantAgent(
    name="security_checker",
    system_message="You check for security vulnerabilities in code.",
    llm_config={"config_list": config_list}
)

doc_checker = AssistantAgent(
    name="doc_checker",
    system_message="You verify code has proper documentation and comments.",
    llm_config={"config_list": config_list}
)

# Group chat
groupchat = GroupChat(
    agents=[syntax_checker, logic_checker, security_checker, doc_checker],
    messages=[],
    max_round=8
)

manager = GroupChatManager(groupchat=groupchat, llm_config={"config_list": config_list})

user = UserProxyAgent(name="user", human_input_mode="NEVER")

code = """
def add_numbers(a, b):
    return a + b
"""

user.initiate_chat(manager, message=f"Review this code:\n{code}")
```

---

## Exercise 2: Content Creation Team

```python
# Content creation pipeline
researcher = AssistantAgent(
    name="researcher",
    system_message="Research topics thoroughly with credible sources.",
    llm_config={"config_list": config_list}
)

outliner = AssistantAgent(
    name="outliner",
    system_message="Create clear, logical outlines for content.",
    llm_config={"config_list": config_list}
)

writer = AssistantAgent(
    name="writer",
    system_message="Write engaging, well-structured content.",
    llm_config={"config_list": config_list}
)

editor = AssistantAgent(
    name="editor",
    system_message="Edit content for clarity, grammar, and flow.",
    llm_config={"config_list": config_list}
)

# Sequential workflow
user = UserProxyAgent(name="user", human_input_mode="NEVER")

user.initiate_chat(researcher, message="Research: Benefits of meditation")
user.initiate_chat(outliner, message="Create outline based on research")
user.initiate_chat(writer, message="Write article from outline")
user.initiate_chat(editor, message="Edit and polish the article")
```
