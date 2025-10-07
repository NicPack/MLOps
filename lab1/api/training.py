import joblib
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression


def load_data():
    data = load_iris()

    X = pd.DataFrame(data.data)
    X.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    class_mapping = data.target_names

    y = pd.DataFrame(data.target)
    return X, y, class_mapping


def train_model(X, y):
    model = LogisticRegression(penalty="l2", max_iter=100000)
    model.fit(X, y)
    return model


def save_model(model, model_name: str):
    joblib.dump(model, f"lab1/models/{model_name}.pkl")
