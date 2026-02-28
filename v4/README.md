# Microsoft AutoGen: The Complete Course v4
## Building Production-Ready Multi-Agent AI Systems

---

**Version**: 4.0 (Comprehensive Edition)  
**Author**: Alpax Prime 🦙  
**Prerequisites**: Python 3.10+, Basic understanding of LLMs

---

## Course Overview

This comprehensive course takes you from AutoGen beginner to production-ready multi-agent developer. Version 4 is completely rewritten with:

- **50+ Working Code Examples** - Copy, paste, run
- **7 Complete Labs** - Each with 5+ exercises
- **3 Provider Deep-Dives** - Ollama, DeepSeek, MiniMax
- **4 Full Projects** - Real-world applications
- **Troubleshooting Guides** - Common issues solved

---

## Table of Contents

1. [Introduction](#introduction)
2. [Lab 1: Environment Setup](#lab-1)
3. [Lab 2: Single Agent Fundamentals](#lab-2)
4. [Lab 3: Two-Agent Conversations](#lab-3)
5. [Lab 4: Tools & Function Calling](#lab-4)
6. [Lab 5: Group Chat](#lab-5)
7. [Lab 6: Human-in-the-Loop](#lab-6)
8. [Lab 7: Production Patterns](#lab-7)
9. [Projects](#projects)
10. [Provider Guides](#providers)

---

## What is AutoGen?

Microsoft AutoGen is an open-source framework for building applications powered by multiple AI agents that can communicate and collaborate.

### Why Multi-Agent Systems?

Single LLM calls have limitations:
- Limited context windows
- No persistent memory
- Difficulty with complex, multi-step tasks

Multi-agent architectures solve these by:
- **Dividing labor** - Each agent specializes
- **Parallel processing** - Agents work simultaneously
- **Robustness** - One agent's failure doesn't halt everything

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                     Your Application                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────┐    ┌──────────────┐    ┌─────────────┐ │
│  │  Assistant   │    │  UserProxy   │    │   GroupChat │ │
│  │   Agent      │    │    Agent     │    │   Manager   │ │
│  └──────┬───────┘    └──────┬───────┘    └──────┬──────┘ │
│         │                    │                    │         │
│         └────────────────────┼────────────────────┘         │
│                              │                              │
│                    ┌─────────▼─────────┐                   │
│                    │   LangGraph      │                   │
│                    │   Checkpointer   │                   │
│                    └─────────┬─────────┘                   │
│                              │                              │
│         ┌────────────────────┼────────────────────┐        │
│         │                    │                    │        │
│  ┌──────▼──────┐    ┌──────▼───────┐    ┌──────▼──────┐│
│  │   Ollama     │    │   DeepSeek   │    │   MiniMax   ││
│  │  (Local)     │    │   (Cloud)    │    │   (Cloud)   ││
│  └──────────────┘    └──────────────┘    └─────────────┘│
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Lab Structure

Each lab follows this structure:

1. **Concept Overview** - What you'll learn
2. **Step-by-Step Guide** - Detailed instructions
3. **Code Examples** - Working code to copy
4. **Exercises** - Practice problems
5. **Solutions** - Complete answers
6. **Common Issues** - Troubleshooting

---

## Quick Start

```bash
# 1. Clone or download this course
cd alpax-adv-ag-v4

# 2. Install dependencies
pip install pyautogen python-dotenv

# 3. Configure your .env file
cp .env.example .env
# Edit .env with your API keys

# 4. Start with Lab 1
cd labs/Lab1
python 01_verify_installation.py
```

---

## Provider Comparison

| Provider | Type | Context | Best For | Cost |
|----------|------|---------|----------|------|
| **Ollama** | Local | 4K-128K | Development, Privacy | Free |
| **DeepSeek** | Cloud | 64K | Production, Coding | $0.14/1M |
| **MiniMax** | Cloud | 200K | Long Documents | $0.10/1M |

---

## Course Progression

```
Week 1: Lab 1-2   (Setup → Single Agent)
Week 2: Lab 3-4   (Conversations → Tools)
Week 3: Lab 5-6   (Group Chat → Human-in-Loop)
Week 4: Lab 7     (Production Patterns)
Week 5: Projects   (Apply what you learned)
```

---

## What's Inside

### Labs (7 complete)
- 50+ code examples
- 35+ exercises with solutions
- Detailed explanations

### Projects (4 full applications)
- Research Assistant
- Code Review System
- Customer Support Bot
- Multi-Agent Collaboration Platform

### Provider Guides (3)
- Ollama setup & optimization
- DeepSeek integration
- MiniMax for long context

---

## Requirements

### Software
- Python 3.10 or higher
- pip or poetry
- Git (optional)

### API Keys (at least one)
- DeepSeek (free sign-up)
- MiniMax (free sign-up)  
- OpenAI (paid)
- Anthropic (paid)

### Hardware (for Ollama)
- 8GB RAM minimum
- 20GB disk space

---

## Support

- Check the troubleshooting section in each lab
- Review common issues in Lab 7
- Examine the provider guides for specific problems

---

## Next Steps

Ready? Start with [Lab 1: Environment Setup](labs/Lab1/README.md)

---

*Built with Microsoft AutoGen & LangGraph*
*Part of the Alpax Prime Training Series*
