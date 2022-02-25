from typing import List


right = "r"
down = "d"

none = [[]]
one = [[right, down], [down, right]]
two = [[right, right, down, down], [right, down, right, down],
       [right, down, down, right], [down, right, right, down], 
       [down, right, down, right], [down, down, right, right]]

def lattice_paths(side_length: int, paths: list = [], n: int = 0) -> list:
    """
    Computes number of possible equal-length paths through an
    n by n lattice.
    """

    if (n == 0):
        paths = [[right], [down]];
    
    for path in paths:
        if can_add_more_path(path, side_length, right):
            paths.append(path + [right])
        if can_add_more_path(path, side_length, down):
            paths.append(path + [down])


    return [paths]

def can_add_more_path(path: list, side_length: int, dir: str) -> bool:
    count = 0
    for ele in list:
        if ele == dir:
            count += 1
    
    if count >= side_length:
        return True
    else:
        return False