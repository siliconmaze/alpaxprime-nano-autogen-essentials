# Lab 3: Exercises & Deep Dive

## Exercise 1: Debate Team

### Task
Create a debate between two agents with opposing views.

```python
from autogen import AssistantAgent, UserProxyAgent

# Pro agent
pro_agent = AssistantAgent(
    name="pro_side",
    system_message="""You are arguing FOR the topic.
    Present strong arguments supporting it.
    Use logic, evidence, and examples.
    Address counterarguments.""",
    llm_config={"config_list": config_list}
)

# Con agent  
con_agent = AssistantAgent(
    name="con_side",
    system_message="""You are arguing AGAINST the topic.
    Present strong arguments opposing it.
    Use logic, evidence, and examples.
    Point out flaws in the opposing view.""",
    llm_config={"config_list": config_list}
)

# Moderator
moderator = AssistantAgent(
    name="moderator",
    system_message="""You moderate a debate fairly.
    Summarize each side's arguments.
    Keep the discussion civil.
    Make no judgments about who won.""",
    llm_config={"config_list": config_list}
)

user = UserProxyAgent(name="user", human_input_mode="NEVER")

# Start debate
user.initiate_chat(pro_agent, message="Should AI be regulated? Argue YES.")
pro_args = pro_agent.last_message()["content"]

user.initiate_chat(con_agent, message=f"Should AI be regulated? Argue NO. Here's the pro argument: {pro_args[:200]}")

user.initiate_chat(moderator, message=f"Summarize this debate. Pro: {pro_args[:200]}, Con: {con_agent.last_message()['content'][:200]}")
```

---

## Exercise 2: Translation Pipeline

### Task
Build a translation pipeline through multiple agents.

```python
from autogen import AssistantAgent, UserProxyAgent

# English to French
en_to_fr = AssistantAgent(
    name="en_to_fr",
    system_message="""You translate English to French.
    Provide natural, idiomatic translations.
    Only output the translation, nothing else.""",
    llm_config={"config_list": config_list}
)

# French to Spanish
fr_to_es = AssistantAgent(
    name="fr_to_es",
    system_message="""You translate French to Spanish.
    Provide natural, idiomatic translations.
    Only output the translation, nothing else.""",
    llm_config={"config_list": config_list}
)

# Back-translate for verification
es_to_en = AssistantAgent(
    name="es_to_en",
    system_message="""You translate Spanish back to English.
    Provide natural translations.
    Only output the translation, nothing else.""",
    llm_config={"config_list": config_list}
)

user = UserProxyAgent(name="user", human_input_mode="NEVER")

# Original
original = "Hello, how are you today?"
print(f"Original: {original}")

# Translate EN -> FR
user.initiate_chat(en_to_fr, message=original)
french = en_to_fr.last_message()["content"]
print(f"French: {french}")

# Translate FR -> ES
user.initiate_chat(fr_to_es, message=french)
spanish = fr_to_es.last_message()["content"]
print(f"Spanish: {spanish}")

# Verify back-translation
user.initiate_chat(es_to_en, message=spanish)
back_to_en = es_to_en.last_message()["content"]
print(f"Back to English: {back_to_en}")
```

---

## Exercise 3: Code Review Workflow

### Task
Create automated code review pipeline.

```python
from autogen import AssistantAgent, UserProxyAgent

# Code writer
writer = AssistantAgent(
    name="writer",
    system_message="""Write Python code that solves the given problem.
    Include docstrings and comments.
    Follow PEP 8 style guide.""",
    llm_config={"config_list": config_list}
)

# Linter
linter = AssistantAgent(
    name="linter",
    system_message="""You are a Python linter.
    Check code for:
    - Syntax errors
    - Style issues (PEP 8)
    - Potential bugs
    - Security issues
    
    List issues found, if any.""",
    llm_config={"config_list": config_list}
)

# Security checker
security = AssistantAgent(
    name="security",
    system_message="""You check Python code for security issues.
    Look for:
    - SQL injection vulnerabilities
    - Command injection
    - Hardcoded secrets
    - Unsafe imports
    
    Report any issues found.""",
    llm_config={"config_list": config_list}
)

# Optimizer
optimizer = AssistantAgent(
    name="optimizer",
    system_message="""You optimize Python code.
    Look for:
    - Performance improvements
    - Memory efficiency
    - Better algorithms
    
    Provide optimized version with explanations.""",
    llm_config={"config_list": config_list}
)

user = UserProxyAgent(name="user", human_input_mode="NEVER")

# Step 1: Write code
user.initiate_chat(writer, message="Write a function to find the factorial of a number.")
code = writer.last_message()["content"]

# Step 2: Lint
user.initiate_chat(linter, message=f"Review this code:\n{code}")
lint_result = linter.last_message()["content"]

# Step 3: Security check
user.initiate_chat(security, message=f"Check for security issues:\n{code}")
security_result = security.last_message()["content"]

# Step 4: Optimize
user.initiate_chat(optimizer, message=f"Optimize this code:\n{code}")
optimized = optimizer.last_message()["content"]

print("=== Code Review Complete ===")
print(f"Issues found: {len(linter.last_message())}")
```

