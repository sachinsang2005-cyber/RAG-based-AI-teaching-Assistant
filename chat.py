from sentence_transformers import SentenceTransformer
import chromadb
import google.generativeai as genai
from dotenv import load_dotenv
import os

# load api
load_dotenv()
api_key=os.getenv("genAPI")
genai.configure(api_key=api_key)


# models
embed_model=SentenceTransformer("all-MiniLM-L6-v2")
llm=genai.GenerativeModel("models/gemini-2.5-flash")


# chromadb
client=chromadb.PersistentClient(path="db")
collection = client.get_collection("lectures")

# time format function
def format_time(seconds):
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes:02d}:{seconds:02d}"




while True:
    question = input("Ask question related to videos:")
    if question.lower()=="exit":
        break

    # question to embeddings
    question_embed=embed_model.encode(
        question
    ).tolist()


    # search relevant chunks
    result=collection.query(
        query_embeddings=[question_embed],
        n_results=3
    )


    # metadata 
    metadata = result["metadatas"][0]
    source=metadata[0]["source"]
    start=metadata[0]["start"]
    end=metadata[0]["end"]

    # context
    context = "\n".join(result["documents"][0])

    # prompt
    prompt=f"""
    you are helpful AI teaching assistant
    so answer the question using provided context.

    Context:{context}

    Question:{question}

    """

    # gemini response
    response = llm.generate_content(prompt)

    print("\nAnswer : ")
    print(response.text)
    print("\n Source : " , source.split("_chunk")[0])
    print(f"Time : {format_time(start)} - {format_time(end)}")