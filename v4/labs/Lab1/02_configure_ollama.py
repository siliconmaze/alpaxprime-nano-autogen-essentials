#!/usr/bin/env python3
"""
Lab 1: Configure Ollama
=======================

This script configures and tests Ollama as your LLM provider.

Prerequisites:
- Ollama installed: brew install ollama
- Model pulled: ollama pull qwen2.5-coder:7b
- Ollama running: ollama serve

Run:
    python 02_configure_ollama.py
"""

import subprocess
import sys
from autogen import AssistantAgent

# Configuration
MODEL = "qwen2.5-coder:7b"  # Change to "llama3", "mistral", etc.
BASE_URL = "http://localhost:11434/v1"
API_KEY = "ollama"  # Not actually used, but required

def check_ollama():
    """Check if Ollama is installed and running."""
    print("[1] Checking Ollama installation...")
    
    try:
        # Check if ollama command exists
        result = subprocess.run(["which", "ollama"], capture_output=True, text=True)
        if result.returncode != 0:
            print("    ✗ Ollama not found!")
            print("    Install with: brew install ollama")
            return False
        print("    ✓ Ollama is installed")
    except Exception as e:
        print(f"    ✗ Error checking Ollama: {e}")
        return False
    
    # Check if Ollama is running
    try:
        result = subprocess.run(["ollama", "list"], capture_output=True, text=True, timeout=5)
        if result.returncode != 0:
            print("    ✗ Ollama not running!")
            print("    Start with: ollama serve")
            return False
        print("    ✓ Ollama is running")
        print(f"\n    Available models:\n{result.stdout}")
    except subprocess.TimeoutExpired:
        print("    ✗ Ollama not responding")
        print("    Start with: ollama serve")
        return False
    except Exception as e:
        print(f"    ✗ Error: {e}")
        return False
    
    return True


def test_model():
    """Test the specified model."""
    print(f"\n[2] Testing model: {MODEL}")
    
    config_list = [{
        "model": MODEL,
        "base_url": BASE_URL,
        "api_key": API_KEY,
        "api_type": "openai"  # Ollama uses OpenAI-compatible API
    }]
    
    try:
        agent = AssistantAgent(
            name="test_agent",
            llm_config={"config_list": config_list}
        )
        
        response = agent.generate_reply(
            messages=[{"role": "user", "content": "Say 'Hello from Ollama!' in exactly those words."}]
        )
        
        print(f"    ✓ Agent responded!")
        print(f"    Response: {response}")
        return True
        
    except Exception as e:
        print(f"    ✗ Error: {e}")
        return False


def main():
    print("=" * 60)
    print("Lab 1: Ollama Configuration")
    print("=" * 60)
    print()
    
    if not check_ollama():
        print("\n✗ Ollama setup incomplete")
        sys.exit(1)
    
    if not test_model():
        print("\n✗ Model test failed")
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("✓ Ollama configured successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
