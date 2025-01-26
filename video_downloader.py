import os
from pytubefix import YouTube
from pytubefix.cli import on_progress
from moviepy.editor import VideoFileClip, AudioFileClip

# output folder
output_folder = "output"

# create the output folder if it does not exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# specify the url of the video to be downloaded
url = "https://youtu.be/9EAR3kh2STg"
# Create a YouTube object
yt = YouTube(url, on_progress_callback=on_progress, use_oauth=True)

# get the video stream with certain resolution
video_stream = yt.streams.filter(res="1080p").first()
# if the video stream is not available, get the highest resolution video stream
if video_stream is None:
    video_stream = yt.streams.get_highest_resolution()
# download the video
video_stream.download(filename="Video.mp4")

# get the audio stream
audio_stream = yt.streams.get_audio_only()
# download the audio
audio_stream.download(filename="Audio.mp3")

# Merge the video and audio files into a single video file
video = VideoFileClip("Video.mp4")
audio = AudioFileClip("Audio.mp3")
# set the audio of the video as the audio file
merge_video = video.set_audio(audio)
# specify the output video format codec as H.264 and audio codec as AAC
merge_video.write_videofile(
    f"{output_folder}/{yt.title}.mp4", codec="libx264", audio_codec="aac", fps=30
)

# Then delete the video and audio files in the local directory
os.remove("Audio.mp3")
os.remove("Video.mp4")
