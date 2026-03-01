# Microsoft AutoGen: The Complete Course v5
## Building Production-Ready Multi-Agent AI Systems

---

**Version**: 5.0 (Ollama-First Edition)  
**Author**: Alpax Prime 🦙  
**Prerequisites**: Python 3.10+, Basic understanding of LLMs

---

## Course Philosophy: Ollama-First Design

This version is specifically designed to ensure you can complete **all labs without requiring any API keys**. 

- **Default Provider**: Ollama (local, free)
- **Fallback Options**: DeepSeek, MiniMax (for users with API keys)
- **Full Experience**: Every lab works with just Ollama installed

---

## What's New in v5

- ✅ **Ollama-First** - All labs default to Ollama, no API keys required
- ✅ **Expanded Labs** - 10+ exercises per lab with detailed solutions
- ✅ **Real-World Examples** - Production-ready code patterns
- ✅ **Better Error Handling** - Common issues documented
- ✅ **Asset References** - Cheat sheets, quick references, architecture diagrams

---

## Table of Contents

1. [Course Overview](#course-overview)
2. [Lab 1: Environment Setup & Ollama Configuration](#lab-1)
3. [Lab 2: Single Agent Fundamentals](#lab-2)
4. [Lab 3: Two-Agent Conversations](#lab-3)
5. [Lab 4: Tools & Function Calling](#lab-4)
6. [Lab 5: Group Chat & Orchestration](#lab-5)
7. [Lab 6: Human-in-the-Loop Patterns](#lab-6)
8. [Lab 7: Production & Deployment](#lab-7)
9. [Provider Guides](#providers)
10. [Assets & References](#assets)

---

## Why This Course Works Without API Keys

### The Ollama Advantage

```
┌─────────────────────────────────────────────────────────────┐
│                    YOUR COMPUTER                             │
│                                                              │
│   ┌─────────────────────────────────────────────────────┐   │
│   │                   OLLAMA SERVER                     │   │
│   │                  (Local AI Engine)                  │   │
│   │                                                      │   │
│   │   ┌──────────┐  ┌──────────┐  ┌──────────────┐   │   │
│   │   │  Qwen    │  │  Llama   │  │   Mistral    │   │   │
│   │   │ 2.5-Coder│  │    3     │  │    7B        │   │   │
│   │   └──────────┘  └──────────┘  └──────────────┘   │   │
│   │                                                      │   │
│   └─────────────────────────────────────────────────────┘   │
│                              │                               │
│                    ┌─────────▼─────────┐                    │
│                    │   AutoGen Framework │                   │
│                    └─────────────────────┘                   │
│                                                              │
└─────────────────────────────────────────────────────────────┘

✓ No internet required after model download
✓ No API costs
✓ Complete privacy
✓ Full course completion possible
```

---

## Quick Start (5 Minutes)

```bash
# 1. Install Ollama (macOS/Linux/Windows)
# https://ollama.ai/download

# 2. Pull a capable model (one-time)
ollama pull qwen2.5-coder:7b

# 3. Clone/download this course
cd v5

# 4. Run your first agent
cd labs/Lab1
python 01_verify_installation.py
```

---

## Lab Overview

| Lab | Topic | Ollama | API Key Optional |
|-----|-------|--------|------------------|
| 1 | Environment Setup | ✅ Required | ✅ Yes |
| 2 | Single Agent | ✅ Default | ✅ Yes |
| 3 | Two-Agent Chat | ✅ Default | ✅ Yes |
| 4 | Tools & Functions | ✅ Default | ✅ Yes |
| 5 | Group Chat | ✅ Default | ✅ Yes |
| 6 | Human-in-the-Loop | ✅ Default | ✅ Yes |
| 7 | Production Patterns | ✅ Default | ✅ Yes |

---

## Provider Configuration Priority

### For Users WITHOUT API Keys (Recommended Path)
```
1. Ollama (local) ← START HERE
   - Install: ollama.ai
   - Models: qwen2.5-coder, llama3, mistral
```

### For Users WITH API Keys
```
1. Ollama (local) - Development
2. DeepSeek - Production ($0.14/1M tokens)
3. MiniMax - Long Context (200K)
```

---

## Course Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    COURSE STRUCTURE                           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   v5/                                                        │
│   ├── README.md                    (Course Overview)        │
│   ├── labs/                                                 │
│   │   ├── Lab1/                   (Environment Setup)       │
│   │   ├── Lab2/                   (Single Agent)            │
│   │   ├── Lab3/                   (Two-Agent Chat)         │
│   │   ├── Lab4/                   (Tools & Functions)      │
│   │   ├── Lab5/                   (Group Chat)              │
│   │   ├── Lab6/                   (Human-in-the-Loop)       │
│   │   └── Lab7/                   (Production Patterns)    │
│   ├── providers/                   (Provider Setup Guides)  │
│   └── assets/                      (Reference Cards)        │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Each Lab Contains

- 📖 **Concept Overview** - Theory and best practices
- 💻 **5-10 Code Examples** - Working, copy-paste ready
- 🏋️ **Exercises** - Practice problems with increasing difficulty
- ✅ **Solutions** - Complete, explained answers
- 🔧 **Troubleshooting** - Common issues and fixes
- 📊 **Performance Tips** - Optimize for speed/cost

---

## Requirements

### For Full Course (No API Keys)
- Python 3.10+
- Ollama installed
- 8GB RAM (for local models)
- 20GB disk space

### For Enhanced Experience (Optional)
- DeepSeek API key
- MiniMax API key
- OpenAI API key

---

## Support Resources

- **Troubleshooting**: Each lab has a dedicated troubleshooting section
- **Provider Guides**: See `/providers/` folder for detailed setup
- **Assets**: Quick reference cards in `/assets/`

---

## Ready to Start?

Begin with [Lab 1: Environment Setup](labs/Lab1/README.md)

---

*Built with Microsoft AutoGen*
*Part of the Alpax Prime Training Series*
*Version 5.0 - Ollama-First Edition*
