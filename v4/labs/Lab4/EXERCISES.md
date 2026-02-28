# Lab 4: Exercises & Deep Dive

## Exercise 1: Complete Tool System

```python
import os
import json
from datetime import datetime
from autogen import AssistantAgent, UserProxyAgent

# ============================================================================
# FILE TOOLS
# ============================================================================

def read_file(filepath: str) -> str:
    """Read contents of a file."""
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return f"File not found: {filepath}"
    except Exception as e:
        return f"Error reading file: {str(e)}"

def write_file(filepath: str, content: str) -> str:
    """Write content to a file."""
    try:
        with open(filepath, 'w') as f:
            f.write(content)
        return f"Successfully wrote to {filepath}"
    except Exception as e:
        return f"Error writing file: {str(e)}"

def list_directory(path: str = ".") -> str:
    """List files in a directory."""
    try:
        files = os.listdir(path)
        return "\n".join(files) if files else "Empty directory"
    except FileNotFoundError:
        return f"Directory not found: {path}"
    except Exception as e:
        return f"Error: {str(e)}"

# ============================================================================
# DATA TOOLS
# ============================================================================

def save_json(data: dict, filepath: str) -> str:
    """Save data as JSON."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        return f"Saved to {filepath}"
    except Exception as e:
        return f"Error: {str(e)}"

def load_json(filepath: str) -> str:
    """Load JSON from file."""
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        return json.dumps(data, indent=2)
    except FileNotFoundError:
        return f"File not found: {filepath}"
    except Exception as e:
        return f"Error: {str(e)}"

# ============================================================================
# SYSTEM TOOLS
# ============================================================================

def get_timestamp() -> str:
    """Get current timestamp."""
    return datetime.now().isoformat()

def get_working_directory() -> str:
    """Get current working directory."""
    return os.getcwd()

# ============================================================================
# REGISTER ALL TOOLS
# ============================================================================

assistant = AssistantAgent(
    name="file_assistant",
    llm_config={"config_list": config_list}
)

# Register file tools
assistant.register_for_execution()(read_file)
assistant.register_for_execution()(write_file)
assistant.register_for_execution()(list_directory)

# Register data tools
assistant.register_for_execution()(save_json)
assistant.register_for_execution()(load_json)

# Register system tools
assistant.register_for_execution()(get_timestamp)
assistant.register_for_execution()(get_working_directory)

# Test
user = UserProxyAgent(name="user", human_input_mode="NEVER")
user.initiate_chat(assistant, message="What time is it and what's in the current directory?")
```

---

## Exercise 2: API Tool with Error Handling

```python
import requests
from typing import Optional

def fetch_url(url: str, timeout: int = 10) -> str:
    """Fetch content from a URL."""
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return f"Success: {len(response.text)} bytes from {url}"
    except requests.exceptions.Timeout:
        return f"Error: Request timeout for {url}"
    except requests.exceptions.HTTPError as e:
        return f"Error: HTTP {e.response.status_code} for {url}"
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

def post_json(url: str, data: dict, timeout: int = 10) -> str:
    """POST JSON data to URL."""
    try:
        response = requests.post(url, json=data, timeout=timeout)
        response.raise_for_status()
        return f"Success: {response.status_code}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_headers(url: str) -> str:
    """Get HTTP headers from URL."""
    try:
        response = requests.head(url, timeout=5)
        headers = dict(response.headers)
        return json.dumps(headers, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"
```

---

## Exercise 3: Database Tools

```python
import sqlite3
from typing import List, Dict

def init_db(db_path: str = "data.db") -> str:
    """Initialize database with tables."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                status TEXT DEFAULT 'pending',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()
        return f"Database initialized: {db_path}"
    except Exception as e:
        return f"Error: {str(e)}"

def add_task(title: str, db_path: str = "data.db") -> str:
    """Add a task to database."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
        conn.commit()
        task_id = cursor.lastrowid
        conn.close()
        return f"Task added: ID {task_id}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_tasks(status: str = None, db_path: str = "data.db") -> str:
    """Get tasks from database."""
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        if status:
            cursor.execute("SELECT * FROM tasks WHERE status = ?", (status,))
        else:
            cursor.execute("SELECT * FROM tasks")
        
        rows = cursor.fetchall()
        conn.close()
        
        if not rows:
            return "No tasks found"
        
        return "\n".join([f"ID: {r['id']}, Title: {r['title']}, Status: {r['status']}" for r in rows])
    except Exception as e:
        return f"Error: {str(e)}"

def update_task(task_id: int, status: str, db_path: str = "data.db") -> str:
    """Update task status."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))
        conn.commit()
        conn.close()
        return f"Task {task_id} updated to {status}"
    except Exception as e:
        return f"Error: {str(e)}"
```

---

## Exercise 4: Tool Composition

```python
# Compose multiple tools together

def pipeline(*functions):
    """Create a pipeline of functions."""
    def execute(input_data):
        result = input_data
        for func in functions:
            result = func(result)
        return result
    return execute

# Example: read -> process -> write
def process_content(content: str) -> str:
    """Process content (example: uppercase)."""
    return content.upper()

# Pipeline: read_file -> process -> write_file
# Note: This is conceptual; actual implementation needs careful handling
```
