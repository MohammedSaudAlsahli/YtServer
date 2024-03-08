import uvicorn
from fastapi import FastAPI

from .functions import extract_video_info

app = FastAPI()


@app.get("/")
def root():
    return {"message": "add video url to get download link"}


@app.get("/{video_url:path}")
async def root(video_url):
    video = extract_video_info(video_url)
    return video


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("ytserver.main:app", host="0.0.0.0", port=8000, reload=True)
