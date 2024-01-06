from uuid import uuid4
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: str = Field(default=str(uuid4()), primary_key=True)
    username: str
    password: str


class Game(SQLModel, table=True):
    id: str = Field(default=str(uuid4()), primary_key=True)
    name: str
    score: int
    user_id: str = Field(foreign_key="user.id")
