# this script needs to be run in the terminal and yt-dlp needs to be installed first

# get the youtube video name
# yt-dlp --get-title https://youtu.be/PHwayuLBKLw

# get the youtube video info
# yt-dlp -F https://youtu.be/PHwayuLBKLw

# if you want to write the video out with its title and specify the video format, you can use the command below:
# yt-dlp -o "%(title)s.%(ext)s" -f mp4 https://youtu.be/PHwayuLBKLw

# get the mp4 file with 1080p
# yt-dlp -f "bestvideo[ext=mp4][height<=1080]" -o "video.mp4" --force-overwrites https://youtu.be/PHwayuLBKLw

# download the most general codec audio
# yt-dlp -f "bestaudio[ext=m4a]" -o "audio.m4a" --force-overwrites https://youtu.be/PHwayuLBKLw

# get the mp4 file with 1080p and the most general codec audio
# yt-dlp -f "bestvideo[ext=mp4][height<=1080]+bestaudio[ext=m4a]" --merge-output-format mp4 -o "%(title)s.%(ext)s" --force-overwrites https://youtu.be/PHwayuLBKLw

# make the youtube url as a variable, which will later be given by the user
yt-dlp -f "bestvideo[ext=mp4][height<=1080]+bestaudio[ext=m4a]" -o "%(title)s.%(ext)s" --force-overwrites $1