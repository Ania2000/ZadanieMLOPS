from inference import CLASSIFIER_PATH, ENCODER_PATH, SentimentInference


def test_model_files_exist() -> None:

    assert ENCODER_PATH.exists()
    assert CLASSIFIER_PATH.exists()


def test_model_loads_without_errors() -> None:

    model = SentimentInference()
    assert model is not None
    assert model.encoder is not None
    assert model.classifier is not None


def test_inference_works_for_multiple_examples() -> None:

    model = SentimentInference()

    samples = [
        "I love this course.",
        "This is okay.",
        "I don't like this course.",
    ]

    for text in samples:
        prediction = model.predict(text)
        assert prediction in {"negative", "neutral", "positive"}
