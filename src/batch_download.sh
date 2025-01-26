#!/bin/bash

# Check if the URL file exists
URL_FILE="urls.txt"
if [ ! -f "$URL_FILE" ]; then
    echo "File $URL_FILE does not exist. Please create it with your list of URLs."
    exit 1
fi

# Read each URL from the file and download using the Python script
while IFS= read -r URL; do
    if [ -n "$URL" ]; then
        echo "Processing URL: $URL"
        python video_downloader_fast.py --url "$URL"
    fi
done < "$URL_FILE"

echo "All videos processed!"
