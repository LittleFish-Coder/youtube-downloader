from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip


def progress_callback(stream, chunk, bytes_remaining):
    size = stream.filesize
    progress = (size - bytes_remaining) / size * 100
    print(f"{progress:.2f}% downloaded")


url = "https://youtu.be/JWwJckdNerg"
# 建立YouTube對象
yt = YouTube(url, on_progress_callback=progress_callback)

# 獲取最高解析度的影片流和音訊流
video_stream = yt.streams.get_highest_resolution()
audio_stream = yt.streams.get_audio_only()

video_stream.download(filename='Video.mp4')
audio_stream.download(filename='Audio.mp3')

# # 將視頻和音訊文件合併成一個完整的影片文件
video = VideoFileClip('Video.mp4')
audio = AudioFileClip('Audio.mp3')
final_video = video.set_audio(audio)
final_video.write_videofile(f"{yt.title}.mp4")
