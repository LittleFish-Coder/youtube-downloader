import streamlit as st
from moviepy.editor import *
from pytube import YouTube


# output folder
output_folder = "output"

# create the output folder if it does not exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


def progress_callback(stream, chunk, bytes_remaining):
    size = stream.filesize
    progress = (size - bytes_remaining) / size * 100
    print(f"{progress:.2f}% downloaded")


st.title("YouTube Downloader")
mp4_url = st.text_input("Enter MP4 URL:")
if "youtube.com" in mp4_url or "youtu.be" in mp4_url:
    try:
        # Create a YouTube object using the video URL
        yt = YouTube(mp4_url, on_progress_callback=progress_callback, use_oauth=True)

        # Display the video details to the user
        st.write("Title:", yt.title)
        st.write("Duration:", yt.length, "seconds")
        st.write("Views:", yt.views)

        # Add a download button for the video in MP3 format
        if st.button("Download"):
            try:
                with st.spinner("Downloading..."):
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
                        f"{output_folder}/{yt.title}.mp4",
                        codec="libx264",
                        audio_codec="aac",
                        fps=30,
                    )

                    # Display a success message to the user
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
    if st.button("Download"):
        # Create a YouTube object using the video URL
        yt = YouTube(mp4_url, on_progress_callback=progress_callback, use_oauth=True)

        # Display the video details to the user
        st.write("Title:", yt.title)
        st.write("Duration:", yt.length, "seconds")
        st.write("Views:", yt.views)
        try:
            with st.spinner("Downloading..."):
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
                    f"{output_folder}/{yt.title}.mp4",
                    codec="libx264",
                    audio_codec="aac",
                    fps=30,
                )

                # Display a success message to the user
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
