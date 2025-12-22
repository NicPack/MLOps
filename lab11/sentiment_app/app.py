import numpy as np
import onnxruntime as ort
from fastapi import FastAPI
from mangum import Mangum
from sentiment_app.models import Input
from tokenizers import Tokenizer

OONX_CLASSIFIER_PATH: str = "model/onnx/classifier.onnx"
OONX_EMBEDDING_MODEL_PATH: str = "model/onnx/sentence_transformer/embedding.onnx"
OONX_TOKENIZER_PATH: str = "model/onnx/sentence_transformer/tokenizer/tokenizer.json"

embedding_session = ort.InferenceSession(OONX_EMBEDDING_MODEL_PATH)
classifier_session = ort.InferenceSession(OONX_CLASSIFIER_PATH)
tokenizer = Tokenizer.from_file(OONX_TOKENIZER_PATH)

SENTIMENT_MAP = {0: "negative", 1: "neutral", 2: "positive"}

app = FastAPI()
handler = Mangum(app)


@app.post("/predict")
def inference(cleaned_text: Input) -> str:
    encoded = tokenizer.encode(cleaned_text.text)

    # prepare numpy arrays for ONNX
    input_ids = np.array([encoded.ids])
    attention_mask = np.array([encoded.attention_mask])

    # run embedding inference
    embedding_inputs = {"input_ids": input_ids, "attention_mask": attention_mask}
    embeddings = embedding_session.run(None, embedding_inputs)[0]

    # run classifier inference
    classifier_input_name = classifier_session.get_inputs()[0].name
    classifier_inputs = {classifier_input_name: embeddings.astype(np.float32)}
    prediction = classifier_session.run(None, classifier_inputs)[0]

    label: str = SENTIMENT_MAP.get(prediction[0], "unknown")
    return label
