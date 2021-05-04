import pytest


@pytest.fixture
def setup():
    print("Start Browser")
    yield
    print("Close Browser")


def test_1(setup):
    print("Test1 executed")


def test_2(setup):
    print("Test2 executed")


def test_3(setup):
    print("Test3 executed")
