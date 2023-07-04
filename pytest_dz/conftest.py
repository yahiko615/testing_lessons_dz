import pytest

from .human import Human


@pytest.fixture()
def create_human():
    human = Human('Misha', 22, 'male')
    return human
