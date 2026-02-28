#!/usr/bin/env python3
"""
Lab 1: Configure DeepSeek
==========================

This script configures and tests DeepSeek as your LLM provider.

Prerequisites:
- DeepSeek account: https://platform.deepseek.com
- API key added to .env file

Run:
    python 03_configure_deepseek.py
"""

import os
import sys
from dotenv import load_dotenv
from autogen import AssistantAgent

# Load environment
load_dotenv()

def check_api_key():
    """Check if DeepSeek API key is configured."""
    print("[1] Checking API key...")
    
    api_key = os.getenv("DEEPSEEK_API_KEY")
    
    if not api_key:
        print("    ✗ DEEPSEEK_API_KEY not found!")
        print("\n    Get your API key:")
        print("    1. Go to https://platform.deepseek.com")
        print("    2. Sign up / Sign in")
        print("    3. Create an API key")
        print("    4. Add to .env: DEEPSEEK_API_KEY=your_key")
        return False
    
    # Mask most of the key for display
    masked = api_key[:8] + "..." + api_key[-4:] if len(api_key) > 12 else "***"
    print(f"    ✓ API key found: {masked}")
    return True


def test_connection():
    """Test DeepSeek connection."""
    print("\n[2] Testing DeepSeek connection...")
    
    api_key = os.getenv("DEEPSEEK_API_KEY")
    model = "deepseek-chat"
    base_url = "https://api.deepseek.com/v1"
    
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
            messages=[{"role": "user", "content": "Say 'Hello from DeepSeek!' in exactly those words."}]
        )
        
        print(f"    ✓ Connected successfully!")
        print(f"    Response: {response}")
        return True
        
    except Exception as e:
        error = str(e)
        print(f"    ✗ Error: {error[:100]}")
        
        if "authentication" in error.lower() or "401" in error:
            print("    → Invalid API key. Check your DeepSeek dashboard.")
        elif "rate limit" in error.lower():
            print("    → Rate limit exceeded. Wait and try again.")
        elif "insufficient" in error.lower():
            print("    → No credits left. Add more to your account.")
        
        return False


def main():
    print("=" * 60)
    print("Lab 1: DeepSeek Configuration")
    print("=" * 60)
    print()
    
    if not check_api_key():
        sys.exit(1)
    
    if not test_connection():
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("✓ DeepSeek configured successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
