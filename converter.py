from pytubefix import YouTube
from pytubefix.cli import on_progress
from pydub import AudioSegment
import os

url = "Your URL Video"

yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

# Downloading the audio from the url
ys = yt.streams.get_audio_only()
downloaded_file_path = ys.download()

def convert_m4a_to_mp3(input_file):
    # Load the m4a file from download
    audio = AudioSegment.from_file(input_file, format='m4a')
    
    # Create the output file by change the extension
    output_file = input_file.rsplit('.', 1)[0] + '.mp3'
    
    # Export file as mp3
    audio.export(output_file, format='mp3')
    print(f"Converted '{input_file}' to '{output_file}'")
    
    # Deleting the original m4a file
    os.remove(input_file)
    print(f"Deleted the original file: '{input_file}'")

# Convert the downloaded file to MP3
convert_m4a_to_mp3(downloaded_file_path)
