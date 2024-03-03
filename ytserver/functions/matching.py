from ytserver.models.video import Video
from ytserver.functions.instance import video_instance


def matching(info: dict) -> list[Video]:
    videos: list[Video] = []

    match info.get("entries"):
        case None:
            videos.append(video_instance(info))
        case _:
            for entry in info.get("entries"):
                videos.append(video_instance(entry))
    return videos
