import os
import argparse
from dotenv import load_dotenv
from settings import Settings


def export_envs(environment: str = "dev") -> None:
    env_files = {
        "dev": "config/.env.dev",
        "test": "config/.env.test",
        "prod": "config/.env.prod",
    }

    if environment not in env_files:
        raise ValueError(
            f"Invalid environment '{environment}'. Must be one of: dev, test, prod"
        )

    env_file = env_files[environment]

    if not os.path.exists(env_file):
        raise FileNotFoundError(f"Environment file not found: {env_file}")

    load_dotenv(dotenv_path=env_file, override=True)


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

    import os
    import yaml

    with open("secrets.yaml", "r", encoding="utf-8") as f:
        secrets = yaml.safe_load(f)

    os.environ["API_KEY"] = secrets["api_key"]
    os.environ["HASLO"] = secrets["haslo"]

    print("API_KEY:", os.environ.get("API_KEY"))
    print("HASLO:", os.environ.get("HASLO"))
