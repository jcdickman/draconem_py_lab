def backward_string(val: str) -> str:
    # 1) will recive an argument called "val" of datatype "str"
    # 2) convert val into a string
    # 3) reverse the string
    # 4) return the reversed string
    return val[::-1]


if __name__ == '__main__':
    print("Example:")
    print(backward_string('val'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
    print("Coding complete? Click 'Check' to earn cool rewards!")
