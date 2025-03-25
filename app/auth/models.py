from pydantic import BaseModel
from pydantic.networks import EmailStr


class User(BaseModel):
    """
    This is the User model that will be used to store the user information

    Attributes:
        sub: str - The user's unique identifier
        nickname: str - The user's nickname
        name: EmailStr - The user's email address
        picture: str - The user's profile picture
        updated_at: str - The user's last updated time
    """

    sub: str
    nickname: str
    name: EmailStr
    picture: str
    updated_at: str
