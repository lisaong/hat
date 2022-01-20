#!/usr/bin/env python3
import sys

def get_platform():
    """Returns the current platform: Linux, Windows, or OS X"""
    
    if sys.platform.startswith("linux"):
        return "Linux"
    if sys.platform == "win32":
        return "Windows"
    if sys.platform == "darwin":
        return "OS X"

    sys.exit(f"ERROR: Unsupported operating system: {sys.platform}")
