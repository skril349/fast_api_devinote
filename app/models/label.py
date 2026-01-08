

from sqlalchemy import UniqueConstraint
from sqlmodel import SQLModel, Field


class Label(SQLModel, table=True):
    __tablename__ = "label"
    __table_args__ = (UniqueConstraint("owner_id", "name", name="uix_owner_labelname"))
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True, min_length=1, default="")
    owner_id: int = Field(default=None, foreign_key="user.id", index=True)


class NoteLabelLink(SQLModel, table=True):
    __tablename__ = "note_label_link"
    __table_args__ = (UniqueConstraint("note_id", "label_id", name="uix_note_label"))
    id: int = Field(default=None, primary_key=True)
    note_id: int = Field(foreign_key="note.id", primary_key=True)
    label_id: int = Field(foreign_key="label.id", primary_key=True)


class LabelCreate(SQLModel):
    name: str   
class LabelRead(SQLModel):
    id: int
    name: str
    model_config = {"from_attributes": True}
    
