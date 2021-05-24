# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode):
        if root == None:
            return []

        self.tmp = []
        self.biTree(root)

        return self.tmp

    def biTree(self, node):
        self.tmp.append(node.val)
        if node.left:
            self.biTree(node.left)
        if node.right:
            self.biTree(node.right)

