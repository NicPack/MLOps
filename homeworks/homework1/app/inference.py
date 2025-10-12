import joblib
from sentence_transformers import SentenceTransformer
from sklearn.linear_model import LogisticRegression

sentence_transformer: SentenceTransformer = SentenceTransformer(
    model_name_or_path="app/model/sentence_transformer.model"
)
classifier: LogisticRegression = joblib.load("app/model/classifier.joblib")
