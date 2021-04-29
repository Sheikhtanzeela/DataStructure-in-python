class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def preorder_recursive(root, result):
        if not roo:
            return
        result.append(root.data)
        preorderTraversal9(root.left, result)
        preorderTraversal(root.right, result)

    def preorder_iterative(root, result):
        if not root:
            return
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def inorder_recursive(self, data):
        if not root:
            return
        inorder_recursive(root.lef, result)
        result.append(root.data)
        inorder_recursive(root.right, result)

    def inorder_iterative(root, result):
        if not root:
            return
        stack = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.data)
                node = node.right


def postorder_recursive(self, data):
    if not root:
        return
    inorder_recursive(root.lef, result)
    inorder_recursive(root.right, result)
    result.append(root.data)


def postorder_iterative(root, result):
    if not root:
        return
    visited = []
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node.right and not node.right in visited:
                stack.append(node)
                node = node.right
            else:
                visited.add(node)
                result.append(node.data)
                node = None
