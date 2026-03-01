"""Lab 1 - Verify Installation"""
import sys

def check_package(name):
    try:
        __import__(name)
        print(f"✅ {name} installed")
        return True
    except ImportError:
        print(f"❌ {name} NOT installed")
        return False

print("Checking dependencies...")
all_ok = all(check_package(p.replace("-", "_")) for p in ["autogen", "dotenv", "requests"])
sys.exit(0 if all_ok else 1)
