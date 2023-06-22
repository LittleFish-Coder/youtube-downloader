import os
from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip


def progress_callback(stream, chunk, bytes_remaining):
    size = stream.filesize
    progress = (size - bytes_remaining) / size * 100
    print(f"{progress:.2f}% downloaded")


# specify the url of the video to be downloaded
url = "https://youtu.be/oYyWoovxq-8"
# Create a YouTube object
yt = YouTube(url, on_progress_callback=progress_callback, use_oauth=True)

# get the video stream with progressive=True and choose the last one
video_stream = yt.streams.filter(progressive="True").last()
# download the video
video_stream.download(filename=f"{yt.title}.mp4")