from pytubefix import YouTube
from pytubefix.cli import on_progress
 
url = "https://youtu.be/RHWcG2uFNFY?si=Ua75CQp90Kn2EUFS"
 
yt = YouTube(url, on_progress_callback = on_progress)
print(yt.title)
 
ys = yt.streams.get_audio_only()
ys.download()