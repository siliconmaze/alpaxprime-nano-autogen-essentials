"""
MiniMax Configuration for AutoGen

Usage:
    from config import get_minimax_config
    config_list = get_minimax_config()
"""

import os
from dotenv import load_dotenv

load_dotenv()

def get_minimax_config(model="MiniMax-Text-01"):
    """Get MiniMax config for AutoGen."""
    api_key = os.getenv("MINIMAX_API_KEY")
    if not api_key:
        raise ValueError("MINIMAX_API_KEY not set")
    
    return [
        {
            "model": model,
            "base_url": "https://api.minimax.io/anthropic/v1",
            "api_key": api_key
        }
    ]
