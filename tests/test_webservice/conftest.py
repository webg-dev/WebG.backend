from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest

from webservice.main import app as application


@pytest.fixture()
def app() -> FastAPI:
    return application


@pytest.fixture()
def client(app) -> TestClient:
    client = TestClient(app)
    return client
