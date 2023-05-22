import yt_dlp as yt
import json

def extract_ytlink(URL):
    # ℹ️ See help(yt_dlp.YoutubeDL) for a list of available options and public functions
    ydl_opts = {"format":"wa", 'outtmpl': './downloads/%(id)s.%(ext)s'}
    with yt.YoutubeDL(ydl_opts) as ydl:
        info = ydl.download(URL)