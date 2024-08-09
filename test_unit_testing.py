import pytest
from main import get_order_count

def test_order_count():
    assert get_order_count() == 2050
