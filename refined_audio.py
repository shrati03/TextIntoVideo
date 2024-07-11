from pydub import AudioSegment

# AudioSegment.ffmpeg = r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\ffmpeg.exe"
# Load the audio file
audio = AudioSegment.from_mp3("Audio.mp3")

# Define the speed increase factor (e.g., 1.5 for 1.5x speed)
speed_factor = 1.5  # Increase speed by a factor of 1.5

# Apply the speed increase effect
faster_audio = audio.speedup(playback_speed=speed_factor)

# Export the modified audio to a new file
faster_audio.export("output_audio.mp3", format="mp3")
