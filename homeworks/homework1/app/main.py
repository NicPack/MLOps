from fastapi import FastAPI

from app.inference import classifier, sentence_transformer
from app.models import Input, Output

app = FastAPI()


@app.post("/predict")
def get_prediction(input: Input) -> Output:
    dumped = input.model_dump()
    mapper = {0: "negative", 1: "neutral", 2: "positive"}
    class_prediction = classifier.predict(sentence_transformer.encode([dumped]))

    return Output(prediction=mapper[class_prediction[0]])
