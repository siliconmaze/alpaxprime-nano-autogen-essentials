"""
DeepSeek Configuration for AutoGen

Usage:
    from config import get_deepseek_config
    config_list = get_deepseek_config()
"""

import os
from dotenv import load_dotenv

load_dotenv()

def get_deepseek_config(model="deepseek-chat"):
    """Get DeepSeek config for AutoGen."""
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError("DEEPSEEK_API_KEY not set")
    
    return [
        {
            "model": model,
            "base_url": "https://api.deepseek.com/v1",
            "api_key": api_key
        }
    ]
