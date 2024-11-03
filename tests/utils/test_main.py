import pytest
from utils.main import print_hello


def test_print_hello():
    name = "Francis"
    exp = f"Hi {name}"
    out = print_hello(name)
    assert out ==  exp