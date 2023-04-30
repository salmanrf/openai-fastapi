from pydantic import BaseSettings


class Settings(BaseSettings):
    OPENAI_API_SECRET_KEY: str
    DATABASE_URL: str
    MONGO_INITDB_DATABASE: str
    CLIENT_ORIGIN: str

    class Config:
        env_file = './.env'


config = Settings()
