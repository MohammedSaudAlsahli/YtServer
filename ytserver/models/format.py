from pydantic import BaseModel


class Format(BaseModel):
    format: str
    format_note: str = None
    ext: str
    protocol: str
    resolution: str
    url: str
    filesize: int | None = None
