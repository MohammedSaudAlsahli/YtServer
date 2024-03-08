from pydantic import BaseModel

from .format import Format


class Formats(BaseModel):
    audio: list[Format | None] | None
    video: list[Format | None] | None
