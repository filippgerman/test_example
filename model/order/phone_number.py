import phonenumbers
from phonenumbers import NumberParseException, is_valid_number, is_possible_number
from pydantic import BaseModel, validator

from model.enum.phone_code import LocalPhoneCode, InternationalPhoneCode


class PhoneNumber(BaseModel):
    phone_number: str

    @validator("phone_number")
    def phone_validator(cls, value: str):
        if value[0] == LocalPhoneCode.ru:
            value = InternationalPhoneCode.ru + value[1:]
        try:
            parse_number = phonenumbers.parse(value)
        except NumberParseException:
            raise ValueError("Ошибка валидации номера телефона")

        if not is_valid_number(parse_number) and not is_possible_number(parse_number):
            raise ValueError("Ошибка валидации номера телефона")
        return value
