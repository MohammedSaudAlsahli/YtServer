from ..models import Video
from .get_formats import getting_formats


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
            formats=getting_formats(
                video.get("formats"),
            ),
        )
    )
    return instance
