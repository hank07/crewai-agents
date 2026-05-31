import os
from crewai import LLM
from dotenv import load_dotenv

load_dotenv()

# Our gateway is OpenAI-compatible but serves Claude models.
# CrewAI detects "claude-" prefix → tries native Anthropic provider (wrong endpoint format).
# Patch: force "openai" provider so CrewAI uses the OpenAI native provider,
# which reads OPENAI_BASE_URL and routes to our gateway correctly.
_original_infer = LLM._infer_provider_from_model.__func__

@classmethod
def _gateway_infer(cls, model: str) -> str:
    if model.startswith("claude-"):
        return "openai"
    return _original_infer(cls, model)

LLM._infer_provider_from_model = _gateway_infer

os.environ["OPENAI_API_KEY"] = os.getenv("LLM_API_KEY", "###")
os.environ["OPENAI_BASE_URL"] = os.getenv("LLM_BASE_URL", "###")

llm = LLM(model=os.getenv("LLM_MODEL", "claude-sonnet-4-5-20250929"))
