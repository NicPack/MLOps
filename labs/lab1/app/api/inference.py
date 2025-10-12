import joblib


def load_model(model_name: str):
    model = joblib.load(f"lab1/models/{model_name}.pkl")
    return model


def predict(model, X):
    pred = model.predict(X)
    return pred
