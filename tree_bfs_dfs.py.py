# print tree BFS and DFS

class Node:
    def __init__(self) -> None:
        self.data = None
        self.left = None
        self.right = None


def print_tree_dfs(root: Node):
    """
    if the node is None, return
    print the node
    if the node has a left child, call the function recursively
    if the node has a right child, call the function recursively
    """

    if root is None:
        return
    print(root.data)
    if root.left is not None:
        print_tree_dfs(root.left)
    if root.right is not None:
        print_tree_dfs(root.right)


def print_tree_bfs(root: Node):
    """
    while there is a node in the queue
    print the node
    if the node has a left child, add it to the queue
    if the node has a right child, add it to the queue
    """

    if root is None:
        return
    queue = []
    queue.append(root)

    while queue:
        node = queue.pop(0)
        print(node.data)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


if __name__ == "__main__":
    root = Node()
    root.data = 1
    root.left = Node()
    root.left.data = 2
    root.right = Node()
    root.right.data = 3
    root.left.left = Node()
    root.left.left.data = 4
    root.left.right = Node()
    root.left.right.data = 5
    root.right.left = Node()
    root.right.left.data = 6
    root.right.right = Node()
    root.right.right.data = 7

    print("BFS")
    print_tree_bfs(root)

    print("DFS")
    print_tree_dfs(root)
