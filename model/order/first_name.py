from pydantic import BaseModel, validator
from model.untils import check_word_presence_cyrillic_letters, check_word_presence_latin_letters


class FirstName(BaseModel):
    first_name: str

    @validator("first_name")
    def name_validator(cls, value: str):
        check_cyrillic = check_word_presence_cyrillic_letters(value)
        check_latin = check_word_presence_latin_letters(value)
        if check_cyrillic and check_latin:
            raise ValueError("Ошибка валидации имени пользователя")
        if not check_cyrillic and not check_latin:
            raise ValueError("Ошибка валидации имени пользователя")
        return value