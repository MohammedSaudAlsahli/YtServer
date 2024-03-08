from pydantic import BaseModel

from ..models import Formats


class Video(BaseModel):
    extractor_key: str
    display_id: str
    thumbnail: str | None
    title: str
    description: str | None
    uploader_url: str
    webpage_url: str
    duration_string: str | None
    formats: Formats
    upload_date: str
