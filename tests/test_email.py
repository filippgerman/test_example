from typing import Any
import pytest

from model.order.email import Email

EMAILS = [
    "filipp@gmail.com",
    "filippgerman32@gmail.com",
    "germanfilipp@yandex.ru"
]

EMAILS_WITH_ERROR = [
    (ValueError, "@gmail.com"),
    (ValueError, "121@"),
    (ValueError, "filipfilipfilip123413231341@gmail.com"),
]


@pytest.mark.parametrize("email", EMAILS)
def test_email(email: str):
    Email(email=email)


@pytest.mark.parametrize("expect_exception, email", EMAILS_WITH_ERROR)
def test_email_with_error(expect_exception: Any, email: str):
    with pytest.raises(expect_exception):
        Email(email=email)
