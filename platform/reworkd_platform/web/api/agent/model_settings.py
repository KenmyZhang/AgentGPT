import openai
from langchain.chat_models import ChatOpenAI

from reworkd_platform.schemas import ModelSettings
from reworkd_platform.settings import settings
from reworkd_platform.web.api.agent.api_utils import rotate_keys

openai.api_base = settings.openai_api_base


def create_model(model_settings: ModelSettings, streaming: bool = False) -> ChatOpenAI:
    return ChatOpenAI(
        client=None,  # Meta private value but mypy will complain its missing
        openai_api_key='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',
        temperature=model_settings.temperature,
        model=model_settings.model,
        max_tokens=model_settings.max_tokens,
        streaming=streaming,
        openai_api_base= 'https://api.openai.com/v1',
        openai_organization='',
    )
