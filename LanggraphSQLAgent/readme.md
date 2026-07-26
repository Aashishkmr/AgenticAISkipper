# Langgraph SQL Agent

This repository contains a SQL agent built with `langraph` that queries a SQLite database and uses LangChain-style tool routing.

## What this project is

- A SQL agent implemented with `langgraph`
- Uses custom node functions for:
  - listing tables
  - calling schema tools
  - generating SQL queries
  - checking and running queries
- Designed to work with Azure/Foundry infrastructure instead of the plain tutorial setup

## Differences from the tutorial

1. Uses Azure Application Insights for tracing
   - `tracer.py` configures `AzureAIOpenTelemetryTracer`
   - traces are sent to Azure App Insights for monitoring

2. Uses Foundry as the resource endpoint rather than Azure OpenAI directly
   - environment value `FOUNDRY_PROJECT_ENDPOINT`
   - agent is configured to use an Azure Foundry project resource

3. Deployment uses Azure Foundry
   - the runtime target is Azure Foundry instead of a local or standard Azure OpenAI deployment
   - this repo is set up for Foundry-hosted agent deployment

## Files of interest

- `graph.py` — graph construction and agent compile logic
- `nodes.py` — node implementations and tool bindings
- `tools.py` — SQL tool definitions
- `init_chat_model.py` — model initialization
- `tracer.py` — App Insights tracing setup
- `.env` — environment values used for Foundry and tracing

## Notes

- Make sure `.env` is loaded before any module calls `os.getenv(...)`
- `common/config.py` can be used to load environment variables at startup
- The agent uses a mix of tool nodes and custom prompts to generate and validate SQL
