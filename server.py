from mcp.server.fastmcp import FastMCP
from logger import get_logger

log = get_logger(__name__)

mcp = FastMCP("Python-MCP-Template")

log.info("Server starting...")


@mcp.tool()
def ping(name: str) -> str:
    """Simple test tool to verify the server is working."""
    return f"Hello, {name}! This is a response from the ping tool."

    

if __name__ == "__main__":
    mcp.run(transport="stdio")