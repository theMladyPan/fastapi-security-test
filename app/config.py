from functools import lru_cache

from pydantic_settings import BaseSettings
from authlib.integrations.starlette_client import OAuth


class Settings(BaseSettings):
    auth0_domain: str
    auth0_api_audience: str
    auth0_issuer: str
    auth0_algorithms: str
    auth0_client_id: str
    auth0_client_secret: str
    session_secret: str

    openai_api_key: str

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()


oauth = OAuth()
_settings = get_settings()

oauth.register(
    "auth0",
    client_id=_settings.auth0_client_id,
    client_secret=_settings.auth0_client_secret,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{_settings.auth0_domain}/.well-known/openid-configuration",
)
