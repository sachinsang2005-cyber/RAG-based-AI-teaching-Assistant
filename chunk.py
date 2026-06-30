import os
import json

files=os.listdir("jsons")

for file in files:
    with open(f"jsons/{file}","r",encoding="utf-8") as f:
        data=json.load(f)


        chunks=[]
        current_text=""
        start_time=data[0]["start"]


        for segment in data:
            current_text+=" "+segment["text"]


        # Create chunk after about 500 characters
            if len(current_text) >= 500:

                chunks.append({
                    "start": start_time,
                    "end": segment["end"],
                    "text": current_text.strip()
                    })

                current_text = ""

                if segment != data[-1]:
                    start_time = segment["end"]

    if current_text:
        chunks.append({
            "start":start_time,
            "end":data[-1]["end"],
            "text":current_text.strip()
        })

    file_name=file.split(".")[0]

    with open(
        f"chunks/{file_name}_chunk.json",
        "w",
        encoding="utf-8") as f:
        json.dump(chunks , f, indent=4)

    print(f"{file_name} are chunked....")