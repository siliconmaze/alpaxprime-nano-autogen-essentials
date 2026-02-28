# Alpax Advanced AutoGen v1 (alpax-adv-ag-v1)

Multi-provider AutoGen workshop - comparing Ollama, DeepSeek, and MiniMax

## Overview

This repository contains walkthroughs for Microsoft's AutoGen framework using three different LLM providers:
- **Ollama** - Local, privacy-focused (qwen2.5-coder:7b)
- **DeepSeek** - Cloud API (deepseek-chat)
- **MiniMax** - Cloud API (MiniMax-Text-01)

## Labs Covered

1. Lab1: Hello AutoGen - Basic agent setup
2. Lab2: Agent Conversations - Two-agent patterns
3. Lab3: Tools & Functions - Function calling
4. Lab4: GroupChat - Multi-agent groups
5. Lab5: Human-in-the-Loop - Interactive workflows
6. Lab6: Real-World Apps - Production patterns
7. Lab7: Production Patterns - Scaling & monitoring

## Quick Start

```bash
# Clone and setup
cd alpax-adv-ag-v1
pip install pyautogen python-dotenv

# Configure your .env file with API keys
cp .env.example .env
```

## Provider Configuration

Each provider has its own configuration - see individual walkthrough folders.
