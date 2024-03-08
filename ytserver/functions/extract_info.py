from yt_dlp import YoutubeDL

from ..models import Video
from .matching import matching_entries


def extract_video_info(url: str) -> list[Video]:
    """
    Function to extract video information from the given URL.

    Args:
        url (str): The URL of the video.

    Returns:
        list[Video]: A list of Video objects containing the extracted video information.
    """
    opt = {
        
    }
    with YoutubeDL(opt) as youtube:
        try:
            video_info = youtube.extract_info(
                url,
                download=False,
            )
            video = matching_entries(video_info)
        except Exception as exception:
            return {"Error": f"{exception}"}

    return video
