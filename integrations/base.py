from abc import ABC, abstractmethod

class Integration(ABC):
    """Abstract base class for integrations."""

    @abstractmethod
    def register_tools(self, mcp):
        """Register this integration's tools with the MCP server."""
        pass

    def validate_credentials(self):
        """Override this to check required env vars on startup."""
        pass