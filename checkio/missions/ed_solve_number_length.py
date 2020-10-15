def number_length(a: int) -> int:
    # your code here
    # algorithm
    # 1) Will recive an argument called "a" of datatype "int"
    # 2) Convert the integer into a string
    # 3) Calculate the length of the string
    # 4) Return the Length of the string
    return len(str(a))

def number_length_two(a: int) -> int:
    mystring = str(a)
    mylength = len(mystring)

    return mylength

if __name__ == '__main__':
    print("Example:")
    print(number_length(10))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert number_length(10) == 2
    assert number_length(0) == 1
    assert number_length(4) == 1
    assert number_length(44) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
