# INSIGHTLENS-Video-Intelligence-Agent-with-RAG

InsightLens is an AI-powered video intelligence system that transforms long video or audio content into structured, actionable insights. It accepts YouTube links or local media files, extracts audio, transcribes speech using models like OpenAI Whisper and Sarvam AI, and generates concise summaries, titles, action items, key decisions, and open questions.

The system leverages Retrieval-Augmented Generation (RAG) with LangChain, ChromaDB, and Mistral to enable conversational question answering over the transcript. A user-friendly Streamlit interface allows users to interact with meeting content, making information retrieval faster and more efficient.


## System Architecture

                    INPUT SOURCE
                          │
         ┌────────────────┴────────────────┐
         │                                 │
   YouTube URL                     Local Video/File
         │                                 │
         └──────────────┬──────────────────┘
                        │
                Audio Extraction
                        │
                WAV Conversion
                        │
                 Audio Chunking
                        │
        ┌───────────────┴───────────────┐
        │                               │
      Whisper                      Sarvam AI
     (English)                    (Hinglish)
        │                               │
        └───────────────┬───────────────┘
                        │
                 Full Transcript
                        │
      ┌─────────────────┼─────────────────┐
      │                 │                 │
      ▼                 ▼                 ▼

  Summarizer     Transcript Analyzer   Vector Store
      │                 │                 │
      │                 │            ChromaDB
      │                 │                 │
      ▼                 ▼                 ▼

 Meeting Title    Action Items       Embeddings
 Summary          Decisions          Retriever
 Questions             │                 │
      └────────────────┼─────────────────┘
                       ▼
               Mistral RAG Chain
                       ▼
             Conversational Chat
                       ▼
                  Streamlit UI


## Demo Video Link: https://drive.google.com/drive/folders/1f6sWCuSBbzKQpa8LTugrHjcsRD_9CMV_?usp=sharing
