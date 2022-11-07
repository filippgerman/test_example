from datetime import date
from typing import Any

import pytest

from model.order.delivery_date import DeliveryDate

DATE_WITH_ERROR = [
    (ValueError, date.today()),
    (ValueError, date(2022, 11, 12)),
    (ValueError, date(2022, 11, 13))
]


@pytest.mark.parametrize("expect_exception, delivery_date", DATE_WITH_ERROR)
def test_first_name(expect_exception: Any, delivery_date: date):
    with pytest.raises(expect_exception):
        DeliveryDate(delivery_date=delivery_date)
