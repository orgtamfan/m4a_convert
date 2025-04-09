from pydub import AudioSegment
import tkinter as tk
from tkinter import filedialog
from pytubefix.cli import on_progress

def convert_mp4_to_mp3(input_file):
    # Load the MP4 file
    audio = AudioSegment.from_file(input_file, format='m4a')
    
    # Create the output file name by replacing the extension
    output_file = input_file.rsplit('.', 1)[0] + '.mp3'
    
    # Export as MP3
    audio.export(output_file, format='mp3')
    print(f"Converted '{input_file}' to '{output_file}'")

def open_file_dialog():
    # Create a Tkinter root window (it won't be shown)
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open a file dialog to select the MP4 file
    input_file = filedialog.askopenfilename(title="Select MP4 file", filetypes=[("MP4 files", "*.m4a")])
    
    if input_file:  # Check if a file was selected
        convert_mp4_to_mp3(input_file)

# Run the file dialog
open_file_dialog()