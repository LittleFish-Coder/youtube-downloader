# Youtube Downloader
This is a youtube downloader that downloads the video from the youtube link.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required packages.
The packages are listed in the requirements.txt file: 
* pytube
* yt-dlp
* moviepy

Use the following command to install the packages.
```bash
pip install -r requirements.txt
```
or use pip3 depending on your system.
```bash
pip3 install -r requirements.txt
```

## Contents
There are total 4 files/scripts in this project.
* [youtube_downloader.py](#youtube_downloaderpy) (Recommended)
* [youtube_downloader_video_fast.py](#youtube_downloader_video_fastpy)
* [youtube_downloader.bash](#youtube_downloaderbash) (for MacOS and Linux)
* [youtube_downloader.bat](#youtube_downloaderbat) (for Windows)

## Usage
In general, it is recommended to use the youtube_downloader.py script as first priority.
If you want to download the video faster(but lower resolution) then use the youtube_downloader_video_fast.py script.
You can tell the difference when you try to download youtube shorts.
The youtube_downloader.py script performs better in contrast to the bash and bat scripts.

### youtube_downloader.py
change the url variable to the youtube link at line 13.
```python
url = "https://www.youtube.com/watch?v=9bZkp7q19f0"
```
Then run the script.
```bash
python youtube_downloader.py
```
It will then download the video with 1080p resolution(if available) and the audio with the highest quality available.

### youtube_downloader_video_fast.py
change the url variable to the youtube link at line 11.
```python
url = "https://www.youtube.com/watch?v=9bZkp7q19f0"
```
Then run the script.
```bash
python youtube_downloader_video_fast.py
```
It will then download the video faster but with 720p resolution(mostly) and the audio with the highest quality available.

### youtube_downloader.bash
run the script.
```bash
bash youtube_downloader.bash
```
It will then ask for the youtube link.
Enter the youtube link and press enter.
It will then download the video with 1080p resolution(if available) and the audio with the highest quality available.

### youtube_downloader.bat
run the script.
```bash
youtube_downloader.bat
```
It will then ask for the youtube link.
Enter the youtube link and press enter.
It will then download the video with 1080p resolution(if available) and the audio with the highest quality available.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
