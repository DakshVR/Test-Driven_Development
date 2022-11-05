def check_pwd(pwd):
    if len(pwd) < 8 or len(pwd) > 20:
        return False

    lower_case = False
    upper_case = False
    digit = False
    for character in pwd:
        if character.islower():
            lower_case = True
        elif character.isupper():
            upper_case = True
        elif character.isdigit():
            digit = True

    if (lower_case and upper_case and digit) == False:
        return False

    return True
