import uvicorn
from fastapi import FastAPI

from .functions import video_info

app = FastAPI()


@app.get("/")
def root():
    """
    This function represents the root endpoint of the API. It does not take any parameters and returns a dictionary with a message key containing the value "add video url to get download link".
    """
    return {"message": "add video url to get download link"}


@app.get("/{video_url:path}")
async def root(video_url):
    """
    This function handles GET requests for the specified video URL, extracts video information, and returns it.
    """
    video = video_info(video_url)
    return video


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("ytserver.main:app", host="0.0.0.0", port=8000, reload=True)
