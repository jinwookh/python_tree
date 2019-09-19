class Node:
    def __init__(self, right=None, left=None, data=None):
        self.right = right
        self.left = left
        self.data = data

    def add_left(self, node):
        self.left = node

    def add_right(self, node):
        self.right = node

    def print_data(self):
        print(self.data, end='')


def inorder(root):
    if root is not None:
        inorder(root.left)
        root.print_data()
        inorder(root.right)


def preorder(root):
    if root is not None:
        root.print_data()
        inorder(root.left)
        postorder(root.right)


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        root.print_data()


testTreeList = ["+", "*", "E", "*", "D", None, None, "/", "C", None, None, None, None, None, None, "A", "B"]


def make_tree(L, index, root):
    root.data = L[index]

    if (index * 2 + 1 < len(L)) and L[index * 2 + 1] is not None:
        root.add_left(Node())
    if (index * 2 + 2 < len(L)) and L[index * 2 + 2] is not None:
        root.add_right(Node())

    if root.left is not None:
        make_tree(L, index * 2 + 1, root.left)
    if root.right is not None:
        make_tree(L, index * 2 + 2, root.right)
    return


def test_preorder(L):
    print("preorder starts!")
    root = Node()
    make_tree(L, 0, root)
    preorder(root)
    print()


def test_postorder(L):
    print("postorder starts!")
    root = Node()
    make_tree(L, 0, root)
    postorder(root)
    print()


def test_inorder(L):
    print("inorder starts!")
    root = Node()
    make_tree(L, 0, root)
    inorder(root)
    print()


test_preorder(testTreeList)
test_inorder(testTreeList)
test_postorder(testTreeList)
