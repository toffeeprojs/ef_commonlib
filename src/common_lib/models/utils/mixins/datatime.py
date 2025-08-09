from pydantic import BaseModel, Field
from datetime import datetime


class DataTimeField(BaseModel):
    datatime: datetime = Field(default_factory=datetime.now)


__all__ = ["DataTimeField"]
