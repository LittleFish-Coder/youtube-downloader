import os
from pytubefix import YouTube
from pytubefix.cli import on_progress
from moviepy.editor import VideoFileClip, AudioFileClip
import re
import argparse

def download_video(url, output_folder="output"):
    """Download the YouTube video from the provided URL."""

    # Create the output directory if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        # Create a YouTube object
        yt = YouTube(url, on_progress_callback=on_progress, use_oauth=True)

        # get the video stream with certain resolution
        video_stream = yt.streams.filter(res="1080p").first()
        # if the video stream is not available, get the highest resolution video stream
        if video_stream is None:
            video_stream = yt.streams.get_highest_resolution()
        # download the video
        video_stream.download(filename=f"{output_folder}/video.mp4")

        # get the audio stream
        audio_stream = yt.streams.get_audio_only()
        # download the audio
        audio_stream.download(filename=f"{output_folder}/audio.mp3")

        # Merge the video and audio files into a single video file
        video = VideoFileClip(f"{output_folder}/video.mp4")
        audio = AudioFileClip(f"{output_folder}/audio.mp3")
        # set the audio of the video as the audio file
        merge_video = video.set_audio(audio)
        # specify the output video format codec as H.264 and audio codec as AAC
        merge_video.write_videofile(
            f"{output_folder}/{yt.title}.mp4", codec="libx264", audio_codec="aac", fps=30
        )
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
    parser.add_argument("--output", default="output", help="Output folder for the downloaded video.")
    args = parser.parse_args()
    # Call the download_video function with the provided URL
    download_video(reformat_url(args.url), args.output)

if __name__ == "__main__":
    main()
