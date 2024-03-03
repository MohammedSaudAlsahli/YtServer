from fastapi import FastAPI

from ytserver.functions.extract_info import extract_video_info


app = FastAPI()


@app.get("/")
def root():
    return {"message": "add video url to get download link"}


@app.get("/{video_url:path}")
async def root(video_url):
    video = extract_video_info(video_url)

    return video


# url = "https://x.com/OwlLunch/status/1750623050557517958?s=20"  # single video

# url = "https://x.com/AustinKonenski/status/1578105871518773248?s=20"  # many videos in one tweet

# url = "https://x.com/eruggggggure/status/1752686213331358058?s=20"  # main video and qouat video

# url = "https://x.com/Osama11/status/1752688031755018709?s=20"  # images only

# url = "https://www.youtube.com/watch?v=FtqWCo1_I4g&list=PLnKe36F30Y4bamRi07AOYS1qGDv_2MGMW"  # youtube list

# url = "https://www.tiktok.com/@x9l.m/video/7309714409826307336"
# v = extract_video_info(url)
# print(v)
