from typing import Any
import pytest

from model.order.phone_number import PhoneNumber
from tests.new_order_model import new_order_model

PHONE_NUMBER = [
    "+611234567890",
    "+431234567890",
    "+994123456789",
    "+375123456789",
    "+541234567890",
    "89253452217",
    "+621234567890",
    "+112345678901"
]
PHONE_NUMBER_WITH_ERROR = [
    (ValueError, "+1"),
    (ValueError, "+11111111111111111111"),
    (ValueError, "+1239"),
    (ValueError, "1239"),
    (ValueError, "test")
]


@pytest.mark.parametrize("phone_number", PHONE_NUMBER)
def test_phone_numbers(phone_number: str):
    PhoneNumber(phone_number=phone_number)


@pytest.mark.parametrize("expect_exception, phone_number", PHONE_NUMBER_WITH_ERROR)
def test_phone_numbers_with_error(expect_exception: Any, phone_number: str):
    with pytest.raises(expect_exception):
        PhoneNumber(phone_number=phone_number)
