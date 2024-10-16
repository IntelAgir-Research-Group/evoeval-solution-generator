
from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list `numbers' and add 'delimiter' at the end of the list
    >>> intersperse([], 4)
    [4]
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3, 4]
    """
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i])
        if i < len(numbers) - 1:
            result.append(delimiter)
    result.append(delimiter)
    return result