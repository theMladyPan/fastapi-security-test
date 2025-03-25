"""Python FastAPI Auth0 integration example"""

from fastapi import FastAPI, Security, Request, Depends
from fastapi.responses import HTMLResponse
from app.utils import VerifyToken
from app.config import _settings, oauth
from starlette.middleware.sessions import SessionMiddleware
from fastapi.middleware.cors import CORSMiddleware
from app.auth.routes import auth_router


# Creates app instance
app = FastAPI()
auth = VerifyToken()

app.add_middleware(SessionMiddleware, secret_key=_settings.session_secret)
# app.include_router(auth_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["Authorization", "Content-Type"],
    max_age=86400,
)


@app.get("/api/public")
async def public():
    """No access token required to access this route"""

    result = {
        "status": "success",
        "msg": ("Hello from a public endpoint! You don't need to be " "authenticated to see this."),
    }
    return result


@app.get("/api/private")
async def private(auth_result: str = Security(auth.verify)):
    """A valid access token is required to access this route"""
    return auth_result
