import argparse
import os

import yaml
from dotenv import load_dotenv
from settings import Settings


def export_envs(env_path: str, secrets_path: str, environment: str = "dev") -> None:
    environment = environment.lower()
    if environment not in ["dev", "test", "prod"]:
        raise ValueError("env variable not in (dev, test, prod)")
    dotenv_path = f"{env_path}.env.{environment}"
    load_dotenv(dotenv_path, override=True)

    with open(f"{secrets_path}secrets.yaml") as file:
        secrets = yaml.safe_load(file)

    for k, v in secrets.items():
        os.environ[k] = str(v)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(env_path="config", secrets_path="config", environment=args.environment)

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("API_KEY: ", settings.API_KEY)
