from fastapi import FastAPI

from api.models.sentiment import PredictRequest, PredictResponse
from inference import SentimentInference


app = FastAPI()
model = SentimentInference()

@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Sentiment API is running"}


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest) -> PredictResponse:
    prediction = model.predict(request.text)
    return PredictResponse(prediction=prediction)