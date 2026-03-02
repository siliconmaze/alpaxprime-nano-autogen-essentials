= AutoGen Basics - Lab Course Outline

== Course Overview

This lab-based course provides a comprehensive introduction to Microsoft's AutoGen framework, enabling students to build sophisticated multi-agent AI applications. Students will progress from basic concepts to building production-ready multi-agent systems through hands-on labs.

**Prerequisites:**
- Basic Python programming knowledge
- Familiarity with LLMs (OpenAI, Anthropic, or local models)
- Understanding of API concepts

**Target Audience:**
- Developers looking to build AI agent applications
- DevOps engineers automating workflows with AI
- Technical professionals exploring multi-agent systems

---

== Chapter Structure

=== 1. Introduction to Multi-Agent AI Systems
- What are multi-agent systems?
- AutoGen framework overview
- Use cases and applications
- Architecture and components

=== 2. Setting Up the Development Environment
- Python environment configuration
- Installing AutoGen and dependencies
- API key configuration
- Local model options (Ollama, LM Studio)

=== 3. AutoGen Core Concepts
- Agent types and hierarchies
- Conversation patterns
- Message passing between agents
- Group chat vs. sequential conversations

=== 4. Building Your First Agent
- Creating a simple assistant agent
- Defining agent personalities
- Basic message handling
- Testing with simple prompts

=== 5. Multi-Agent Conversations
- Two-agent conversations
- Setting up conversation flow
- Role-based agent interactions
- Handling responses and context

=== 6. Group Chat Configuration
- GroupChatManager overview
- Speaker selection strategies
- Maximum rounds and termination
- Speaker transition rules

=== 7. Tool Use and Function Calling
- Registering custom functions
- Tool execution flow
- Building agents with capabilities
- Real-world tool integration examples

=== 8. Advanced Conversation Patterns
- Sequential message passing
- Nested chats
- Selective forwarding
- Custom speaker selection

=== 9. Human-in-the-Loop Patterns
- Human intervention modes
- Auto-reply vs. manual approval
- Interactive agent scenarios
- Use cases for human involvement

=== 10. Building Production Applications
- Error handling and recovery
- Logging and monitoring
- Scaling considerations
- Best practices

---

== Lab Guide (18 Labs)

| Lab | Topic | Description |
|-----|-------|-------------|
| 1 | Environment Setup | Install Python, AutoGen, and configure API keys |
| 2 | Your First AutoGen Agent | Create and run a basic assistant agent |
| 3 | Two-Agent Conversation | Set up a conversation between two agents |
| 4 | Agent with Custom Personality | Define agent roles and behaviors |
| 5 | Introduction to Group Chat | Create a multi-agent group conversation |
| 6 | Registering Custom Tools | Add function calling to agents |
| 7 | Building a Research Assistant | Create an agent that searches and summarizes |
| 8 | Coding Agent with Execution | Build an agent that writes and runs code |
| 9 | Sequential Chat Patterns | Implement multi-step workflows |
| 10 | Nested Chat Architectures | Build hierarchical agent conversations |
| 11 | Human-in-the-Loop Patterns | Add human approval to agent workflows |
| 12 | Tool Composition | Chain multiple tools in agent workflows |
| 13 | Conversational Flow Control | Custom speaker selection and routing |
| 14 | Error Handling in Agents | Graceful failure and recovery strategies |
| 15 | Building a Chatbot | Create a customer service agent |
| 16 | Multi-Tool Research Agent | Combine search, storage, and analysis |
| 17 | Capstone - AI Meeting Assistant | Build a complete meeting summarization system |
| 18 | Capstone Solution | Fully worked solution for the capstone |

---

== Lab Detail Specifications

=== Lab 1: Environment Setup
**Objectives:**
- Install Python 3.10+ and pip
- Install autogen package
- Configure OpenAI/Anthropic API keys
- Verify installation with test script

**Steps:**
1. Check Python version
2. Create virtual environment
3. Install autogen and dependencies
4. Set up environment variables
5. Test basic agent creation

---

=== Lab 2: Your First AutoGen Agent
**Objectives:**
- Create an AssistantAgent instance
- Configure the agent with model
- Send messages and receive responses
- Understand agent state

