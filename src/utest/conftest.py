import pytest
from src.Talos import Talos


@pytest.fixture(scope='session')
def talos():
    return Talos()
