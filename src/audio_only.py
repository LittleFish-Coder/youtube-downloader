from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip


def progress_callback(stream, chunk, bytes_remaining):
    size = stream.filesize
    progress = (size - bytes_remaining) / size * 100
    print(f"{progress:.2f}% downloaded")


# specify the url of the video to be downloaded
url = "https://youtu.be/oYyWoovxq-8?si=W2AYTQbwYwD30sQK"
# Create a YouTube object
yt = YouTube(url, on_progress_callback=progress_callback, use_oauth=True)

# Filter the streams to get the one with only audio (highest bitrate)
audio_stream = yt.streams.filter(only_audio=True).first()

print(f"Downloading {yt.title}...")
audio = AudioFileClip(audio_stream.url)
audio.write_audiofile(f"{yt.title}.mp3")
print("Download completed.")
