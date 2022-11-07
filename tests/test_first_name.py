from typing import Any
import pytest

from model.order.first_name import FirstName

NAMES = [
    "Petr",
    "FILIPP",
    "Петр",
    "ёввыы",
    "Ёзвск",
    "ФИЛИПП"
]

NAMES_WITH_ERROR = [
    (ValueError, "пафfdas"),
    (ValueError, "fdaпвавы"),
    (ValueError, "FASПРПР"),
    (ValueError, "ПАРПFDSS"),
    (ValueError, "ПЕРЕРsasa"),
]


@pytest.mark.parametrize("first_name", NAMES)
def test_first_name(first_name: str):
    FirstName(first_name=first_name)


@pytest.mark.parametrize("expect_exception, first_name", NAMES_WITH_ERROR)
def test_first_name(expect_exception: Any, first_name: str):
    with pytest.raises(expect_exception):
        FirstName(first_name=first_name)
