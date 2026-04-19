from fastapi import FastAPI

from api.models.iris import PredictRequest, PredictResponse
from inference import load_model, predict as run_prediction


app = FastAPI()
model = load_model()


@app.get("/")
def welcome_root() -> dict[str, str]:

    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check() -> dict[str, str]:

    return {"status": "ok"}


@app.post("/predict")
def predict(request: PredictRequest) -> PredictResponse:

    prediction = run_prediction(model, request.model_dump())
    return PredictResponse(prediction=prediction)