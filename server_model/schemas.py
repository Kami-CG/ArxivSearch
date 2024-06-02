from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class EntryBase(BaseModel):
    url_source: str
    updated: datetime
    published: datetime
    title: str
    summary: Optional[str] = None
    authors: Optional[str] = None


class EntryCreate(EntryBase):
    pass


class Entry(EntryBase):
    id: int

    class Config:
        from_attributes = True
