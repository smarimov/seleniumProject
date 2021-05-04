import pytest
import sys


@pytest.mark.skip
def test_login():
    print('Login done')


def test_logout():
    print('Logout done')


@pytest.mark.skipif(sys.version_info < (3, 10), reason='Python version not supported')
def test_addProduct():
    print("add product")
