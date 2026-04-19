import asyncio
from dotenv import load_dotenv
import os

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent




load_dotenv()

llm = ChatOpenAI()

stdio_server_params = StdioServerParameters(
    command="python", 
    args=["/home/paper/eoniq/langchain/langchain-course/documentation-helper/servers/math_server.py"],
)

async def main():
    print("Hello from documentation-helper!")


if __name__ == "__main__":
    asyncio.run(main())
