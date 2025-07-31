from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=Ollama(id="llama3.2:1b"),
    tools=[DuckDuckGoTools()],
    instructions=[
        "Always use the DuckDuckGo search tool to find current information.",
        "Search the web for the user's query and provide real-time results.",
        "Never provide generic responses - always search first."
    ],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("Search for the latest news on artificial intelligence", stream=True)