from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest


@pytest.fixture()
def app(monkeypatch, mongo_database) -> FastAPI:
    from webservice.main import app as application
    application.state.db = mongo_database
    return application


@pytest.fixture()
def client(app) -> TestClient:
    client = TestClient(app)
    return client
