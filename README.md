# How to use the app

To install the app run:
`pip install ytserver`

to run the server, run: `ytserver`

It will run on the `0.0.0.0` at port `8000`

to use the server just make get requiest at `http://0.0.0.0:8000/<your video url>` and it return a json of the video information

```json
    [
        {
        "extractor_key": "Twitter",
        "display_id": "1765708518038941924",
        "thumbnail": "https://pbs.twimg.com/amplify_video_thumb/1765708420500402176/img/3jLKkb4EKAz0NlXT.jpg?name=small",
        "title": "فيديوهات وروابط الأحداث - إدارة التحريات والبحث الجنائي بشرطة منطقة الرياض تقبض على شخص لانتحاله صفة غير صحيحة.",
        "description": "إدارة التحريات والبحث الجنائي بشرطة منطقة الرياض تقبض على شخص لانتحاله صفة غير صحيحة. https://t.co/fqGvREBNEI",
        "uploader_url": "https://twitter.com/videohat_1",
        "webpage_url": "https://twitter.com/videohat_1/status/1765708518038941924",
        "duration_string": "16",
        "formats": {
        "audio": [],
        "video": [
        {
        "format": "http-288 - 302x270",
        "format_note": null,
        "ext": "mp4",
        "protocol": "https",
        "resolution": "302x270",
        "url": "https://video.twimg.com/amplify_video/1765708420500402176/vid/avc1/302x270/MFtQlpDZCyxkCCKZ.mp4?tag=14",
        "filesize": null
        },
        {
        "format": "http-832 - 404x360",
        "format_note": null,
        "ext": "mp4",
        "protocol": "https",
        "resolution": "404x360",
        "url": "https://video.twimg.com/amplify_video/1765708420500402176/vid/avc1/404x360/OJcGw6iIYz4P9Lg_.mp4?tag=14",
        "filesize": null
        },
        {
        "format": "http-2176 - 576x512",
        "format_note": null,
        "ext": "mp4",
        "protocol": "https",
        "resolution": "576x512",
        "url": "https://video.twimg.com/amplify_video/1765708420500402176/vid/avc1/576x512/MJBW8Ku18AHg5uD8.mp4?tag=14",
        "filesize": null
        }
        ]
        },
        "upload_date": "20240307"
        }
    ]
```