---

## Exercise 4: Research Assistant

### Task
Build multi-step research workflow.

```python
from autogen import AssistantAgent, UserProxyAgent

# Topic identifier
identifier = AssistantAgent(
    name="identifier",
    system_message="""Identify the main topic and subtopics.
    Break down complex topics into manageable parts.
    List key areas to research.""",
    llm_config={"config_list": config_list}
)

# Researcher
researcher = AssistantAgent(
    name="researcher",
    system_message="""Research the given topic thoroughly.
    Provide detailed information with examples.
    Cite sources when possible.""",
    llm_config={"config_list": config_list}
)

# Synthesizer
synthesizer = AssistantAgent(
    name="synthesizer",
    system_message="""Combine multiple sources of information.
    Create a coherent summary.
    Highlight key findings and insights.""",
    llm_config={"config_list": config_list}
)

user = UserProxyAgent(name="user", human_input_mode="NEVER")

topic = "Impact of AI on employment"

# Identify subtopics
user.initiate_chat(identifier, message=topic)
subtopics = identifier.last_message()["content"]

# Research each subtopic
user.initiate_chat(researcher, message=subtopics)
research = researcher.last_message()["content"]

# Synthesize
user.initiate_chat(synthesizer, message=research)
final_report = synthesizer.last_message()["content"]

print(final_report)
```

---

## Exercise 5: Interview Simulation

```python
from autogen import AssistantAgent, UserProxyAgent

# Interviewer
interviewer = AssistantAgent(
    name="interviewer",
    system_message="""You conduct professional job interviews.
    Ask relevant questions.
    Probe deeper into answers.
    Evaluate responses fairly.""",
    llm_config={"config_list": config_list}
)

# Candidate
candidate = AssistantAgent(
    name="candidate",
    system_message="""You are a job candidate.
    Answer questions professionally.
    Provide specific examples.
    Be honest about experience level.""",
    llm_config={"config_list": config_list}
)

user = UserProxyAgent(name="user", human_input_mode="NEVER")

# Start interview
user.initiate_chat(interviewer, message="Tell me about your experience with Python.")
```

---

## Complete Example: Customer Support Pipeline

```python
from autogen import AssistantAgent, UserProxyAgent

# Triage agent
triage = AssistantAgent(
    name="triage",
    system_message="""Classify customer issues into categories:
    - billing
    - technical
    - general
    
    Also determine urgency:
    - low: general questions
    - medium: non-critical issues  
    - high: critical issues/blockers
    
    Output: category, urgency""",
    llm_config={"config_list": config_list}
)

# Technical support
tech_support = AssistantAgent(
    name="tech_support",
    system_message="""You provide technical support.
    Ask clarifying questions.
    Provide step-by-step solutions.
    Escalate if needed.""",
    llm_config={"config_list": config_list}
)

# Billing
billing = AssistantAgent(
    name="billing",
    system_message="""You handle billing inquiries.
    Be helpful and patient.
    Know pricing, refunds, subscriptions.""",
    llm_config={"config_list": config_list}
)

# General
general = AssistantAgent(
    name="general",
    system_message="""You handle general questions.
    Be friendly and helpful.
    Provide accurate information.""",
    llm_config={"config_list": config_list}
)

user = UserProxyAgent(name="user", human_input_mode="NEVER")

# Incoming ticket
ticket = "I can't log into my account and I need to process an urgent order!"

# Triage
user.initiate_chat(triage, message=ticket)
classification = triage.last_message()["content"]
print(f"Classified as: {classification}")

# Route to appropriate agent
if "technical" in classification.lower():
    user.initiate_chat(tech_support, message=ticket)
elif "billing" in classification.lower():
    user.initiate_chat(billing, message=ticket)
else:
    user.initiate_chat(general, message=ticket)
```
