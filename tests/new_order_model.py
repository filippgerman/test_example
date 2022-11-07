from datetime import date

from model.order.order import Order

NAME = "test"
LAST_NAME = "test"
PHONE_NUMBER = "89253452217"
EMAIL = "filipp@gmail.com"
ADDRESS = "bali kyta 7"
DELIVERY_DATE = date(2022, 11, date.today().day + 7)


def new_order_model(first_name: str = NAME,
                    last_name: str = LAST_NAME,
                    phone_number: str = PHONE_NUMBER,
                    email: str = EMAIL,
                    address: str = ADDRESS,
                    delivery_date: date = DELIVERY_DATE) -> Order:
    return Order(
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        email=email,
        address=address,
        delivery_date=delivery_date
    )
