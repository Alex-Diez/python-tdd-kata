import unittest
from collections import deque


def path_sum(root, given_sum):
    all_path = []
    queue = deque([])
    add_to_queue(queue, root)
    while len(queue) > 0:
        node = queue.popleft()
        node.add_to_path()
        current_sum = node.current_sum()
        if node.is_leaf() and current_sum == given_sum:
            all_path.append(node.path)
        else:
            path = tuple(node.copy_path())
            add_to_queue(queue, node.left(), current_sum, path)
            add_to_queue(queue, node.right(), current_sum, path)
    return all_path


def add_to_queue(queue, node, current_sum=0, path=()):
    if node is not None:
        queue.append(TreeNodeWrapper(node, current_sum, list(path)))


class TreeNodeWrapper(object):
    def __init__(self, node, prev, path):
        self.node = node
        self.prev = prev
        self.path = path

    def is_leaf(self):
        return self.node.left is None and self.node.right is None

    def val(self):
        return self.node.val

    def left(self):
        return self.node.left

    def right(self):
        return self.node.right

    def add_to_path(self):
        self.path.append(self.node.val)

    def current_sum(self):
        return self.val() + self.prev

    def copy_path(self):
        return list(self.path)


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None


class PathSumTest(unittest.TestCase):
    def testNothing(self):
        pass

    def testPathSumOfEmptyTree(self):
        self.assertEqual(path_sum(None, 10), [])

    def testOnlyRoot_sumEqRootVal(self):
        self.assertEqual(path_sum(TreeNode(10), 10), [[10]])

    def testOnlyRoot_sumNotEqRootVal(self):
        self.assertEqual(path_sum(TreeNode(20), 10), [])

    def testTwoLevel_leftInPath(self):
        self.assertEqual(path_sum(TreeNode(3, TreeNode(4), TreeNode(5)), 7), [[3, 4]])

    def testNegativeSum(self):
        self.assertEqual(path_sum(TreeNode(0, TreeNode(-1), TreeNode(-1)), -1), [[0, -1], [0, -1]])
