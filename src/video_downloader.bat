@echo off
@REM This script requires yt-dlp to be installed

@REM REM Prompt the user to input the YouTube URL
set /p youtube_url=Please input the YouTube URL: 

@REM REM Download the video using yt-dlp
yt-dlp -f "bestvideo[ext=mp4][height<=1080]+bestaudio[ext=m4a]" -o "%%(title)s.%%(ext)s" --force-overwrites %youtube_url%

pause