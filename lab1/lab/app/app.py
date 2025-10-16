import pandas as pd
from fastapi import FastAPI

from lab1.api.inference import load_model
from lab1.api.models import PredictRequest, PredictResponse
from lab1.api.training import load_data

app = FastAPI()
_, _, class_mapping = load_data()


model = load_model("iris_model")


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    data = pd.DataFrame(data=request.model_dump(), index=[0])
    prediction = model.predict(data)[0]
    return PredictResponse(prediction=class_mapping[prediction])
