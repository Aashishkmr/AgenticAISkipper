from common import config
from graph import agent
import os
from langchain_azure_ai.agents.hosting import ResponsesHostServer

def main() -> None:
    graph = agent
    port = int(os.environ.get("PORT", "8088"))
    ResponsesHostServer(graph).run(port=port)


if __name__ == "__main__":
    main()