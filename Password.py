#  The password will be considered strong enough if its length is greater than or equal to 10 symbols,
#  it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it.
#  The password contains only ASCII latin letters or digits.


def is_more_then_10digits(data: str) -> bool:
    if data.__len__() >= 10:
        return True
    return False


def has_uppercase(data: str) -> bool:
    for i in data:
        if i.isupper():
            return True
    return False


def has_lowercase(data: str) -> bool:
    for i in data:
        if i.islower():
            return True
    return False


def has_digit(data: str) -> bool:
    for i in data:
        if i.isdigit():
            return True
    return False


def checkio(data: str) -> bool:
    if is_more_then_10digits(data):
        if data.isascii():
            if has_uppercase(data):
                if has_lowercase(data):
                    if has_digit(data):
                        return True
    return False


# Some hints
# Just check all conditions


if __name__ == '__main__':
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
