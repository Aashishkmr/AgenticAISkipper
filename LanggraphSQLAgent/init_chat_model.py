import os
from langchain.chat_models import init_chat_model
import common.config
model = init_chat_model(
    "azure_ai:gpt-4.1"
)