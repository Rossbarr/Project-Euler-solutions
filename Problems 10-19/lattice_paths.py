right = "r"
down = "d"

none = [[]]
one = [[right, down], [down, right]]
two = [[right, right, down, down], [right, down, right, down],
       [right, down, down, right], [down, right, right, down], 
       [down, right, down, right], [down, down, right, right]]

def lattice_paths(n: int):
    """
    Computes number of possible equal-length paths through an
    n by n lattice.
    """
    paths = []
    while True:
        direction = right
        path = []
        path << direction
