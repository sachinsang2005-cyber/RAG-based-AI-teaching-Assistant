from sentence_transformers import SentenceTransformer
import os
import json

model=SentenceTransformer("all-MiniLM-L6-v2")
files = os.listdir("chunks")
for file in files:
    with open(f"chunks/{file}" , "r" , encoding="utf-8") as f:
        data = json.load(f)

    for chunk in data:
        embedding=model.encode(chunk["text"])
        # print(len(embedding))
        print(embedding[:10])


