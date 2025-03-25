"""Python FastAPI Auth0 integration example"""

from fastapi import FastAPI, Security
from app.utils import VerifyToken  # 👈 Import the new class

# Creates app instance
app = FastAPI()
auth = VerifyToken()  # 👈 Get a new instance


@app.get("/api/public")
def public():
    """No access token required to access this route"""

    result = {
        "status": "success",
        "msg": ("Hello from a public endpoint! You don't need to be " "authenticated to see this."),
    }
    return result


@app.get("/api/private")
def private(
    auth_result: str = Security(auth.verify),
):  # 👈 Use Security and the verify method to protect your endpoints
    """A valid access token is required to access this route"""
    return auth_result
