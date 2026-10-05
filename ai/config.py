from typing import Literal

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class AISettings(BaseSettings):
    """Конфигурация AI-слоя. Значения берутся из .env или переменных окружения."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # в .env лежат ещё и переменные FastAPI/Postgres
    )

    llm_provider: Literal["ollama", "cloud"] = "ollama"

    ollama_model: str = "qwen3:4b-instruct"
    ollama_base_url: str = "http://localhost:11434"

    # cloud — любой провайдер с OpenAI-совместимым API
    cloud_model: str = ""
    cloud_base_url: str = "https://openrouter.ai/api/v1"
    cloud_api_key: SecretStr | None = None
    cloud_project: str = ""  # нужен только там, где провайдер требует каталог/проект

    llm_temperature: float = 0.1


settings = AISettings()
