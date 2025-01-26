@echo off
@REM This script calls the Python file to download YouTube videos

@REM Prompt the user to input the YouTube URL
set /p youtube_url=Please input the YouTube URL: 

@REM Call the Python script with the entered URL
python video_downloader_fast.py --url %youtube_url%

@REM Pause to allow the user to see the output
pause
