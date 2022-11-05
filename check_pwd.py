def check_pwd(pwd):
    if len(pwd) < 8 or len(pwd) > 20:
        return False

    symbols = '~`!@#$%^&*()_+-='
    lower_case = False
    upper_case = False
    digit = False
    symbol = False

    for character in pwd:
        if character.islower():
            lower_case = True
        elif character.isupper():
            upper_case = True
        elif character.isdigit():
            digit = True
        elif character in symbols:
            symbol = True

    if (lower_case and upper_case and digit and symbol) == False:
        return False

    return True
