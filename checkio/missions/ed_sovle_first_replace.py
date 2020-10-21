from typing import Iterable


def replace_first(items: list) -> Iterable:
    # 1) will recive argument called "items" of datatype "list"
    # 2) take the first element and replace it at the end of the list. An empty list or list with only one element should stay the same.
    # 3) return the list
    if len(items) == 0:
        return []
    else:
        return items[1:] + [items[0]]


if __name__ == '__main__':
    print("Example:")
    print(list(replace_first([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")