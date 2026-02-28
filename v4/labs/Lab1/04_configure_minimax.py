#!/usr/bin/env python3
"""
Lab 1: Configure MiniMax
=========================

This script configures and tests MiniMax as your LLM provider.

Prerequisites:
- MiniMax account: https://platform.minimax.io
- API key added to .env file

Run:
    python 04_configure_minimax.py
"""

import os
import sys
from dotenv import load_dotenv
from autogen import AssistantAgent

load_dotenv()

def check_api_key():
    """Check if MiniMax API key is configured."""
    print("[1] Checking API key...")
    
    api_key = os.getenv("MINIMAX_API_KEY")
    
    if not api_key:
        print("    ✗ MINIMAX_API_KEY not found!")
        print("\n    Get your API key:")
        print("    1. Go to https://platform.minimax.io")
        print("    2. Sign up / Sign in")
        print("    3. Create an API key")
        print("    4. Add to .env: MINIMAX_API_KEY=your_key")
        return False
    
    masked = api_key[:8] + "..." + api_key[-4:] if len(api_key) > 12 else "***"
    print(f"    ✓ API key found: {masked}")
    return True


def test_connection():
    """Test MiniMax connection."""
    print("\n[2] Testing MiniMax connection...")
    
    api_key = os.getenv("MINIMAX_API_KEY")
    model = "MiniMax-Text-01"
    base_url = "https://api.minimax.io/anthropic/v1"
    
    config_list = [{
        "model": model,
        "base_url": base_url,
        "api_key": api_key
    }]
    
    try:
        agent = AssistantAgent(
            name="test_agent",
            llm_config={"config_list": config_list}
        )
        
        response = agent.generate_reply(
            messages=[{"role": "user", "content": "Say 'Hello from MiniMax!' in exactly those words."}]
        )
        
        print(f"    ✓ Connected successfully!")
        print(f"    Response: {response}")
        return True
        
    except Exception as e:
        print(f"    ✗ Error: {str(e)[:100]}")
        return False


def main():
    print("=" * 60)
    print("Lab 1: MiniMax Configuration")
    print("=" * 60)
    print()
    
    if not check_api_key():
        sys.exit(1)
    
    if not test_connection():
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("✓ MiniMax configured successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
