# 🧠 AI Therapy Counsellor (Backend)

Welcome to the backend of **AI Therapy Counsellor** — an empathetic, LLM-powered virtual therapist designed to help users navigate emotional challenges through personalized, context-aware conversations.

> ✨ This backend powers the intelligence, retrieval, memory, emotion detection, and LLM reasoning in our therapy assistant.

---

## 🚀 Tech Stack

- 🧠 **LLM**: Meta LLaMA 4 Scout (via [OpenRouter API](https://openrouter.ai))
- 📚 **RAG**: Retrieval-Augmented Generation with Pinecone
- 💬 **BufferMemory**: LangChain-style chat history
- 💡 **Embeddings**: Hugging Face (MiniLM/E5 models)
- 😔 **Emotion Detection**: DistilBERT + emotion mapping
- 📦 **Vector Store**: Pinecone
- 📂 **Dataset**: Real-world therapy dialogue from HuggingFace

---

## 🏗️ Project Architecture

### 1. 🧹 Preprocessing
- Removes stopwords, unwanted characters
- Normalizes sentences for better chunking

### 2. 🧩 Chunking & Semantic Grouping
- Breaks dialogues into meaningful sections while preserving context
- Output: semantic document objects

### 3. 🔍 Embedding & Storage
- Uses Hugging Face embeddings to vectorize chunks
- Stored in **Pinecone vector DB** (batched with efficient memory use)

### 4. 📤 RAG + LLM (Meta LLaMA 4 Scout)
- Queries user → retrieves matching vector chunks
- Augments with prompt + LLM knowledge → generates human-like reply

### 5. 🔁 BufferMemory
- Remembers previous conversations (for each session)
- Helps maintain therapeutic continuity

### 6. 😢 Emotion Detection
- Classifies user emotion using DistilBERT
- Maps output to appropriate **emotion-specific prompt**

### 7. 💌 Prompt Engineering
- 15+ carefully written prompts
- Tailored by emotion (e.g., grief, anxiety, panic, self-doubt)
- Each session dynamically routes to the best one

---

## 🗂️ Directory Structure

therapy-counsellor-backend/ ├── data/ → Raw + processed datasets ├── models/ → Emotion model + prompt templates ├── vectorstore/ → Pinecone config + setup ├── utils/ → Preprocessing, chunking, embeddings ├── rag_engine/ → Retriever, LLM caller, and full RAG pipeline ├── configs/ → config.yaml (API keys, settings) ├── main.py → Entry point ├── requirements.txt → All dependencies └── README.md → You're here!