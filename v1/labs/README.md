# Microsoft AutoGen: The Complete Course - Labs Edition
## Build Multi-Agent AI Systems with Microsoft's Open-Source Framework

---

## Course Overview

**Microsoft AutoGen** is an open-source framework that enables developers to build applications powered by multiple AI agents that can communicate and collaborate to solve complex tasks.

This **Labs Edition** contains hands-on exercises with complete, runnable code for each module.

**What you'll build:**
- ✓ A code assistant multi-agent system
- ✓ A research team of collaborating agents
- ✓ A human-in-the-loop workflow
- ✓ Production-ready agent patterns

---

## Prerequisites

Before starting the labs, ensure you have:

1. **Python 3.8+** installed
2. **OpenAI API Key** (or compatible endpoint like Azure OpenAI)
3. Basic understanding of Python and LLMs

---

## Lab Structure

| Lab | Topic | Skills Learned |
|-----|-------|----------------|
| Lab 1 | Hello Autogen | Installation, environment setup, first agent |
| Lab 2 | Agent Conversations | AssistantAgent, UserProxyAgent, initiate_chat |
| Lab 3 | Tools & Functions | Function calling, code execution, custom tools |
| Lab 4 | GroupChat | Multiple agents, speaker selection, group communication |
| Lab 5 | Human-in-the-Loop | Human input modes, approval workflows |
| Lab 6 | Real-World Apps | Code review system, research assistant, data pipeline |
| Lab 7 | Production Patterns | Error handling, state management, async support |

---

## Quick Start

```bash
# Clone or navigate to course directory
cd ms-autogen-course

# Install dependencies
pip install pyautogen python-dotenv

# Set your API key
export OPENAI_API_KEY="your-api-key-here"

# Run any lab
cd Lab1_Hello_Autogen
python lab_solution.py
```

---

## Course Modules

### Module 1: Introduction to AutoGen
- What is Microsoft AutoGen?
- Why Multi-Agent Systems?
- AutoGen Architecture Overview

### Module 2: Setting Up Your Environment
- Installation
- Configuration
- Quick Verification

### Module 3: Core Concepts
- The Agent Base Class
- Conversations
- Messages
- LLM Configuration

### Module 4: Building Your First AutoGen Application
- A Simple Two-Agent Conversation
- Understanding the Flow

### Module 5: Working with Different Agent Types
- AssistantAgent - The AI Worker
- UserProxyAgent - The Human Interface
- GroupChat - Multiple Agents
- Custom Agent Registration

### Module 6: Tools and Function Calling
- Defining Functions
- Code Execution
- Complete Tool-Using Example

### Module 7: Advanced Conversation Patterns
- Nested Chats
- Sequential Chats
- Speaker Selection in GroupChat
- Conditional Responses

### Module 8: Human-in-the-Loop Patterns
- Always Ask for Human Input
- Terminate with Human Approval
- Selective Human Intervention
- Example: Human Approval Workflow

### Module 9: Real-World Use Cases
- Code Review System
- Research Assistant Team
- Data Analysis Pipeline

### Module 10: Best Practices and Troubleshooting
- Configuration Best Practices
- Common Issues and Solutions
- Security Considerations
- Performance Optimization
- Testing AutoGen Applications

### Module 11: Production Deployment Patterns
- Error Handling
- State Management
- Async Support

---

## Resources

- **AutoGen GitHub**: https://github.com/microsoft/autogen
- **Documentation**: https://microsoft.github.io/autogen/
- **Discord Community**: https://discord.gg/pAbnFJrkgjw

---

*Course created by Steve Robinson - Alpaca Mango*
*Last Updated: 2024*
