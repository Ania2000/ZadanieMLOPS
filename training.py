from pathlib import Path

import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


MODEL_PATH = Path("iris_model.joblib")


def load_data():

    iris = load_iris()
    return iris.data, iris.target


def train_model():

    x, y = load_data()
    model = RandomForestClassifier(random_state=42)
    model.fit(x, y)
    return model


def save_model(model, path: Path = MODEL_PATH) -> None:

    joblib.dump(model, path)


if __name__ == "__main__":
    trained_model = train_model()
    save_model(trained_model)
    print(f"Model saved to {MODEL_PATH}")
