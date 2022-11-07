from model.order.address import Address
from model.order.delivery_date import DeliveryDate
from model.order.email import Email
from model.order.first_name import FirstName
from model.order.last_name import LastName
from model.order.phone_number import PhoneNumber
from model.order.receiving_time import ReceivingTime
from pydantic import BaseModel


class Order(FirstName,
            LastName,
            PhoneNumber,
            Email,
            Address,
            DeliveryDate,
            ReceivingTime):
    pass

# receiving_time: date
