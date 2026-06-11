from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Python-MCP-Template")

@mcp.tool()
def ping(name: str) -> str:
    """Simple test tool to verify the server is working."""
    return f"Hello, {name}! This is a response from the ping tool."

if __name__ == "__main__":
    mcp.run(transport="stdio")