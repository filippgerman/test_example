from pydantic import BaseModel, validator

from model.untils import check_word_presence_cyrillic_letters, check_word_presence_latin_letters


class LastName(BaseModel):
    last_name: str

    @validator("last_name")
    def last_name_validator(cls, value: str):
        check_cyrillic = check_word_presence_cyrillic_letters(value, True)
        check_latin = check_word_presence_latin_letters(value, True)
        if check_cyrillic and check_latin:
            raise ValueError("Ошибка валидации имени пользователя")
        if not check_cyrillic and not check_latin:
            raise ValueError("Ошибка валидации имени пользователя")
        return value
