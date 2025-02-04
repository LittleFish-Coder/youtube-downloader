import argparse
from pytubefix import YouTube
from pytubefix.cli import on_progress
import re

def download_video(url):
    """Download the YouTube video from the provided URL."""
    try:
        yt = YouTube(url, on_progress_callback=on_progress, use_oauth=True)
        stream = yt.streams.filter(progressive=True).last()
        if stream:
            stream.download(filename=f"{yt.title}.mp4")
            print(f"Video '{yt.title}' downloaded successfully.")
        else:
            print("No suitable stream found for the video.")
    except Exception as e:
        print(f"An error occurred: {e}")

def reformat_url(url):
    """Reformat the YouTube video URL."""
    youtu_be_pattern = re.compile(r"^https?://youtu\.be/")
    youtube_pattern = re.compile(r"^https?://(www\.)?youtube\.com/watch\?v=([^&]+)")

    if youtu_be_pattern.match(url):
        return url
    elif youtube_pattern.match(url):
        video_id = youtube_pattern.match(url).group(2)
        return f"https://youtu.be/{video_id}"
    else:
        return url

def main():
    parser = argparse.ArgumentParser(description="Download YouTube videos.")
    parser.add_argument("--url", default="https://youtu.be/oYyWoovxq-8", help="URL of the YouTube video to download.")
    args = parser.parse_args()
    # Call the download_video function with the provided URL
    download_video(reformat_url(args.url))

if __name__ == "__main__":
    main()