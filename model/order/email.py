from email_validate import validate_or_fail
from email_validate.exceptions import AddressFormatError, AddressNotDeliverableError
from pydantic import BaseModel, validator


class Email(BaseModel):
    email: str

    @validator("email")
    def email_validator(cls, value: str):
        try:
            validate_or_fail(value, check_blacklist=False)
        except AddressFormatError:
            raise ValueError("Ошибка валидации почты пользователя")
        except AddressNotDeliverableError:
            raise ValueError("Ошибка валидации почты, адрес не существует")
        return value
