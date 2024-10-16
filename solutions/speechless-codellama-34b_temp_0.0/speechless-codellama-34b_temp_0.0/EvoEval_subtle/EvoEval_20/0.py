from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    min_diff = float('inf')
    result = (0, 0)
    for i in range(len(numbers) - 1):
        diff = abs(numbers[i] - numbers[i + 1])
        if diff < min_diff:
            min_diff = diff
            result = (numbers[i + 1], numbers[i])
    return result