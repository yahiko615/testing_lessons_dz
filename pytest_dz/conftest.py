import pytest

from .human import Human


@pytest.fixture()
def create_human():
    human = Human('Misha', 22, 'male')
    yield human


@pytest.fixture()
def create_giga_old_human():
    human = Human('Misha', 99, 'male')
    yield human


@pytest.fixture()
def create_dead_human():
    human = Human('Misha', 101, 'male')
    yield human


@pytest.fixture()
def create_negative_human():
    human = Human('Misha', -1, 'male')
    yield human