**Steps:**
1. Import AutoGen classes
2. Configure LLM settings
3. Create AssistantAgent
4. Initiate conversation
5. Process response

---

### Lab 3: Two-Agent Conversation
**Objectives:**
- Create two distinct agents
- Set up conversation flow
- Exchange messages between agents
- Observe role-based responses

---

### Lab 4: Agent with Custom Personality
**Objectives:**
- Define system message for personality
- Configure agent behavior
- Test different personas
- Handle context appropriately

---

### Lab 5: Introduction to Group Chat
**Objectives:**
- Create GroupChat
- Add multiple agents
- Configure GroupChatManager
- Execute group conversation

---

### Lab 6: Registering Custom Tools
**Objectives:**
- Define Python functions as tools
- Register tools with agent
- Execute tool calls
- Process tool results

---

### Lab 7: Building a Research Assistant
**Objectives:**
- Combine web search with summarization
- Create multi-step workflow
- Aggregate results
- Present formatted output

---

### Lab 8: Coding Agent with Execution
**Objectives:**
- Create agent that generates code
- Implement code execution
- Handle output and errors
- Build REPL-style interaction

---

### Lab 9: Sequential Chat Patterns
**Objectives:**
- Chain conversations sequentially
- Pass context between agents
- Build multi-step pipelines
- Handle intermediate results

---

### Lab 10: Nested Chat Architectures
**Objectives:**
- Create parent-child agent relationships
- Delegate tasks to sub-agents
- Aggregate nested results
- Manage complexity

---

### Lab 11: Human-in-the-Loop Patterns
**Objectives:**
- Configure human intervention mode
- Set up approval workflows
- Test manual override
- Build interactive systems

---

### Lab 12: Tool Composition
**Objectives:**
- Chain multiple tools
- Create tool pipelines
- Handle dependent operations
- Build composite workflows

---

### Lab 13: Conversational Flow Control
**Objectives:**
- Implement custom speaker selection
- Create routing logic
- Control conversation flow
- Add conditional transitions

---

### Lab 14: Error Handling in Agents
**Objectives:**
- Handle API failures gracefully
- Implement retry logic
- Add fallback strategies
- Log errors appropriately

---

### Lab 15: Building a Chatbot
**Objectives:**
- Create customer service agent
- Handle FAQs
- Route complex queries
- Maintain conversation history

---

### Lab 16: Multi-Tool Research Agent
**Objectives:**
- Combine search, storage, analysis tools
- Create comprehensive research workflow
- Generate reports
- Persist results

---

### Lab 17: Capstone - AI Meeting Assistant
**Objectives:**
- Build complete application
- Integrate multiple agents
- Handle real-world scenarios
- Production-ready code

---

### Lab 18: Capstone Solution
**Objectives:**
- Review complete solution
- Understand design decisions
- Learn best practices
- Extend the application

---

== Supporting Materials

=== Instructor Resources
- Solution guides for each lab
- Common issues and troubleshooting
- Discussion questions
- Assessment criteria

=== Setup Requirements
- Python 3.10+
- OpenAI API key (or Anthropic/Ollama)
- 8GB RAM minimum
- Internet connection

---

== Course Progression

```
Week 1: Labs 1-4  (Environment → First Agent)
Week 2: Labs 5-8  (Group Chat → Code Execution)
Week 3: Labs 9-12 (Advanced Patterns → Tool Composition)
Week 4: Labs 13-16 (Flow Control → Multi-Tool Agent)
Week 5: Labs 17-18 (Capstone)
```

---

== Technical Notes

- All labs use Python 3.10+
- Compatible with AutoGen 0.2+
- Supports OpenAI, Anthropic, Azure OpenAI, local models
- Labs are platform-agnostic (macOS, Linux, Windows WSL)

---

== Assessment

- Completion of all 18 labs
- Capstone project submission
- Code review for best practices

---

## Summary

This course provides a hands-on, lab-driven approach to learning AutoGen. Students build practical skills progressively, starting from basic agent creation to building complete multi-agent applications. Upon completion, students will be equipped to develop production-ready AI agent systems using Microsoft's AutoGen framework.
