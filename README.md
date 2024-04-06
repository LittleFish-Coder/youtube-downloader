# Youtube Downloader

This is a youtube downloader that downloads the video from the youtube link.

## Installation

Clone the repository to your local machine or download the zip file.

```bash
git clone https://github.com/LittleFish-Coder/youtube-downloader.git
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required packages.

The packages are listed in the requirements.txt file:

- pytube
- yt-dlp
- moviepy

Use the following command to install the packages.

```bash
pip install -r requirements.txt
```

Or use pip3 depending on your system.

```bash
pip3 install -r requirements.txt
```

## Contents

There are total 4 files/scripts in this project.

- [video_downloader.py](#video_downloaderpy) (Recommended)
- [video_downloader_fast.py](#video__downloader_fastpy)
- [video_downloader.bash](#video__downloaderbash) (for MacOS and Linux)
- [video_downloader.bat](#video_downloaderbat) (for Windows)

## Usage

In general, it is recommended to use the video_downloader.py script as first priority.
The video_downloader.py script performs better in contrast to the bash and bat scripts.

### video_downloader.py

Change the url variable to the youtube link at line 13.

```python
url = "https://www.youtube.com/watch?v=9bZkp7q19f0"
```

Then run the script.

```bash
python video_downloader.py
```

It will then download the video with 1080p resolution(if available) and the audio with the highest quality available.

### video_downloader_fast.py

Change the url variable to the youtube link at line 11.

```python
url = "https://www.youtube.com/watch?v=9bZkp7q19f0"
```

Then run the script.

```bash
python video_downloader_fast.py
```

It will then download the video faster but with 720p resolution(mostly) and the audio with the highest quality available.

### video_downloader.bash

Run the script.

```bash
bash video_downloader.bash
```

It will ask for the youtube link.

Enter the youtube link and press enter, then it will download the video with 1080p resolution(if available) and the audio with the highest quality available.

### video_downloader.bat

Run the script.

```bash
video_downloader.bat
```

It will ask for the youtube link.

Enter the youtube link and press enter, then it will download the video with 1080p resolution(if available) and the audio with the highest quality available.
