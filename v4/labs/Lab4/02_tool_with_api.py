"""
Lab 4: Tools with Real API Calls
=================================

Build tools that make actual API calls.

Key Concepts:
- Async functions for API calls
- Error handling in tools
- Tool response formatting

Run with:
    python 02_tool_with_api.py
"""

import os
import json
import asyncio
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent

load_dotenv()

print("=" * 60)
print("Lab 4: Tools with Real API Calls")
print("=" * 60)

api_key = os.getenv("DEEPSEEK_API_KEY", "")
if not api_key:
    api_key = "ollama"
    model = "qwen2.5-coder:7b"
    base_url = "http://localhost:11434/v1"
else:
    model = "deepseek-chat"
    base_url = "https://api.deepseek.com/v1"

config_list = [{"model": model, "base_url": base_url, "api_key": api_key}]

# ============================================================================
# DEFINE API TOOLS
# ============================================================================

async def fetch_price(symbol: str) -> str:
    """
    Fetch current stock price.
    
    Args:
        symbol: Stock ticker (e.g., "AAPL", "GOOGL")
    
    Returns:
        Current price or error
    """
    try:
        # Note: Use real API in production (Yahoo Finance, Alpha Vantage, etc.)
        # This is a mock for demonstration
        mock_prices = {
            "AAPL": "$178.50",
            "GOOGL": "$141.20",
            "MSFT": "$378.90",
            "AMZN": "$178.35",
        }
        
        symbol = symbol.upper()
        if symbol in mock_prices:
            return f"{symbol}: {mock_prices[symbol]}"
        return f"Unknown symbol: {symbol}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_exchange_rate(from_curr: str, to_curr: str) -> str:
    """
    Get exchange rate between currencies.
    
    Args:
        from_curr: Source currency (e.g., "USD")
        to_curr: Target currency (e.g., "EUR")
    
    Returns:
        Exchange rate
    """
    try:
        # Mock rates (use real API in production)
        rates = {
            ("USD", "EUR"): 0.92,
            ("USD", "GBP"): 0.79,
            ("USD", "JPY"): 149.50,
            ("EUR", "USD"): 1.09,
            ("GBP", "USD"): 1.27,
        }
        
        pair = (from_curr.upper(), to_curr.upper())
        if pair in rates:
            return f"1 {from_curr} = {rates[pair]} {to_curr}"
        return f"Exchange rate unknown for {from_curr} to {to_curr}"
    except Exception as e:
        return f"Error: {str(e)}"


def search_wikipedia(query: str) -> str:
    """
    Search Wikipedia for a topic.
    
    Args:
        query: Search query
    
    Returns:
        Summary from Wikipedia or error
    """
    try:
        import urllib.parse
        import urllib.request
        
        # Use Wikipedia API
        base_url = "https://en.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "format": "json",
            "srlimit": 1
        }
        
        url = f"{base_url}?{urllib.parse.urlencode(params)}"
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode())
            
        if data["query"]["search"]:
            result = data["query"]["search"][0]
            snippet = result["snippet"].replace("<", "").replace(">", "")
            return f"{result['title']}: {snippet[:200]}..."
        return f"No results for: {query}"
    except Exception as e:
        return f"Error: {str(e)}"

# ============================================================================
# REGISTER AND TEST
# ============================================================================

print("\n[1] Creating agent with API tools...")

assistant = AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list}
)

# Register async tool
assistant.register_for_execution()(fetch_price)

# Register sync tools  
assistant.register_for_execution()(get_exchange_rate)
assistant.register_for_execution()(search_wikipedia)

print("    Registered: fetch_price, get_exchange_rate, search_wikipedia")

# ============================================================================
# TEST
# ============================================================================

user_proxy = UserProxyAgent(name="user", human_input_mode="NEVER")

print("\n[2] Testing API tools...")

print("\n    [Stock Price]")
user_proxy.initiate_chat(assistant, message="What's the price of AAPL?")

print("\n    [Exchange Rate]")
user_proxy.initiate_chat(assistant, message="Convert 100 USD to EUR")

print("\n    [Wikipedia Search]")
user_proxy.initiate_chat(assistant, message="Tell me about Python programming language")

print("\n" + "=" * 60)
print("✓ API Tools Complete!")
print("=" * 60)
