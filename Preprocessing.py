import re
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

def preprocess_and_chunk_multipair_sessions(dataset_rows, chunk_size=500, chunk_overlap=100):
    documents = []

    for row in dataset_rows:
        raw_text = row['text']

        # Step 1: Remove the <<SYS>> ... <</SYS>> block
        cleaned = re.sub(r"\[INST\] <<SYS>>.*?<</SYS>>", "", raw_text, flags=re.DOTALL)

        # Step 2: Extract all user–therapist turn pairs in order
        dialogue_pairs = re.findall(r"<s>\[INST\](.*?)\[/INST\](.*?)</s>", cleaned, flags=re.DOTALL)

        full_convo = []
        for user_turn, therapist_turn in dialogue_pairs:
            user_clean = user_turn.strip().replace("<s>", "").replace("</s>", "")
            therapist_clean = therapist_turn.strip().replace("<s>", "").replace("</s>", "")
            if user_clean and therapist_clean:
                full_convo.append(f"User: {user_clean}\nTherapist: {therapist_clean}")

        # Combine all turn pairs into a single multi-pair conversation document
        if full_convo:
            combined_text = "\n\n".join(full_convo)
            documents.append(Document(page_content=combined_text))

    # Step 3: Chunk long conversations
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    split_docs = splitter.split_documents(documents)

    return split_docs
	
	# Run preprocessing and chunking
split_docs = preprocess_and_chunk_multipair_sessions(ds2)