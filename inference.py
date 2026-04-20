from pathlib import Path

import joblib
from sentence_transformers import SentenceTransformer


MODEL_DIR = Path("models/sentiment")
ENCODER_PATH = MODEL_DIR / "sentence_transformer.model"
CLASSIFIER_PATH = MODEL_DIR / "classifier.joblib"

LABELS = {
    0: "negative",
    1: "neutral",
    2: "positive",
}


class SentimentInference:


    def __init__(self) -> None:
        self.encoder = SentenceTransformer(str(ENCODER_PATH))
        self.classifier = joblib.load(CLASSIFIER_PATH)

    def predict(self, text: str) -> str:

        embedding = self.encoder.encode([text])
        prediction = self.classifier.predict(embedding)[0]
        return LABELS[int(prediction)]