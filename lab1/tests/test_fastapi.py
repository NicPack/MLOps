from app import health_check, welcome_root


def test_welcome_root():
    assert welcome_root() == {"message": "Welcome to the ML API"}


def test_health_path():
    assert health_check() == {"status": "ok"}
