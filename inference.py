from pathlib import Path

import joblib


MODEL_PATH = Path("iris_model.joblib")

CLASS_NAMES = {
    0: "setosa",
    1: "versicolor",
    2: "virginica",
}


def load_model(path: Path = MODEL_PATH):
    """Load the trained model from a file."""
    return joblib.load(path)


def predict(model, features: dict) -> str:
    """Make a prediction and return the predicted class name."""
    data = [
        [
            features["sepal_length"],
            features["sepal_width"],
            features["petal_length"],
            features["petal_width"],
        ]
    ]
    prediction = model.predict(data)[0]
    return CLASS_NAMES[int(prediction)]
