from fastapi import Request, HTTPException, status
from app.auth.models import User
from pydantic import ValidationError


def protected_endpoint(request: Request):
    """
    This Dependency protects an endpoint and it can only be accessed if the user has an active session
    """
    if "id_token" not in request.session:  # it could be userinfo instead of id_token
        # this will redirect people to the login after if they are not logged in
        raise HTTPException(
            status_code=status.HTTP_307_TEMPORARY_REDIRECT, detail="Not authorized", headers={"Location": "/login"}
        )


def user_info(request: Request) -> User:
    """
    This Dependency gets the user information from the session
    """
    try:
        return User(**request.session.get("userinfo", {}))
    except ValidationError:
        return None
