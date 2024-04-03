class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if not node.left_child:
                node.left_child = TreeNode(value)
            else:
                self._insert_recursive(node.left_child, value)
        else:
            if not node.right_child:
                node.right_child = TreeNode(value)
            else:
                self._insert_recursive(node.right_child, value)

    def search(self, value):
        return self._search_tree(self.root, value)

    def _search_tree(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_tree(node.left_child, value)
        else:
            return self._search_tree(node.right_child, value)


class RedBlackTree:
    RED = True
    BLACK = False

    class Node:
        def __init__(self, value, color=True):
            self.value = value
            self.color = color
            self.left_child = None
            self.right_child = None

    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)
        self.root.color = self.BLACK  # Ensure root is black

    def _insert(self, node, value):
        if node is None:
            return self.Node(value)

        if value < node.value:
            node.left_child = self._insert(node.left_child, value)
        elif value > node.value:
            node.right_child = self._insert(node.right_child, value)

        if self._is_red_color(node.right_child) and not self._is_red_color(node.left_child):
            node = self._rotate_right(node)
        if self._is_red_color(node.left_child) and self._is_red_color(node.left_child.left_child):
            node = self._rotate_left(node)
        if self._is_red_color(node.left_child) and self._is_red_color(node.right_child):
            self._flip_colors(node)

        return node

    def _is_red_color(self, node):
        return node is not None and node.color == self.RED

    def _rotate_left(self, node):
        x = node.right_child
        node.right_child = x.left_child
        x.left_child = node
        x.color = node.color
        node.color = self.RED
        return x

    def _rotate_right(self, node):
        x = node.left_child
        node.left_child = x.right_child
        x.right_child = node
        x.color = node.color
        node.color = self.RED
        return x

    def _flip_colors(self, node):
        node.color = not node.color
        node.left_child.color = not node.left_child.color
        node.right_child.color = not node.right_child.color

    def search(self, value):
        return self._search_tree(self.root, value)

    def _search_tree(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_tree(node.left_child, value)
        else:
            return self._search_tree(node.right_child, value)


class AVLTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left_child = None
            self.right_child = None
            self.height = 1

    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if not node:
            return self.Node(value)
        if value < node.value:
            node.left_child = self._insert(node.left_child, value)
        else:
            node.right_child = self._insert(node.right_child, value)

        node.height = 1 + max(self._get_height(node.left_child), self._get_height(node.right_child))

        balance = self._get_balance(node)

        # Left Left Case
        if balance > 1 and value < node.left_child.value:
            return self._rotate_right(node)

        # Right Right Case
        if balance < -1 and value > node.right_child.value:
            return self._rotate_left(node)

        # Left Right Case
        if balance > 1 and value > node.left_child.value:
            node.left_child = self._rotate_left(node.left_child)
            return self._rotate_right(node)

        # Right Left Case
        if balance < -1 and value < node.right_child.value:
            node.right_child = self._rotate_right(node.right_child)
            return self._rotate_left(node)

        return node

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left_child) - self._get_height(node.right_child)

    def _rotate_left(self, z):
        y = z.right_child
        T2 = y.left_child

        y.left_child = z
        z.right_child = T2

        z.height = 1 + max(self._get_height(z.left_child), self._get_height(z.right_child))
        y.height = 1 + max(self._get_height(y.left_child), self._get_height(y.right_child))

        return y

    def _rotate_right(self, y):
        x = y.left_child
        T2 = x.right_child

        x.right_child = y
        y.left_child = T2

        y.height = 1 + max(self._get_height(y.left_child), self._get_height(y.right_child))
        x.height = 1 + max(self._get_height(x.left_child), self._get_height(x.right_child))

        return x

    def search(self, value):
        return self._search_tree(self.root, value)

    def _search_tree(self, node, value):
        if not node:
            return False
        if node:
            return True
