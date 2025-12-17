import joblib
import pytest
from app.main import app
from fastapi.testclient import TestClient
from sentence_transformers import SentenceTransformer
from sklearn.linear_model import LogisticRegressionCV

client = TestClient(app)


def test_input_is_not_empty_string():
    response = client.post("/predict", json={"text": ""})
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "string_too_short",
                "loc": ["body", "text"],
                "msg": "String should have at least 1 character",
                "input": "",
                "ctx": {"min_length": 1},
            }
        ]
    }


def test_input_is_string():
    response = client.post("/predict", json={"text": 1})
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "string_type",
                "loc": ["body", "text"],
                "msg": "Input should be a valid string",
                "input": 1,
            }
        ]
    }


@pytest.mark.parametrize(
    ("input", "output"),
    [
        ("Wow, that was fantastic", {"prediction": "positive"}),
        ("ok", {"prediction": "neutral"}),
        ("That was a complete waste of time", {"prediction": "negative"}),
    ],
)
def test_response_validation(input, output):
    response = client.post(url="/predict", json={"text": input})
    assert response.json() == output


def test_model_loading():
    classifier = joblib.load("model/classifier.joblib")
    assert type(classifier) is LogisticRegressionCV

    sentence_transformer = SentenceTransformer("model/sentence_transformer.model")
    assert type(sentence_transformer) is SentenceTransformer
