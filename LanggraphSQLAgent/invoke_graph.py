question = "Which genre on average has the longest tracks?"
from pprint import pprint

from graph import agent
from azure_tracer import azure_tracer
# Build the config with tracer
config = {
    "configurable": {"thread_id": "1"},   # optional metadata
    "callbacks": [azure_tracer],                # attach your tracer here
}
stream = agent.stream_events(
    {"messages": [{"role": "user", "content": question}]},
    version="v3",
    config=config
)
for message in stream.messages:
    for token in message.text:
        print(token, end="", flush=True)

final_state = stream.output
