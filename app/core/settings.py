from pydantic import BaseSettings


class Settings(BaseSettings):
    ALGORITHM = 'HS256'
    EXPIRE_TIME_MINUTES = 15
    SECRET_KEY = 'secret'

settings = Settings()