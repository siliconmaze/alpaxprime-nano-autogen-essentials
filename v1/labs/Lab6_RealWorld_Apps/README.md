# Lab 6: Real-World Applications

## Objective
Build complete, production-ready multi-agent systems for real-world use cases.

## Estimated Time
45 minutes

---

## Application 1: Code Review System

Create `code_review_system.py`:

```python
"""Lab 6a: Multi-Agent Code Review System"""
import os
from dotenv import load_dotenv
import autogen
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

config_list = [{"model": "gpt-4", "api_key": api_key}]

# Code Submitter - submits code for review
submitter = UserProxyAgent(
    name="submitter",
    human_input_mode="NEVER",
    code_execution_config={"use_docker": False}
)

# Code Reviewer - reviews code for issues
reviewer = AssistantAgent(
    name="reviewer",
    llm_config={"config_list": config_list},
    system_message="""You are an expert code reviewer.
    Review the submitted code for:
    1. Bugs and errors
    2. Security vulnerabilities
    3. Code quality issues
    4. Performance improvements
    
    Provide specific feedback with line numbers if possible."""
)

# Security Expert - specifically checks for security issues
security_expert = AssistantAgent(
    name="security_expert",
    llm_config={"config_list": config_list},
    system_message="""You are a security expert.
    Review code for security vulnerabilities:
    1. SQL injection
    2. XSS attacks
    3. Authentication issues
    4. Data exposure
    5. Common OWASP Top 10 issues"""
)

# Create group chat
groupchat = GroupChat(
    agents=[submitter, reviewer, security_expert],
    messages=[],
    max_round=10
)

manager = GroupChatManager(
    groupchat=groupchat,
    llm_config={"config_list": config_list}
)

# Code to review
code_to_review = '''
def get_user(user_id, request):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    # Execute query...
    return user_data

def display_user_name(user_id, request):
    user = get_user(user_id, request)
    return f"<h1>Welcome {user['name']}</h1>"
'''

submitter.initiate_chat(
    manager,
    message=f"Please review this code for issues:\n\n{code_to_review}"
)
```

---

## Application 2: Research Assistant Team

Create `research_assistant.py`:

```python
"""Lab 6b: Research Assistant Team"""
import os
from dotenv import load_dotenv
import autogen
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

config_list = [{"model": "gpt-4", "api_key": api_key}]

# Topic Finder - identifies key topics
topic_finder = AssistantAgent(
    name="topic_finder",
    llm_config={"config_list": config_list},
    system_message="""You identify key topics and subtopics for research.
    Break down complex topics into manageable areas to investigate."""
)

# Researcher - gathers information on topics
researcher = AssistantAgent(
    name="researcher",
    llm_config={"config_list": config_list},
    system_message="""You research topics thoroughly.
    Find recent information, statistics, and key insights.
    Always cite your sources."""
)

# Synthesizer - combines findings into coherent summary
synthesizer = AssistantAgent(
    name="synthesizer",
    llm_config={"config_list": config_list},
    system_message="""You synthesize research into clear, actionable summaries.
    Organize findings logically with clear headings."""
)

# User
user = UserProxyAgent(
    name="user",
    human_input_mode="NEVER"
)

# Group chat
groupchat = GroupChat(
    agents=[user, topic_finder, researcher, synthesizer],
    messages=[],
    max_round=15
)

manager = GroupChatManager(
    groupchat=groupchat,
    llm_config={"config_list": config_list}
)

user.initiate_chat(
    manager,
    message="Research the impact of AI on software development jobs. Provide a comprehensive summary."
)
```

---

## Application 3: Data Analysis Pipeline

Create `data_analysis.py`:

