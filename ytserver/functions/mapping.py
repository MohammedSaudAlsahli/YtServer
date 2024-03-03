from ytserver.models.video import Video
from ytserver.database.session import (
    AudioFormat,
    VideoFormat,
    session,
)


# issue with async and await, the error said, RuntimeWarning: coroutine 'mapping' was never awaited mapping(instance)


# async def mapping(video_instance: Video) -> None:
#     video: Video = await Video(
#         extractor_key=video_instance.extractor_key,
#         display_id=video_instance.display_id,
#         thumbnail=video_instance.thumbnail,
#         title=video_instance.title,
#         description=video_instance.description,
#         uploader_url=video_instance.uploader_url,
#         webpage_url=video_instance.webpage_url,
#         duration_string=video_instance.duration_string,
#     )

#     for audio_data in video_instance.formats.audio:
#         audio_format = AudioFormat(
#             format=audio_data.format,
#             format_note=audio_data.format_note,
#             ext=audio_data.ext,
#             protocol=audio_data.protocol,
#             resolution=audio_data.resolution,
#             url=audio_data.url,
#             filesize=audio_data.filesize,
#         )
#         video.audio_formats.append(audio_format)

#     for video_data in video_instance.formats.video:
#         video_format = VideoFormat(
#             format=video_data.format,
#             format_note=video_data.format_note,
#             ext=video_data.ext,
#             protocol=video_data.protocol,
#             resolution=video_data.resolution,
#             url=video_data.url,
#             filesize=video_data.filesize,
#         )
#         video.video_formats.append(video_format)

#     try:
#         with session:
#             session.add(video)
#             session.commit()

#     except Exception as e:
#         return f"error: {e}"
