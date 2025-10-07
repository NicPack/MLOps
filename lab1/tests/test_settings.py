import pytest
from main import export_envs
from settings import Settings


def test_prod_env():
    export_envs(env_path="lab1/config/", secrets_path="lab1/tests/", environment="prod")
    settings = Settings()
    assert settings.ENVIRONMENT == "prod"
    assert settings.APP_NAME == "lab1"
    assert settings.API_KEY == "fakesecretapikey12345"


def test_test_env():
    export_envs(env_path="lab1/config/", secrets_path="lab1/tests/", environment="test")
    settings = Settings()
    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "lab1"
    assert settings.API_KEY == "fakesecretapikey12345"


def test_dev_env():
    with pytest.raises(ValueError) as exc_info:
        export_envs(
            env_path="lab1/config/", secrets_path="lab1/tests/", environment="xyz"
        )
