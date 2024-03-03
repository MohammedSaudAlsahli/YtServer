from pydantic import BaseModel

from ytserver.models.format import Format


class Formats(BaseModel):
    audio: list[Format | None] | None
    video: list[Format | None] | None
