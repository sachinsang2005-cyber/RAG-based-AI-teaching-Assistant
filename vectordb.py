from sentence_transformers import SentenceTransformer
import chromadb
import os 
import json

model=SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="db")

collection = client.get_or_create_collection(name="lectures")

files = os.listdir("chunks")

for file in files:
    with open(f"chunks/{file}" , "r" , encoding="utf-8") as f:
        data = json.load(f)

    for i,chunk in enumerate(data):
        embedding=model.encode(
            chunk["text"]
        ).tolist()

        collection.add(
            ids=[f"{file}_{i}"],
            embeddings=[embedding],
            documents=[chunk["text"]],
            metadatas = [{
                    "source" : file,
                    "start"  : chunk["start"],
                    "end" : chunk["end"]
                }]
            )

print("all chunks are stored successfully...")