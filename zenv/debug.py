"""
Zen Environment Debugging Module
"""

from dataclasses import dataclass


@dataclass
class DebugArgs:
    """
    Debugging arguments.
    """
    debug: bool
    quiet: bool