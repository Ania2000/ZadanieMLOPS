from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_predict_returns_valid_json_response() -> None:

    response = client.post(
        "/predict",
        json={"text": "What a great MLOps lecture, I am very satisfied"},
    )

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")

    data = response.json()
    assert "prediction" in data
    assert data["prediction"] in {"negative", "neutral", "positive"}


def test_predict_works_for_multiple_examples() -> None:

    examples = [
        "I love this product.",
        "This is average.",
        "This is terrible.",
    ]

    for text in examples:
        response = client.post("/predict", json={"text": text})
        assert response.status_code == 200
        assert response.json()["prediction"] in {"negative", "neutral", "positive"}


def test_predict_rejects_missing_text() -> None:

    response = client.post("/predict", json={})

    assert response.status_code == 422
    assert response.headers["content-type"].startswith("application/json")

    data = response.json()
    assert "detail" in data
    assert isinstance(data["detail"], list)
    assert len(data["detail"]) > 0
    assert data["detail"][0]["loc"][-1] == "text"


def test_predict_rejects_empty_text() -> None:

    response = client.post("/predict", json={"text": ""})

    assert response.status_code == 422
    assert response.headers["content-type"].startswith("application/json")

    data = response.json()
    assert "detail" in data
    assert isinstance(data["detail"], list)
    assert len(data["detail"]) > 0
    assert data["detail"][0]["loc"][-1] == "text"
