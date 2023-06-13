import openai
from langchain.chat_models import ChatOpenAI

from reworkd_platform.schemas import ModelSettings
from reworkd_platform.settings import settings
from reworkd_platform.web.api.agent.api_utils import rotate_keys

openai.api_base = settings.openai_api_base


def create_model(model_settings: ModelSettings, streaming: bool = False) -> ChatOpenAI:
    return ChatOpenAI(
        openai_api_key='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',
        temperature=model_settings.temperature,
        model=model_settings.model,
        max_tokens=model_settings.max_tokens,
        streaming=streaming,
        openai_api_base= 'https://api.openai.com/v1',
        openai_organization='',
    )
