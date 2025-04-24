# 🔀 Get prompt by emotion
def get_prompt_by_emotion(emotion: str):
    return PROMPTS.get(emotion, PROMPTS["grief_prompt"])

# 🧠 AI Therapy Assistant Loop
print("🧠 AI Therapy Assistant is ready. Type 'bye' anytime to exit.\n")

while True:
    query = input("💬 How are you feeling or what would you like to talk about?\n")

    if query.lower() in ["bye", "exit", "quit"]:
        print("👋 Take care! I'm always here when you want to talk again.")
        break

    raw_emotion = detect_emotion(query)
    fallback_emotion = fallback_keyword_detection(query)
    final_emotion = fallback_emotion if fallback_emotion else map_emotion(raw_emotion)

    print(f"🔍 Detected Emotion: {raw_emotion}")
    if fallback_emotion:
        print(f"🔁 Overridden by keyword detection → {fallback_emotion}")
    print(f"🧩 Routing to Prompt for: {final_emotion}")

    selected_prompt = get_prompt_by_emotion(final_emotion)

    # 🧠 Build dynamic RAG chain with updated prompt
    rag_chain = ConversationalRetrievalChain.from_llm(
        llm=llama_scout_llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=False,
        combine_docs_chain_kwargs={"prompt": selected_prompt}
    )

    result = rag_chain({"question": query})
    print("\n🧠 AI Therapy Assistant:")
    print(result["answer"])
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")