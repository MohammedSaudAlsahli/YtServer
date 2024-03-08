from ..models import Video
from .instance import video_instance


def video_matching(info: dict) -> list[Video]:
    """
    Function to create a list of Video objects based on the input dictionary.
    Takes a dictionary 'info' as input and returns a list of Video objects.
    """
    videos: list[Video] = []

    match info.get("entries"):
        case None:
            videos.append(video_instance(info))
        case _:
            for entry in info.get("entries"):
                videos.append(video_instance(entry))
    return videos
