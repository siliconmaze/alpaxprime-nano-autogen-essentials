# Lab 1: Hello AutoGen - Setting Up Your Environment

## Objective
Set up your development environment and verify AutoGen is working correctly.

## Estimated Time
15 minutes

## Prerequisites
- Python 3.8+
- OpenAI API Key

---

## Step 1: Install AutoGen

```bash
# Create a virtual environment (recommended)
python -m venv autogen-env
source autogen-env/bin/activate  # On Windows: autogen-env\Scripts\activate

# Install AutoGen
pip install pyautogen

# Install additional dependencies
pip install openai python-dotenv
```

---

## Step 2: Configure Your API Key

Create a `.env` file in your project root:

```bash
# .env
OPENAI_API_KEY=your-openai-api-key-here
```

Or set it directly:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

---

## Step 3: Verify Your Setup

Create `verify_setup.py`:

```python
"""Lab 1: Verify AutoGen Installation"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Check if API key is set
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("⚠️  WARNING: OPENAI_API_KEY not found in environment")
    print("Please set your API key in .env or export OPENAI_API_KEY")
    exit(1)

# Try to import AutoGen
try:
    import autogen
    print(f"✓ AutoGen version: {autogen.__version__}")
except ImportError as e:
    print(f"✗ Failed to import AutoGen: {e}")
    exit(1)

# Create a simple configuration
config_list = [
    {
        "model": "gpt-4",
        "api_key": api_key
    }
]

# Create a simple agent
try:
    assistant = autogen.AssistantAgent(
        name="test_agent",
        llm_config={"config_list": config_list}
    )
    print("✓ AssistantAgent created successfully!")
except Exception as e:
    print(f"✗ Failed to create agent: {e}")
    exit(1)

print("\n" + "="*50)
print("🎉 All checks passed! AutoGen is ready to use.")
print("="*50)
```

---

## Step 4: Run the Verification

```bash
python verify_setup.py
```

**Expected Output:**
```
✓ AutoGen version: 0.2.0
✓ AssistantAgent created successfully!

==================================================
🎉 All checks passed! AutoGen is ready to use.
==================================================
```

---

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'autogen'` | Run `pip install pyautogen` |
| `AuthenticationError` | Check your API key is correct |
| `RateLimitError` | Wait a moment and retry |

---

## What You Learned

✓ How to install AutoGen
✓ How to configure API keys
✓ How to verify your setup

---

## Next Step

Proceed to **Lab 2: Agent Conversations** to create your first multi-agent application!
