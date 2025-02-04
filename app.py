import streamlit as st
from moviepy.editor import *
from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
from collections import defaultdict
import re


# output folder
output_folder = "output"

# create the output folder if it does not exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

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


st.title("YouTube Downloader")
url = st.text_input("Enter Youtube URL:")
if "youtube.com" in url or "youtu.be" in url:
    try:
        url = reformat_url(url)
        
        # Create a YouTube object using the video URL
        yt = YouTube(url, on_progress_callback=on_progress, use_oauth=True)

        # Display the video details to the user
        st.markdown(f"## {yt.title}")

        # show the picture of the video
        st.image(yt.thumbnail_url)

        yt_streams = yt.streams

        # Collect all available resolutions
        available_resolutions = set()
        for stream in yt_streams.filter(type="video"):
            available_resolutions.add(stream.resolution)

        resolutions = ["144p", "240p", "360p", "480p", "720p", "1080p", "1440p", "2160p"]
        # extract the available streams with the selected resolutions
        resolutions = [res for res in resolutions if res in available_resolutions]


        # dropdown to select the resolution
        resolution = st.selectbox("Select resolution", resolutions, index=resolutions.index("480p") if "480p" in resolutions else 0)

        # Add a download button for the video in MP3 format
        if st.button("Download") and resolution is not None:
            try:
                with st.spinner("Downloading..."):
                    # get the video stream with certain resolution
                    video_stream = yt.streams.filter(res=resolution).first()
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
                        f"{output_folder}/{yt.title}.mp4",
                        codec="libx264",
                        audio_codec="aac",
                        fps=30,
                    )

                st.success("Download complete!")
            except:
                st.error("Download failed.")

            with open(f"{output_folder}/{yt.title}.mp4", "rb") as f:
                byte_content = f.read()
                st.download_button(
                    label="Download mp4",
                    data=byte_content,
                    file_name=f"{yt.title}.mp4",
                    mime="audio/mpeg",
                )
    except:
        # Display an error message if the video cannot be downloaded or converted
        st.error("Download failed!")
else:
    st.warning("Please enter a valid YouTube URL.")
