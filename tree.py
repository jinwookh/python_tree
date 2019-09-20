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


def iter_inorder(root):
    stack = []
    while True:
        while root is not None:
            stack.append(root)
            root = root.left

        if len(stack) == 0:
            break

        root = stack.pop()
        root.print_data()
        root = root.right


def iter_pre_order(root):
    stack = []
    while True:
        while root is not None:
            root.print_data()
            stack.append(root)
            root = root.left

        if len(stack) == 0:
            break

        root = stack.pop()
        root = root.right


def iter_post_order(root):
    stack = []
    structure_index = 1
    while True:
        if structure_index == 1:
            while root is not None:
                stack.append([root, 1])
                root = root.left

        if len(stack) == 0:
            break
        structure = stack.pop()
        if structure[1] == 1:
            stack.append([structure[0], 2])
            root = structure[0].right
            structure_index = 1
            continue
        if structure[1] == 2:
            structure[0].print_data()
            structure_index = 2


def preorder(root):
    if root is not None:
        root.print_data()
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        root.print_data()


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


def test_tree_function(sentence, func, L):
    print(sentence)
    root = Node()
    make_tree(L, 0, root)
    func(root)
    print()


testTreeList = ["+", "*", "E", "*", "D", None, None, "/", "C", "F", "G", None, None, None, None, "A", "B"]

test_tree_function("preorder starts!", preorder, testTreeList)
test_tree_function("iter preorder starts!", iter_pre_order, testTreeList)

test_tree_function("inorder starts!", inorder, testTreeList)
test_tree_function("iter inorder starts!", iter_inorder, testTreeList)

test_tree_function("post order starts!", postorder, testTreeList)
test_tree_function("iter post order starts!", iter_post_order, testTreeList)
