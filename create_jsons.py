import whisper
import os
import json

model=whisper.load_model("base")
files = os.listdir("audios")
for file in files:
    result=model.transcribe(f"audios/{file}")
    data = []
    for segment in result["segments"]:
        data.append({
            "start":segment["start"],
            "end":segment["end"],
            "text":segment["text"]
        })

    file_name = file.split(".")[0]
    with open(f"jsons/{file_name}.json","w",encoding="utf-8") as f:
        json.dump(data , f, indent=4)

    print(f"{file_name} created successfully...")