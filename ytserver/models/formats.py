from pydantic import BaseModel

from ..models import Format


class Formats(BaseModel):
    audio: list[Format | None] | None
    video: list[Format | None] | None
