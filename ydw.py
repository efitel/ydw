import pytube

# Prompt the user to enter the YouTube URL
url = input("Enter the YouTube video URL: ")

# Create a YouTube object
youtube = pytube.YouTube(url, use_oauth=True, allow_oauth_cache=True)

# Get the available video streams
video_streams = youtube.streams.filter(progressive=True)

# Print the available video streams and ask the user to select one
print("Available video streams:")
for i, stream in enumerate(video_streams):
    print(f"{i+1}. {stream.resolution}")
selected_stream_index = int(input("Select a video stream (enter the number): ")) - 1
selected_stream = video_streams[selected_stream_index]

# Download the selected video stream to the current directory
print(f"Downloading '{selected_stream.default_filename}'...")
selected_stream.download()
print("Download complete.")
