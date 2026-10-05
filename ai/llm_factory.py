from crewai import LLM

from ai.config import settings


def get_llm() -> LLM:
    """Возвращает LLM согласно .env. Единственная точка переключения провайдера."""
    if settings.llm_provider == "ollama":
        return LLM(
            model=f"ollama/{settings.ollama_model}",
            base_url=settings.ollama_base_url,
            temperature=settings.llm_temperature,
        )

    if not settings.cloud_api_key or not settings.cloud_model:
        raise RuntimeError(
            "LLM_PROVIDER=cloud, но CLOUD_MODEL или CLOUD_API_KEY пуст. Проверьте .env"
        )

    return LLM(
        model=f"openai/{settings.cloud_model}",
        base_url=settings.cloud_base_url,
        api_key=settings.cloud_api_key.get_secret_value(),
        project=settings.cloud_project or None,  # нужен, например, Yandex AI Studio
        temperature=settings.llm_temperature,
    )
