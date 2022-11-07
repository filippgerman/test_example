from typing import Any

import pytest

from model.order.receiving_time import ReceivingTime

RECEIVING_TIME = [
    "10:00-13:00",
    "13:00-16:00",
    "16:00-19:00"
]

RECEIVING_TIME_WITH_ERROR = [
    (ValueError, "10:00-14:00"),
    (ValueError, "13:00-15:00"),
    (ValueError, "16:00-20:00")
]


@pytest.mark.parametrize("receiving_time", RECEIVING_TIME)
def test_receiving_time(receiving_time: str):
    ReceivingTime(receiving_time=receiving_time)


@pytest.mark.parametrize("expect_exception, receiving_time", RECEIVING_TIME_WITH_ERROR)
def test_receiving_time_with_error(expect_exception: Any, receiving_time: str):
    with pytest.raises(expect_exception):
        ReceivingTime(receiving_time=receiving_time)
