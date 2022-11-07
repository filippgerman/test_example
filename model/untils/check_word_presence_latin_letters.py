import string


def check_word_presence_latin_letters(word: str, with_hyphen: bool = False) -> bool:
    letters = string.ascii_letters + '-' if with_hyphen else string.ascii_letters
    if all(char in letters for char in word):
        return True
    return False
