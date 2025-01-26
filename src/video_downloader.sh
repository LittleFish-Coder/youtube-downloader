#!/bin/bash

# Shell script to download YouTube videos using video_downloader.py

# Prompt the user to enter a YouTube URL
read -p "Enter the YouTube URL: " URL

# Check if the URL is not empty
if [ -z "$URL" ]; then
    echo "You must provide a URL!"
    exit 1
fi

# Call the Python script with the entered URL
python video_downloader_fast.py --url "$URL"
