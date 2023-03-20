from math import inf
from collections import defaultdict


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


# check if BST contains a target value.
def contains(root, target):
    if not root:
        return False

    if root.val == target:
        return True
    if target < root.val:
        return contains(root.left, target)
    else:
        return contains(root.right, target)


'''
For a balanced tree, the height is equal to O(log2(n)) where n is the number of nodes

Runtime for contains on a balanced BST:
O(log2(n))

Runtime of contains on a balanced binary tree:
O(n)

'''

# Binary seach trees - insert (new nodes will always be leaf)


def insert(root, target):
    if not root:
        return TreeNode(target)
    elif target == root.val:
        return root  # no operation if duplicates
    elif target < root.val:
        root.left = insert(root.left, target)
    elif target > root.val:
        root.right = insert(root.right, target)
    return root

# Implement Remove in BST


def remove(root, target):
    if not root:
        return None
    if target < root.val:
        root.left = remove(root.left, target)
        return root
    elif target > root.val:
        root.right = remove(root.right, target)
        return root
    else:  # target == root.val
        # case1: root is a leaf node
        if not root.left and not root.right:
            return None
        # root.left is None
        elif not root.left:
            return root.right
        # root.right is None
        elif not root.right:
            return root.left
        # has two children
        else:
            replacement = get_max_node(root.left)
            replacement.left = remove(root.left, replacement.val)
            replacement.right = root.right
            return replacement


# get the maximum value in the left side of the tree if the node has two children
# so that i can make that node as root
def get_max_node(root):
    while root and root.right:
        root = root.right
    return root


'''
Operation          Runtime where n is number of nodes
Insert               O(log2(n))
Contains             O(log2(n))
Runtime              O(log2(n))

This only works if the tree is relatively balanced. An unbalanced 
tree could take O(n) for any of these operations.
'''

'''
Trees
------
1. Self-balancing binary search trees
2. Adelson-velskii and landis (AVL)
3. Red-black
4. B
5. Splay
'''
