import pytest
import urllib.request
from textStract import TextStract



@pytest.fixture
def textStract():
    return TextStract()


def test_decimal(textStract):
    
    assert 200 == 200