```python
"""Lab 6c: Data Analysis Pipeline"""
import os
from dotenv import load_dotenv
import autogen
from autogen import AssistantAgent, UserProxyAgent

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

config_list = [{"model": "gpt-4", "api_key": api_key}]

# Data Engineer - prepares and transforms data
data_engineer = AssistantAgent(
    name="data_engineer",
    llm_config={"config_list": config_list},
    system_message="""You are a data engineer.
    Write Python code to:
    1. Load and clean data
    2. Transform and aggregate
    3. Handle missing values
    Execute the code and show results."""
)

# Data Analyst - performs analysis
data_analyst = AssistantAgent(
    name="data_analyst",
    llm_config={"config_list": config_list},
    system_message="""You are a data analyst.
    Analyze data to find:
    1. Trends and patterns
    2. Correlations
    3. Key insights
    Provide statistical summaries."""
)

# Data Visualizer - creates visualizations
visualizer = AssistantAgent(
    name="visualizer",
    llm_config={"config_list": config_list},
    system_message="""You create data visualizations.
    Suggest appropriate chart types and create them using matplotlib/seaborn."""
)

# Executor
executor = UserProxyAgent(
    name="executor",
    human_input_mode="NEVER",
    code_execution_config={"work_dir": "analysis_output", "use_docker": False}
)

# Sample data analysis request
analysis_request = """
Analyze this sales data:
```
import pandas as pd
data = {
    'month': ['Jan','Feb','Mar','Apr','May','Jun'],
    'sales': [12000, 15000, 11000, 18000, 22000, 21000],
    'expenses': [8000, 9000, 8500, 10000, 11000, 10500],
    'customers': [120, 150, 130, 180, 220, 210]
}
df = pd.DataFrame(data)
```
Calculate monthly profit, find best month, and identify trends.
"""

executor.initiate_chat(
    data_engineer,
    message=analysis_request
)
```

---

## Application 4: Customer Support System

Create `support_system.py`:

```python
"""Lab 6d: Customer Support System with Routing"""
import os
from dotenv import load_dotenv
import autogen
from autogen import AssistantAgent, UserProxyAgent

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

config_list = [{"model": "gpt-4", "api_key": api_key}]

# Triage Agent - routes to appropriate handler
triage = AssistantAgent(
    name="triage",
    llm_config={"config_list": config_list},
    system_message="""You are a triage agent.
    Classify customer issues into categories:
    - billing (payment, invoices, refunds)
    - technical (bugs, errors, setup)
    - general (questions, information)
    
    Respond with only the category."""
)

# Billing Specialist
billing = AssistantAgent(
    name="billing_specialist",
    llm_config={"config_list": config_list},
    system_message="""You are a billing specialist.
    Help with payment issues, invoices, refunds, and subscriptions."""
)

# Technical Support
tech_support = AssistantAgent(
    name="tech_support",
    llm_config={"config_list": config_list},
    system_message="""You are technical support.
    Help with technical issues, bugs, setup, and troubleshooting."""
)

# General Info
info_agent = AssistantAgent(
    name="info_agent",
    llm_config={"config_list": config_list},
    system_message="""You provide general information.
    Answer questions about products, services, and policies."""
)

# Customer
customer = UserProxyAgent(
    name="customer",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=5
)

# Function to route based on triage
def route_to_specialist(category):
    specialists = {
        "billing": billing,
        "technical": tech_support,
        "general": info_agent
    }
    return specialists.get(category.lower(), info_agent)

# Example conversation
customer_message = "I was charged twice for my subscription this month!"

# First, get category
customer.initiate_chat(triage, message=customer_message)

# Then route to specialist (in real app, automate this)
print(f"\n→ Routing to billing specialist...\n")

customer.initiate_chat(
    billing,
    message="The customer was charged twice. Help resolve this issue."
)
```

---

## What You Learned

✓ Building a code review system with multiple reviewers
✓ Creating a research assistant team
✓ Data analysis pipeline with multiple roles
✓ Customer support system with intelligent routing

---

## Next Step

Proceed to **Lab 7: Production Patterns** for deployment best practices!
