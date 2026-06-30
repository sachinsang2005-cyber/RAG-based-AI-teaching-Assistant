# import whisper
# print("whisper installed successfully...")

import os
import subprocess

files=os.listdir("videos")
for file in files:
    file_name=file.split(".")[0]
    subprocess.run([
        r"C:\Program Files (x86)\ffmpeg\bin\ffmpeg.exe",
        "-i",f"videos/{file}" , 
        f"audios/{file_name}.mp3"])