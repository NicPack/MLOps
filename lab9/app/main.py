from app.core_api_functions import get_inference
from fastapi import FastAPI
from app.models import Input, Output

app = FastAPI()


@app.get("/")
def healthcheck():
    return {"status": "ok"}


@app.post("/predict")
def get_prediction(input: Input) -> Output:
    """_summary_

    Args:
        input (Input): _description_

    Returns:
        Output: _description_
    """
    return get_inference(input)
