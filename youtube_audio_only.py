from pytube import YouTube


def progress_callback(stream, chunk, bytes_remaining):
    size = stream.filesize
    progress = (size - bytes_remaining) / size * 100
    print(f"{progress:.2f}% downloaded")


# specify the url of the video to be downloaded
url = "https://youtu.be/oYyWoovxq-8"
# Create a YouTube object
yt = YouTube(url, on_progress_callback=progress_callback, use_oauth=True)

# download the audio only with AAC codec
yt.streams.filter(only_audio=True).first().download(filename=f"{yt.title}.mp3")
