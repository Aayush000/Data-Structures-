from math import inf
from collections import defaultdict

# Tree Bonus Problems! Solutions


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def max_value(root):
    if not root:
        return -inf

    return max(max_value(root.left), root.val, max_value(root.right))

# def max_value_path(root):
#     path = []
#     helper(root, path)
#     return path

# def helper(root, path):
#     if not root:
#         return path
#     path.append(root.val)

#     if root.val


def height(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 0

    return 1 + max(height(root.left), height(root.right))


def most_common_value(root):
    frequencies = defaultdict(int)
    get_counts(root, frequencies)

    common_val = None
    highest_count = 0
    for val, freq in frequencies.items():
        if freq > highest_count:
            hightest_count = freq
            common_val = val

    return common_val


def get_counts(root, frequencies):
    if not root:
        return

    get_counts(root.left, frequencies)
    frequencies[root.val] += 1
    get_counts(root.right, frequencies)


# Test cases
root = TreeNode(7,
                TreeNode(2,
                         TreeNode(4),
                         TreeNode(8,
                                  TreeNode(1),
                                  TreeNode(5))),
                TreeNode(4,
                         TreeNode(7),
                         TreeNode(7)))
print(max_value(root))
print(most_common_value(root))
print(height(root))
