from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    openai_api_key: str
    proxycurl_api: str
    serp_api: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
