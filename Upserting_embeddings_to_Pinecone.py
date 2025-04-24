import uuid
import hashlib
from langchain_huggingface import HuggingFaceEmbeddings
from pinecone import Pinecone

# STEP 1: Define a hash-based ID generator
def generate_id(text: str) -> str:
    return hashlib.md5(text.encode('utf-8')).hexdigest()

# STEP 2: Initialize embedding model
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# STEP 3: Connect to Pinecone
pc = Pinecone(api_key="Put Vector DB API Key here")  # Replace with your key
index = pc.Index("therapy-docs")

# STEP 4: Set batch sizes
batch_size = 5000
micro_batch_size = 100

# STEP 5: Batch-wise embedding and upsert
for i in range(0, len(split_docs), batch_size):
    batch = split_docs[i:i+batch_size]
    texts = [doc.page_content for doc in batch]
    embeddings = embedding_model.embed_documents(texts)

    vectors_to_upsert = [
        {
            "id": generate_id(text),
            "values": vector,
            "metadata": {
                "source": "therapy-dataset",
                "text": text  # ✅ crucial for RAG!
            }
        }
        for text, vector in zip(texts, embeddings)
    ]

    for j in range(0, len(vectors_to_upsert), micro_batch_size):
        micro_batch = vectors_to_upsert[j:j+micro_batch_size]
        index.upsert(vectors=micro_batch, namespace="default")

    print(f"✅ Uploaded batch {i // batch_size + 1} ({len(vectors_to_upsert)} vectors)")
