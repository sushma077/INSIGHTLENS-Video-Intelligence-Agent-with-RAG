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


## Project Structure
        INSIGHTLENS-Video-Intelligence-Agent-with-RAG/
        │
        ├── helpers/
        │   ├── audio_extractor.py        # Handles audio extraction from YouTube/local files
        │   └── __pycache__/              # Compiled Python files
        │
        ├── visionRag/
        │   ├── meeting_summarizer.py     # Generates summaries and titles using LLM
        │   ├── rag_pipeline.py           # Implements Retrieval-Augmented Generation (RAG)
        │   ├── retrieval_store.py        # Vector database creation and semantic retrieval
        │   ├── speech_transcriber.py     # Speech-to-text using Whisper/Sarvam AI
        │   ├── transcript_analyzer.py    # Extracts action items, decisions, questions
        │   └── __pycache__/              # Compiled Python files
        │
        ├── app.py                        # Streamlit frontend application
        ├── test_main.py                  # Testing script for pipeline execution
        ├── requirements.txt              # Project dependencies
        ├── README.md                     # Project documentation
        └── InsightLens_Report.pdf        # Detailed project report

        

## Demo Video
  --link: https://drive.google.com/drive/folders/1f6sWCuSBbzKQpa8LTugrHjcsRD_9CMV_?usp=sharing
