"""
Lab 7: Monitoring & Observability
===================================

Add logging, metrics, and monitoring to AutoGen.

Run with:
    python 02_monitoring.py
"""

import os
import time
import json
from datetime import datetime
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent

load_dotenv()

print("=" * 60)
print("Lab 7: Monitoring & Observability")
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
# METRICS TRACKER
# ============================================================================

class AgentMetrics:
    """Track agent metrics."""
    
    def __init__(self):
        self.requests = []
        self.errors = []
        
    def track_request(self, model, duration_ms, success, tokens=None):
        """Record a request."""
        self.requests.append({
            "timestamp": datetime.now().isoformat(),
            "model": model,
            "duration_ms": duration_ms,
            "success": success,
            "tokens": tokens
        })
        
    def track_error(self, model, error):
        """Record an error."""
        self.errors.append({
            "timestamp": datetime.now().isoformat(),
            "model": model,
            "error": str(error)
        })
        
    def get_stats(self):
        """Get statistics."""
        total = len(self.requests)
        successful = sum(1 for r in self.requests if r["success"])
        
        durations = [r["duration_ms"] for r in self.requests if r["duration_ms"]]
        avg_duration = sum(durations) / len(durations) if durations else 0
        
        return {
            "total_requests": total,
            "successful": successful,
            "failed": total - successful,
            "success_rate": successful / total if total > 0 else 0,
            "avg_duration_ms": avg_duration,
            "total_errors": len(self.errors)
        }

# ============================================================================
# DEMO
# ============================================================================

print("\n[1] Creating metrics tracker...")

metrics = AgentMetrics()
assistant = AssistantAgent(name="assistant", llm_config={"config_list": config_list})
user_proxy = UserProxyAgent(name="user", human_input_mode="NEVER")

# Simulate requests
print("\n[2] Tracking requests...")

for i in range(3):
    start = time.time()
    try:
        response = user_proxy.generate_reply(
            messages=[{"role": "user", "content": f"Message {i}"}],
            sender=assistant
        )
        duration = (time.time() - start) * 1000
        metrics.track_request(model, duration, success=True)
        print(f"    Request {i+1}: OK ({duration:.0f}ms)")
    except Exception as e:
        duration = (time.time() - start) * 1000
        metrics.track_request(model, duration, success=False)
        metrics.track_error(model, e)
        print(f"    Request {i+1}: FAILED")

# Print stats
print("\n[3] Statistics:")
stats = metrics.get_stats()
for key, value in stats.items():
    print(f"    {key}: {value}")

print("\n" + "=" * 60)
print("✓ Monitoring Complete!")
print("=" * 60)
