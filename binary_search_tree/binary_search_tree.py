# Definition for a binary tree node.
# Runs on python 3.10+

tree_compatible_type = set | list | tuple | None


class TreeNode:
    """
    Represents a node in a binary tree.

    Attributes:
        val (int | None): The value stored in the node.
        left (TreeNode): The left child node.
        right (TreeNode): The right child node.
    """

    def __init__(
        self, val: int | None = None, left: "TreeNode" = None, right: "TreeNode" = None
    ) -> "TreeNode":
        """
        Initializes a TreeNode with the given value and optional left and right children.

        Args:
            val (int | None): The value to store in the node.
            left (TreeNode): The left child node.
            right (TreeNode): The right child node.

        Returns:
            TreeNode: A TreeNode instance.
        """
        self.val = val
        self.left = left
        self.right = right


class Tree:
    """
    Represents a binary tree and provides methods for tree operations.

    Attributes:
        tree_data (tree_compatible_type): The data used to construct the tree.
        root_node (TreeNode): The root node of the binary tree.
    """

    def __init__(self, tree_data: tree_compatible_type = None) -> "Tree":
        """
        Initializes a Tree with the given tree_data (can be set, list, tuple, or None).

        Args:
            tree_data (tree_compatible_type): The data used to construct the tree.

        Returns:
            Tree: A Tree instance.
        """
        self.tree_data = tree_data
        self.root_node = None
        if tree_data and isinstance(tree_data, (set, list, tuple)):
            self.construct_tree(tree_data)

    def construct_tree(self, tree_data: tree_compatible_type):
        """
        Constructs the binary tree using the provided tree_data.

        Args:
            tree_data (tree_compatible_type): The data used to construct the tree.
        """
        tree_data_clone = tree_data.copy()
        self.root_node = TreeNode(val=tree_data_clone[0])
        current_node = self.root_node

        for val in tree_data_clone[1:]:
            self.insert(val, current_node)

    def traverse(self, node: TreeNode, values: list | None = None) -> list | None:
        """
        Performs an in-order traversal of the binary tree and returns the values.

        Args:
            node (TreeNode): The current node being traversed.
            values (list | None): A list to store the values during traversal.

        Returns:
            list | None: A list of values in in-order traversal order.
        """
        if node is None:
            return None

        # It's quite bad setting a default array in the method's definition in Python,
        # hence we set it here.
        if values is None:
            values = []

        if node.left is not None:
            self.traverse(node.left, values)

        values.append(node.val)

        if node.right is not None:
            self.traverse(node.right, values)

        return values

    def search(self, val: any, node: TreeNode | None) -> TreeNode | None:
        if node is None or node.val == val:
            return node
        if val < node.val:
            return self.search(val, node.left)
        else:
            return self.search(val, node.right)

    def insert(self, val: int, node: TreeNode | None):
        if node is None:
            return

        if val not in self.tree_data:
            self.tree_data.append(val)

        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val=val)
            else:
                self.insert(val, node.left)
        elif val > node.val:
            if node.right is None:
                node.right = TreeNode(val=val)
            else:
                self.insert(val, node.right)

    def delete(self, val: int, node: TreeNode | None):
        if node is None:
            return node

        if val < node.val:
            node.left = self.delete(val, node.left)
            return node
        elif val > node.val:
            node.right = self.delete(val, node.right)
            return node
        elif val == node.val:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.right = self.find_successor_node(target_node=node, node=node.right)
                return node

    def find_successor_node(self, target_node: TreeNode, node: TreeNode | None):
        if node.left:
            node.left = self.find_successor_node(target_node, node.left)
            return node
        else:
            target_node.val = node.val
            return node.right

    def nodes(self):
        """
        Returns the tree_data attribute, which contains all the values in the tree.

        Returns:
            tree_compatible_type: The tree data.
        """
        return self.tree_data


tree_data = [50, 25, 10, 33, 4, 11, 75, 56, 89, 52, 61, 82, 95, 12]
tree = Tree(tree_data)
res = tree.traverse(tree.root_node)

print(res)
