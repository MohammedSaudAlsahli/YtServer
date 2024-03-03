from ytserver.models.video import Video
# from ytserver.functions.mapping import mapping
from ytserver.functions.get_formats import get_formats


def video_instance(video: dict):
    instance: Video = Video(
        **dict(
            video,
            formats=get_formats(
                video.get("formats"),
            ),
        )
    )
    # mapping(instance)
    return instance
