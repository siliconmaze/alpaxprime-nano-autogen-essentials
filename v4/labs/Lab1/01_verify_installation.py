#!/usr/bin/env python3
"""
Lab 1: Verify Installation
===========================

This script verifies that all required dependencies are correctly installed.

Run:
    python 01_verify_installation.py
"""

import sys
import importlib

def check_python_version():
    """Check if Python version is 3.10 or higher."""
    print(f"[1] Python version: {sys.version}")
    if sys.version_info >= (3, 10):
        print("    ✓ Python version is compatible (3.10+)")
        return True
    else:
        print("    ✗ WARNING: Python 3.10+ recommended")
        return False


def check_package(name, display_name=None):
    """Check if a package is installed."""
    display_name = display_name or name
    try:
        if name == "dotenv":
            importlib.import_module("dotenv")
        elif name == "openai":
            importlib.import_module("openai")
        elif name == "langchain":
            importlib.import_module("langchain")
        else:
            importlib.import_module(name)
        
        # Try to get version
        try:
            mod = importlib.import_module(name)
            version = getattr(mod, "__version__", "unknown")
            print(f"    ✓ {display_name}: installed (version {version})")
        except:
            print(f"    ✓ {display_name}: installed")
        return True
    except ImportError:
        print(f"    ✗ {display_name}: NOT installed")
        return False


def main():
    print("=" * 60)
    print("Lab 1: Verifying Installation")
    print("=" * 60)
    print()
    
    all_good = True
    
    # Check Python
    all_good &= check_python_version()
    print()
    
    # Check required packages
    print("[2] Checking required packages:")
    all_good &= check_package("autogen", "AutoGen")
    all_good &= check_package("dotenv", "python-dotenv")
    print()
    
    # Check optional packages
    print("[3] Checking optional packages:")
    check_package("openai", "OpenAI")
    check_package("langchain", "LangChain")
    print()
    
    # Summary
    print("=" * 60)
    if all_good:
        print("✓ All required packages installed!")
        print("\nYou can proceed to the next step.")
    else:
        print("✗ Some packages are missing.")
        print("\nInstall missing packages with:")
        print("  pip install pyautogen python-dotenv")
    print("=" * 60)


if __name__ == "__main__":
    main()
