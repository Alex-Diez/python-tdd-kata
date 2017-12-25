import unittest
from collections import deque


def path_sum(root, given_sum):
    all_path = []
    if root is not None:
        queue = deque([])
        queue.append(TreeNodeWrapper(root, 0, []))
        while len(queue) > 0:
            node = queue.popleft()
            node.append_path()
            if node.current_sum() == given_sum and node.is_leaf():
                all_path.append(node.path)
            else:
                if node.has_left():
                    queue.append(node.left_wrapper())
                if node.has_right():
                    queue.append(node.right_wrapper())
    return all_path


class TreeNodeWrapper(object):
    def __init__(self, node, prev, path):
        self.node = node
        self.prev = prev
        self.path = path

    def is_leaf(self):
        return self.node.is_leaf()

    def current_sum(self):
        return self.node.val + self.prev

    def append_path(self):
        self.path.append(self.node.val)

    def has_left(self):
        return self.node.left is not None

    def left_wrapper(self):
        return TreeNodeWrapper(self.node.left, self.current_sum(), list(self.path))

    def has_right(self):
        return self.node.right is not None

    def right_wrapper(self):
        return TreeNodeWrapper(self.node.right, self.current_sum(), list(self.path))


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None


class PathSumTest(unittest.TestCase):
    def testEmptyTree(self):
        self.assertEqual([], path_sum(None, 10))

    def testOnlyRoot_sumEqRootVal(self):
        self.assertEqual([[10]], path_sum(TreeNode(10), 10))

    def testOnlyRoot_sumNotEqRootVal(self):
        self.assertEqual([], path_sum(TreeNode(20), 10))

    def testTwoLevel_leftInPath(self):
        self.assertEqual([[3, 4]], path_sum(TreeNode(3, TreeNode(4), TreeNode(5)), 7))

    def testNegativeSum(self):
        self.assertEqual([[0, -1], [0, -1]], path_sum(TreeNode(0, TreeNode(-1), TreeNode(-1)), -1))
