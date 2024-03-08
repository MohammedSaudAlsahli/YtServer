from ytserver.models.video import Video
from ytserver.functions.get_formats import get_formats


def video_instance(video: dict):
    """
    Creates a video instance based on the provided video dictionary.

    Args:
        video (dict): The dictionary containing video information.

    Returns:
        Video: The created video instance.
    """
    instance: Video = Video(
        **dict(
            video,
            formats=get_formats(
                video.get("formats"),
            ),
        )
    )
    return instance
