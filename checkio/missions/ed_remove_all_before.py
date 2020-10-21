from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    # 1) will recive arguments called "items" of datatype "list" and "border of datatype "int"
     # 2) handle the edge cases
          # a) If the element is not in the list then the list will not be changed
     # 3) If the element is in the list then it will cut off everything that is before it
     # 4) Return the list
    if border not in items:
        return items
    else:
        x = items.index(border)
    return items[x:]


if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_before([], 0)) == []
    assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")
