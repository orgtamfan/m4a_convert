from pytubefix import YouTube
from pytubefix.cli import on_progress
from pydub import AudioSegment
import os

url = "https://youtu.be/DzLv6W4aYlA?si=_KfLhWuMaoNE79_h"
directory = "C:/Users/A S U S/OneDrive/Music/Playlists" 

yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

# Downloading the audio from the url
ys = yt.streams.get_audio_only()
file_path = ys.download()

def convert_mp4_to_mp3(input_file, output_dir):
    # Load the m4a file
    audio = AudioSegment.from_file(input_file, format='m4a')
    
    # Create the output file name by replacing the extension and adding the output directory
    output = os.path.join(output_dir, os.path.basename(input_file).rsplit('.', 1)[0] + '.mp3')
    
    # Export as mp3
    audio.export(output, format='mp3')
    print(f"Converted '{input_file}' to '{output}'")
    
    # Delete the original m4a file
    os.remove(input_file)
    print(f"Deleted the original file: '{input_file}'")

# Convert the downloaded file to MP3 and specify the output directory
convert_mp4_to_mp3(file_path, directory)
