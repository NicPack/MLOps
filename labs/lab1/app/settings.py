from pydantic import field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str
    API_KEY: str

    @field_validator("ENVIRONMENT")
    def validate_environments(cls, value):
        if value not in ["dev", "test", "prod"]:
            raise ValueError("ENVIRONMENT variable is not one of dev, test, prod")
        return value
