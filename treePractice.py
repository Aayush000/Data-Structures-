from math import inf
from collections import defaultdict


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


'''
1. remove_leafs(root) - remove all leafs from the tree
2. limit_path(root, limit) - remove all nodes where the sum of nodes on the path
 from root is greater than limit
3. subtree_sum(root) - reset node values to be the sum of their subtrees + their 
initial value
4. combine(root1, root2) - merge tree1 and tree2
'''


def remove_leafs(root):
    '''remove all leafs from the tree'''
    if root:
        if not root.left and not root.right:
            return None
        else:
            root.left = remove_leafs(root.left)
            root.right = remove_leafs(root.right)
    return root


def limit_path(root, limit):
    """Remove all nodes where the sum of the nodes on the path from root to themselves
     is greater than limit.
     For example, given the tree:
     root ->  3
            4   2
          1
     calling root = limit_path(root, 6), would result in the following tree:
     root -> 3
               2
     this is because the path to node 4 exceeded the given limit (ie: 3 + 4 > 6) so it
     and all it's descendents were removed from the tree."""
    if root:
        if root.val > limit:
            return None
        else:
            root.left = limit_path(root.left, limit-root.val)
            root.right = limit_path(root.right, limit-root.val)
    return root


def subtree_sum(root):
    """Updates the values in the tree such that each node's value is equal to the sum
     of values in it's left and right subtrees, plus it's initial value. For example,
     given the initial tree:
     root ->  3
            4   2
          5
     then after calling subtree_sum(root), the tree would look like:
     root ->  14
            9    2
          5
     The changes are as follows. root.left.val == 9 b/c it's subtrees contain a single
     node with value 5 and it's initial value was 4, 5 + 4 = 9.
     root.val == 14 b/c it's left subtree contains a summed value of 9, and it's right
     subtree contains a node with value 2, and it's initial value was 3. 9 + 2 + 3 = 14
  """
    if not root:
        return 0
    else:
        total = root.val + subtree_sum(root.left) + subtree_sum(root.right)
        root.val = total
        return total


def combine(root1, root2):
    """Combines two trees and returns their new root.
     If both trees have a node at a given position, the resulting tree will have a node
     at the same position who's value is the sum of the two input nodes. If only one of
     the trees has input at the given location the result will include an identical node
     in that position. This method should not modify either input.
     For example: given the two trees:
     root1 ->  3
             4

     root2 ->  2
                 7
     then the returned node would be the head of a tree like:
     result -> 5
             4   7
     The result tree has a node at root with value 5 b/c both inputs had a node in that
     position and 3 + 2 = 5. The result has a node at root.left b/c one of the two input
     trees had a node there. The same reasoning dictates the node at root.right"""
    if not root1 and not root2:
        return None
    elif not root1:
        return root2
    elif not root2:
        return root1
    else:
        new_node = TreeNode(root1.val + root2.val)
        new_node.left = combine(root1.left, root2.left)
        new_node.right = combine(root2.right, root2.right)
        return new_node


tree1 = TreeNode(5, TreeNode(2, None, TreeNode(3)))
tree2 = TreeNode(2, TreeNode(7), TreeNode(6, None, TreeNode(4)))

# print(remove_leafs(tree2))
# print(limit_path(tree2, 20))
# print(subtree(tree2))
# print(combine(tree1, tree2))
