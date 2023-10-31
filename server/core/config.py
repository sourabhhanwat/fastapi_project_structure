from starlette.config import Config
API_PREFIX = '/v1/api'
VERSION = "0.0.1"

config = Config(".env")
PROJECT_NAME: str = config("Example", default="Project Example")
DEBUG: bool = config("DEBUG", cast=bool, default=True)