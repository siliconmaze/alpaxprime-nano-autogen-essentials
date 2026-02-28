"""
Ollama Configuration for AutoGen

Usage:
    from config import get_ollama_config
    config_list = get_ollama_config("qwen2.5-coder:7b")
"""

def get_ollama_config(model="qwen2.5-coder:7b"):
    """Get Ollama config for AutoGen."""
    return [
        {
            "model": model,
            "base_url": "http://localhost:11434/v1",
            "api_key": "ollama",
            "api_type": "openai"
        }
    ]

# List of available Ollama models
AVAILABLE_MODELS = {
    "qwen2.5-coder:7b": "Best for coding",
    "llama3": "General purpose",
    "mistral": "Fast general",
    "codellama": "Code focused",
}
