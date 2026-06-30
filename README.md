# RAG Based AI Teaching Assistant

## Overview

RAG (Retrieval-Augmented Generation) based AI Teaching Assistant that allows students to ask questions from lecture videos and get accurate answers with source and timestamp references.

The system converts lecture videos into text, creates chunks, generates embeddings, stores them in ChromaDB, retrieves relevant content, and uses Gemini to generate answers.

---

## Features

- Convert lecture videos to audio using FFmpeg
- Transcribe audio using OpenAI Whisper
- Create timestamp-based chunks
- Generate embeddings using Sentence Transformers
- Store embeddings in ChromaDB
- Retrieve relevant lecture content
- Answer questions using Gemini 2.5 Flash
- Display source file and timestamp

---

## Tech Stack

### AI Models
- Whisper (Speech to Text)
- all-MiniLM-L6-v2 (Embeddings)
- Gemini 2.5 Flash (LLM)

### Database
- ChromaDB

### Language
- Python

---

## Project Structure

```
RAG Based AI Teaching Assistant/
│
├── videos/
├── audios/
├── jsons/
├── chunks/
├── db/
│
├── process_video.py
├── tts.py
├── chunk.py
├── vectordb.py
├── chat.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Workflow

### Step 1
Video → Audio

```text
videos/
↓
process_video.py
↓
audios/
```

### Step 2
Audio → Text

```text
audios/
↓
Whisper
↓
Transcript
```

### Step 3
Transcript → Chunks

```text
Transcript
↓
chunk.py
↓
chunks/
```

### Step 4
Chunks → Embeddings

```text
Chunks
↓
Sentence Transformer
↓
Embeddings
```

### Step 5
Store Embeddings

```text
Embeddings
↓
ChromaDB
↓
db/
```

### Step 6
Question Answering

```text
Question
↓
Embedding
↓
ChromaDB Retrieval
↓
Relevant Chunks
↓
Gemini
↓
Answer + Source + Timestamp
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd RAG-Based-AI-Teaching-Assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
genAPI=YOUR_GEMINI_API_KEY
```

---

## Run

Create database:

```bash
python vectordb.py
```

Start chatbot:

```bash
python chat.py
```

Example:

```text
Ask Question:
What is a Maglev train?
```

Output:

```text
Answer:
Maglev trains use magnetic levitation...

Source:
maglev_chunk.json

Time:
00:00 - 00:42
```

---

## Future Enhancements

- Streamlit Web Interface
- Multiple Lecture Support
- PDF Support
- Chat History
- Multi-language Support
- Lecture Recommendation System

---

## Author

Abhishek Fulpagare

Computer Engineering Student
Pimpri Chinchwad College of Engineering & Research, Pune
