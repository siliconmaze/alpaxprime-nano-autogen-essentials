"""
AutoGen v5 Configuration Module
Ollama-first design - works without API keys
"""
import os
from dotenv import load_dotenv

load_dotenv()

# ============================================
# OLLAMA CONFIG (Primary - No API Key Required)
# ============================================
def get_ollama_config(model: str = None):
    """
    Get Ollama configuration - works without API keys!
    
    Args:
        model: Model name (default: from env or qwen2.5-coder:7b)
    
    Returns:
        AutoGen config_list
    """
    model = model or os.getenv("OLLAMA_MODEL", "qwen2.5-coder:7b")
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")
    
    return [{
        "model": model,
        "base_url": base_url,
        "api_key": "ollama",  # Ollama doesn't need a real key
        "api_type": "openai"  # Use OpenAI-compatible API
    }]

# ============================================
# DEEPSEEK CONFIG (Optional - Requires Key)
# ============================================
def get_deepseek_config(model: str = "deepseek-chat"):
    """
    Get DeepSeek configuration.
    Requires DEEPSEEK_API_KEY in .env
    """
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError(
            "DEEPSEEK_API_KEY not found. "
            "Get one free at https://platform.deepseek.com"
        )
    
    return [{
        "model": model,
        "base_url": "https://api.deepseek.com/v1",
        "api_key": api_key
    }]

# ============================================
# MINIMAX CONFIG (Optional - Requires Key)
# ============================================
def get_minimax_config(model: str = "MiniMax-Text-01"):
    """Get MiniMax configuration."""
    api_key = os.getenv("MINIMAX_API_KEY")
    if not api_key:
        raise ValueError("MINIMAX_API_KEY not found")
    
    return [{
        "model": model,
        "base_url": "https://api.minimax.io/anthropic/v1",
        "api_key": api_key
    }]

# ============================================
# UNIFIED CONFIG (Auto-detect best provider)
# ============================================
def get_config(provider: str = "auto") -> list:
    """
    Get configuration for specified provider.
    Priority: Ollama > DeepSeek > MiniMax
    """
    if provider == "auto":
        try:
            return get_ollama_config()
        except Exception:
            pass
        
        if os.getenv("DEEPSEEK_API_KEY"):
            return get_deepseek_config()
        
        if os.getenv("MINIMAX_API_KEY"):
            return get_minimax_config()
        
        raise ValueError("No valid provider. Install Ollama or add API keys.")
    
    providers = {
        "ollama": get_ollama_config,
        "deepseek": get_deepseek_config,
        "minimax": get_minimax_config
    }
    
    if provider not in providers:
        raise ValueError(f"Unknown provider: {provider}")
    
    return providers[provider]()

# ============================================
# VALIDATION
# ============================================
def validate_config(config_list: list) -> bool:
    """Validate that a config actually works."""
    try:
        from autogen import AssistantAgent
        agent = AssistantAgent(
            name="validator",
            llm_config={"config_list": config_list}
        )
        response = agent.generate_reply(
            messages=[{"role": "user", "content": "OK"}]
        )
        return response is not None
    except Exception as e:
        print(f"Config validation failed: {e}")
        return False
