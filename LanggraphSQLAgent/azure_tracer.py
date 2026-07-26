import os

from azure.identity import DefaultAzureCredential
from langchain_azure_ai.callbacks.tracers import AzureAIOpenTelemetryTracer

azure_tracer = AzureAIOpenTelemetryTracer(
	project_endpoint=os.getenv("FOUNDRY_PROJECT_ENDPOINT"),
	credential=DefaultAzureCredential(),
	name="foundry-project-tracer",
	agent_id="foundry-based-sql-agent",
	trace_all_langgraph_nodes=True,
)