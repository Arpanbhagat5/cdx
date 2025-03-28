# Pretty print a tree
class Node:
    def __init__(self,value) -> None:
        self.data = value
        self.right=None
        self.left=None

def print_tree(root: Node, level: int, is_right: bool) -> None:
    spacer="     "
    right_brancher="/---"
    left_brancher="\---"
    brancher=right_brancher if is_right else left_brancher
    if root is None:
        return

    if root.right is not None:
        print_tree(root.right, level+1, True)

    if level:
        print(spacer*level+brancher, root.data)
    else:
        print(spacer*level, root.data)

    if root.left is not None:
        print_tree(root.left, level+1, False)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.right = Node(7)
    root.right.left = Node(6)
    root.right.left.left = Node(9)
    root.left.right = Node(5)
    root.left.right.right = Node(8)
    root.left.left = Node(4)
    print_tree(root, 0, False)


