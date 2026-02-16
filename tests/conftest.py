import importlib
import pytest


@pytest.fixture()
def client():
    # reload module to reset in-memory state between tests
    app_mod = importlib.reload(__import__("src.app", fromlist=["app"]))
    app = app_mod.app
    from fastapi.testclient import TestClient

    with TestClient(app) as client:
        yield client
