def check_word_presence_cyrillic_letters(word: str, with_hyphen: bool = False) -> bool:
    if all(__check_char(char, with_hyphen) for char in word):
        return True
    return False


def __check_char(char: str, with_hyphen: bool):
    ord_char = ord(char)
    if with_hyphen and ord_char == 45:
        return True
    if 1040 <= ord_char <= 1103:
        return True
    elif ord_char == 1025 or ord_char == 1105:
        return True
    else:
        return False
