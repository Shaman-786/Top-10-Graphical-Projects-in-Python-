import sys
from moviepy.editor import VideoFileClip

if __name__ == "__main__":
    video_path = sys.argv[1]  # Get the video path from command-line arguments
    clip = VideoFileClip(video_path)
    clip.preview()
