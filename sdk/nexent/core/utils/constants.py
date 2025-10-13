from enum import Enum

THINK_TAG_PATTERN = r"<think>.*?</think>"


class ToolCategory(Enum):
    """Enumeration for MCP tool categories"""
    SEARCH = "search"
    FILE = "file"
    EMAIL = "email"
    TERMINAL = "terminal"
