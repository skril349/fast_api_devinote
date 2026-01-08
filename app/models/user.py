

from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    full_name: str = Field(index=True, default="")
    email: str = Field(index=True, unique=True)
    hashed_password: str = Field(default="")

class UserCreate(SQLModel):
    full_name: str = ""
    email: str
    password: str
    
class UserRead(SQLModel):
    id: int
    full_name: str
    email: str
    model_config = {"from_attributes": True}

class UserUpdate(SQLModel):
    full_name: str | None = None
    email: str | None = None
    password: str | None = None
    