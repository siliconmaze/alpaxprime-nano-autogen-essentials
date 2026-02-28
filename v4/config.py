"""
Configuration helper for AutoGen Course v4

Usage:
    from config import get_config
    
    # Get default config (first available provider)
    config_list = get_config()
    
    # Or specify provider
    config_list = get_config("ollama")
    config_list = get_config("deepseek")
    config_list = get_config("minimax")
"""

import os
from dotenv import load_dotenv

load_dotenv()


def get_ollama_config(model: str = "qwen2.5-coder:7b"):
    """Get Ollama configuration."""
    return [{
        "model": model,
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama",
        "api_type": "openai"
    }]


def get_deepseek_config(model: str = "deepseek-chat"):
    """Get DeepSeek configuration."""
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError("DEEPSEEK_API_KEY not set in .env")
    return [{
        "model": model,
        "base_url": "https://api.deepseek.com/v1",
        "api_key": api_key
    }]


def get_minimax_config(model: str = "MiniMax-Text-01"):
    """Get MiniMax configuration."""
    api_key = os.getenv("MINIMAX_API_KEY")
    if not api_key:
        raise ValueError("MINIMAX_API_KEY not set in .env")
    return [{
        "model": model,
        "base_url": "https://api.minimax.io/anthropic/v1",
        "api_key": api_key
    }]


def get_openai_config(model: str = "gpt-4"):
    """Get OpenAI configuration."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not set in .env")
    return [{
        "model": model,
        "base_url": "https://api.openai.com/v1",
        "api_key": api_key
    }]


def get_anthropic_config(model: str = "claude-3-sonnet-20240229"):
    """Get Anthropic configuration."""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY not set in .env")
    return [{
        "model": model,
        "base_url": "https://api.anthropic.com",
        "api_key": api_key
    }]


def get_config(provider: str = "auto"):
    """
    Get configuration for specified provider.
    
    Args:
        provider: "ollama", "deepseek", "minimax", "openai", "anthropic", or "auto"
    
    Returns:
        config_list for AutoGen
    
    Raises:
        ValueError: If provider is unknown or not configured
    """
    if provider == "auto":
        # Try each provider in order of preference
        for p in ["deepseek", "minimax", "openai", "anthropic", "ollama"]:
            try:
                return get_config(p)
            except (ValueError, Exception):
                continue
        raise ValueError("No valid provider found. Configure at least one provider in .env")
    
    providers = {
        "ollama": get_ollama_config,
        "deepseek": get_deepseek_config,
        "minimax": get_minimax_config,
        "openai": get_openai_config,
        "anthropic": get_anthropic_config
    }
    
    if provider not in providers:
        raise ValueError(f"Unknown provider: {provider}. Use: {', '.join(providers.keys())}")
    
    return providers[provider]()


# Convenience function for quick testing
if __name__ == "__main__":
    try:
        config = get_config()
        print(f"✓ Using provider: {config[0]['model']}")
    except ValueError as e:
        print(f"✗ {e}")
