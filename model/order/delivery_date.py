from datetime import date

from pydantic import BaseModel, validator


class DeliveryDate(BaseModel):
    delivery_date: date

    @validator("delivery_date")
    def receiving_time(cls, value: date):
        if value.isoweekday() > 5:
            raise ValueError("Ошибка валидации даты, выходной день")
        today = date.today()

        if today > value:
            raise ValueError("Ошибка валидации даты, заданная дата уже прошла")

        date_delta = value - date.today()
        if date_delta.days < 7:
            raise ValueError("Ошибка валидации даты, заданная дата меньше недели")
        return value
