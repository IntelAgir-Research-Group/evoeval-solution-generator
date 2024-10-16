

def sort_even(l: list):
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    even_values = sorted([l[i] for i in even_indices])
    for i, val in zip(even_indices, even_values):
        l[i] = val
    return l
