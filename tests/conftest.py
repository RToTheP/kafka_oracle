from fastkafka import FastKafka
from fastkafka.testing import Tester
import pytest

from ko.app import create_app

@pytest.fixture()
def app() -> FastKafka:
    app = create_app()
    yield app
