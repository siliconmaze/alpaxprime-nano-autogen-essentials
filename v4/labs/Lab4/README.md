# Lab 4: Tools & Function Calling

## Objectives

- Register custom functions as tools
- Build tools that call APIs
- Handle tool errors
- Chain multiple tools

---

## Key Concepts

### Registering Tools

```python
def my_function(arg: str) -> str:
    """Description of what the function does."""
    return "result"

agent.register_for_execution()(my_function)
```

### Tool Requirements

- Docstrings are used by LLM to understand when to call
- Return strings (not objects)
- Handle errors gracefully

---

## Examples

### Example 1: Basic Tool

```python
def get_weather(location: str) -> str:
    """Get weather for a location."""
    return f"Weather in {location}: 72°F"

assistant.register_for_execution()(get_weather)
```

### Example 2: API Tool

```python
import requests

def fetch_data(url: str) -> str:
    """Fetch data from URL."""
    try:
        r = requests.get(url, timeout=10)
        return r.text[:500]
    except Exception as e:
        return f"Error: {e}"
```

---

## Exercises

1. Create file read/write tools
2. Build calculator with error handling
3. Create a Wikipedia search tool

---

## Next Lab

[Lab 5: Group Chat](../Lab5/README.md)
