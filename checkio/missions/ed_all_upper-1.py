def is_all_upper(text: str) -> bool:
    # 1) will recive arguments called "text" of datatype "str"
    # 2) Check the String if there are any characters in it and also check for all upper case characters
    # 3) return true if the string is empty or return false if the string has all upper case characters
    if any(x.islower() for x in text):
        return False
    else:
        return True



if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")