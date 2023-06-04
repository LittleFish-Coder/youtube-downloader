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

# get the video stream with certain resolution
video_stream = yt.streams.filter(res="1080p").first()
# download the video
video_stream.download(filename="Video.mp4")

# get the audio stream
audio_stream = yt.streams.get_audio_only()
# download the audio
audio_stream.download(filename="Audio.mp3")

# Merge the video and audio files into a single video file
video = VideoFileClip('Video.mp4')
audio = AudioFileClip('Audio.mp3')
final_video = video.set_audio(audio)
final_video.write_videofile(f"{yt.title}.mp4", codec="libx264", audio_codec="aac")

# Then delete the video and audio files in the local directory
# os.remove("Audio.mp3")
# os.remove("Video.mp4")
