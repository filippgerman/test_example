import pytest

from model.order.last_name import LastName

LAST_NAMES = [
    "German",
    "Герман",
    "Ёрпрп",
    "Гер-ман"
]


@pytest.mark.parametrize("last_name", LAST_NAMES)
def test_first_name(last_name: str):
    LastName(last_name=last_name)
