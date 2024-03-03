from yt_dlp import YoutubeDL

from ytserver.models.video import Video
from ytserver.functions.matching import matching


def extract_video_info(url: str) -> list[Video]:
    opt = {
        
    }
    with YoutubeDL(opt) as youtube:
        try:
            video_info = youtube.extract_info(
                url,
                download=False,
            )
            video =  matching(video_info)

        except Exception as exception:
            return {"Error": f"{exception}"}

    return video
