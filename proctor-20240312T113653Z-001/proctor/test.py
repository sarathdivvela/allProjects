from moviepy.editor import *

# Load the WebM file
webm_clip = VideoFileClip(r"C:\Users\GANESH\OneDrive\Documents\proctor-20240312T113653Z-001\proctor\sample.webm")

# Write the clip to an MP4 file
webm_clip.write_videofile("output.mp4", codec="libx264")