from pytube import YouTube


def progress_callback(stream, chunk, bytes_remaining):
    size = stream.filesize
    progress = (size - bytes_remaining) / size * 100
    print(f"{progress:.2f}% downloaded")


# specify the url of the video to be downloaded
url = "https://youtu.be/0QlYn3L7B1g"
# Create a YouTube object
yt = YouTube(url, on_progress_callback=progress_callback, use_oauth=True)

# Filter the streams to get the one with only audio (highest bitrate)
audio_stream = yt.streams.filter(only_audio=True, file_extension="mp4").first()

# Download the audio with the highest bitrate and AAC codec
audio_stream.download(filename=f"{yt.title}.mp4")

print("Download completed.")
