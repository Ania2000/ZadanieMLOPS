import pytest
from pydantic import ValidationError

from api.models.sentiment import PredictRequest, PredictResponse


def test_predict_request_accepts_valid_text() -> None:

    request = PredictRequest(text="This is a valid sentence.")
    assert request.text == "This is a valid sentence."


def test_predict_request_rejects_missing_text() -> None:

    with pytest.raises(ValidationError):
        PredictRequest()


def test_predict_request_rejects_empty_text() -> None:

    with pytest.raises(ValidationError):
        PredictRequest(text="")


def test_predict_response_accepts_valid_prediction() -> None:

    response = PredictResponse(prediction="positive")
    assert response.prediction == "positive"
