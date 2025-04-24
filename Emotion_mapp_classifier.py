# 🧠 Emotion Classifier
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=3)

EMOTION_MAP = {
    "sadness": "sad",
    "anger": "anger",
    "fear": "panic",
    "joy": "self_esteem",
    "love": "relationship",
    "surprise": "confusion",
    "neutral": "casual",
    "guilt": "guilt",
    "shame": "shame",
    "frustration": "frustration",
    "jealousy": "jealousy",
    "envy": "envy"
}

# 🔍 Detect top emotion
def detect_emotion(text: str) -> str:
    preds = emotion_classifier(text)[0]
    return max(preds, key=lambda x: x["score"])["label"].lower()

# 🧩 Optional keyword fallback if emotion is misclassified
def fallback_keyword_detection(text: str) -> str | None:
    text = text.lower()
    if "panic" in text or "attack" in text:
        return "panic"
    if "lonely" in text or "isolated" in text:
        return "loneliness"
    if "jealous" in text:
        return "jealousy"
    if "ashamed" in text or "shame" in text:
        return "shame"
    if "envy" in text or "envious" in text:
        return "envy"
    return None

# 🧠 Map emotion to internal prompt key
def map_emotion(model_emotion: str) -> str:
    return EMOTION_MAP.get(model_emotion.lower(), "grief")