question = "Which genre on average has the longest tracks?"
import json
from pprint import pprint
from langgraph.types import Command

from graph_with_interrupt import agent_with_interrupt
from azure_tracer import azure_tracer
# Build the config with tracer
config = {
    "configurable": {"thread_id": "1"},   # optional metadata
    "callbacks": [azure_tracer],                # attach your tracer here
}
stream = agent_with_interrupt.stream_events(
    {"messages": [{"role": "user", "content": question}]},
    version="v3",
    config=config
)
for message in stream.messages:
    for token in message.text:
        print(token, end="", flush=True)
if stream.interrupted:
    action = stream.interrupts[0]
    print("INTERRUPTED:")
    for request in action.value:
        print(json.dumps(request, indent=2))

from langgraph.types import Command

stream = agent_with_interrupt.stream_events(
    Command(resume={"type": "accept"}),
    # Command(resume={"type": "edit", "args": {"query": "..."}}),
    config,
    version="v3",
)
for message in stream.messages:
    for token in message.text:
        print(token, end="", flush=True)
if stream.interrupted:
    action = stream.interrupts[0]
    print("INTERRUPTED:")
    for request in action.value:
        print(json.dumps(request, indent=2))