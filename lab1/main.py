import argparse
import os

import yaml
from dotenv import load_dotenv
from settings import Settings


def export_envs(environment: str = "dev") -> None:
    environment = environment.lower()
    if environment not in ["dev", "test", "prod"]:
        raise ValueError("env variable not in (dev, test, prod)")
    if environment == "dev":
        load_dotenv(".env.dev")
    elif environment == "test":
        load_dotenv(".env.test")
    else:
        load_dotenv(".env.prod")

    with open("secrets.yaml") as file:
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

    export_envs(args.environment)

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("API_KEY: ", settings.API_KEY)
