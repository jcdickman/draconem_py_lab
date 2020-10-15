def end_zeros(num: int) -> int:
    # 1) will recive an argument called "num" of datatype "int"
    # 2) convert the integer into a string
    # 3) count the trailing zeros of the string
    # 4) return the count of the trailing zeros
    return len(s := str(num)) - len(s.rstrip("0"))


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")