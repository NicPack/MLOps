import joblib
from app.models import Input, Output
from sentence_transformers import SentenceTransformer
from sklearn.linear_model import LogisticRegression

classifier: LogisticRegression = joblib.load("model/classifier.joblib")
sentence_transformer: SentenceTransformer = SentenceTransformer(
    model_name_or_path="model/sentence_transformer.model"
)


def get_inference(input: Input) -> Output:
    dumped = input.model_dump()
    mapper = {0: "negative", 1: "neutral", 2: "positive"}
    class_prediction = classifier.predict(sentence_transformer.encode([dumped]))

    return Output(prediction=mapper[class_prediction[0]])
