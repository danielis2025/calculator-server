# server.py
from mcp.server.fastmcp import FastMCP # pyright: ignore[reportMissingImports]

# Create an MCP server
mcp = FastMCP("Demo")

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add a and b"""
    return a + b

# Add a subtraction tool
@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract "b" from "a" """
    return -(b - a)

# Add a multiplication tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply a and b"""
    return a * b

# Add a division tool
@mcp.tool()
def divide(a: int, b: int) -> int:
    """Divide a by b """
    return (a / b) if b != 0 else float('inf')


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


# Start the server
if __name__ == "__main__":
    mcp.run()