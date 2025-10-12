from api.models import PredictRequest
from app import health_check, predict, welcome_root


def test_welcome_root():
    assert welcome_root() == {"message": "Welcome to the ML API"}


def test_health_path():
    assert health_check() == {"status": "ok"}


def test_prediction():
    request = PredictRequest(
        sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2
    )
    response = predict(request)
    assert response.prediction == "setosa"
