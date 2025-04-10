from pytubefix import YouTube
from pytubefix.cli import on_progress
from pydub import AudioSegment
import os

url = "https://youtu.be/DzLv6W4aYlA?si=n60ZC5lZ4WNiQtt1"

yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

# Download the audio stream
ys = yt.streams.get_audio_only()
downloaded_file_path = ys.download()

def convert_mp4_to_mp3(input_file):
    # Load the M4A file
    audio = AudioSegment.from_file(input_file, format='m4a')
    
    # Create the output file name by replacing the extension
    output_file = input_file.rsplit('.', 1)[0] + '.mp3'
    
    # Export as MP3
    audio.export(output_file, format='mp3')
    print(f"Converted '{input_file}' to '{output_file}'")
    
    # Delete the original M4A file
    os.remove(input_file)
    print(f"Deleted the original file: '{input_file}'")

# Convert the downloaded file to MP3
convert_mp4_to_mp3(downloaded_file_path)