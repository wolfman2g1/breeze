from functools import lru_cache
from typing import Optional
from pydantic import BaseSettings, SecretStr

class Settings(BaseSettings):
    ENV: str
    DB_HOST: str
    DB_USER: str
    DB_PASS: SecretStr
    TESTING: Optional[bool] = False

@lru_cache
def get_config():
    return Settings()

config = get_config()