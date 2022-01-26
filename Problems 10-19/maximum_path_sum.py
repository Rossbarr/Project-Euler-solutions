"""
This file holds the solutions for problems 18 and 67,
maximum path sum 1 and 2, respectively.
"""

class binary_tree_node():
    """
    Defines a node in a binary tree.
    """
    def __init__(self, value: int, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str(self.value)

    def update_value(self) -> None:
        if self.left is not None and self.right is not None:
            left_value = self.left.value
            right_value = self.right.value
            if left_value >= right_value:
                child_value = left_value
            else:
                child_value = right_value
        else:
            child_value = 0

        self.value += child_value

def set_up_binary_tree(triangle: list) -> list:
    triangle.reverse()
    binary_tree = []
    for i in range(len(triangle)):
        binary_tree.append([])
        for j in range(len(triangle[i])):
            node = binary_tree_node(value=triangle[i][j])
            binary_tree[i].append(node)
            if i > 0:
                node.left = binary_tree[i-1][j]
                node.right = binary_tree[i-1][j+1]
            node.update_value()

    binary_tree.reverse()
    return binary_tree

def maximum_path_sum_1():
    triangle1 = [
    (75,),
    (95, 64),
    (17, 47, 82),
    (18, 35, 87, 10),
    (20,  4, 82, 47, 65),
    (19,  1, 23, 75,  3, 34),
    (88,  2, 77, 73,  7, 63, 67),
    (99, 65,  4, 28,  6, 16, 70, 92),
    (41, 41, 26, 56, 83, 40, 80, 70, 33),
    (41, 48, 72, 33, 47, 32, 37, 16, 94, 29),
    (53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14),
    (70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57),
    (91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48),
    (63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31),
    ( 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23)
    ]
    bt = set_up_binary_tree(triangle1)
    print(bt[0][0])

def maximum_path_sum_2():
    triangle2 = []
    with open("p067_triangle.txt", 'r') as file:
        for line in file:
            triangle2.append([int(i) for i in line.split(" ")])

    bt = set_up_binary_tree(triangle2)
    print(bt[0][0])

maximum_path_sum_2()
