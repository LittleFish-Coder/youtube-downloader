import tkinter as tk
import pytube
from tkinter import ttk
import threading

class DownloadThread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        yt = pytube.YouTube(self.url)
        stream = yt.streams.filter(only_audio=True).first()
        stream.download(filename=f"{yt.title}.mp3")
        download_button["state"] = "normal"
        progress_bar.stop()

def download_audio():
    url = url_entry.get()
    download_button["state"] = "disabled"
    progress_bar.start()
    download_thread = DownloadThread(url)
    download_thread.start()

root = tk.Tk()
root.title("YouTube Audio Downloader")

url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.pack()

url_entry = tk.Entry(root)
url_entry.pack()

download_button = tk.Button(root, text="Download Audio", command=download_audio)
download_button.pack()

progress_bar = ttk.Progressbar(root, mode='indeterminate')
progress_bar.pack()

root.mainloop()
