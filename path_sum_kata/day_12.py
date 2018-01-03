import unittest
import collections


def path_sum(root, given_sum):
    all_paths = []
    queue = collections.deque([])
    if root is not None:
        queue.append((root, 0, []))
    while len(queue) > 0:
        node, prev, path = queue.popleft()
        path.append(node.val)
        if node.is_leaf() and node.val + prev == given_sum:
            all_paths.append(path)
        else:
            for child in node:
                queue.append((child, node.val + prev, list(path)))
    return all_paths


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None

    def __iter__(self):
        return filter(lambda child: child is not None, [self.left, self.right])


class PathSumTest(unittest.TestCase):
    def testEmptyPath_whenEmptyTree(self):
        self.assertEqual([], path_sum(None, 10))

    def testRootOnly_sumEqRootVal(self):
        self.assertEqual([[10]], path_sum(TreeNode(10), 10))

    def testRootOnly_sumNotEqRootVal(self):
        self.assertEqual([], path_sum(TreeNode(20), 10))

    def testTwoLevels_leftInPath(self):
        self.assertEqual([[3, 4]], path_sum(TreeNode(3, TreeNode(4), TreeNode(5)), 7))

    def testTwoLevels_bothInPath(self):
        self.assertEqual([[1, -1], [1, -1]], path_sum(TreeNode(1, TreeNode(-1), TreeNode(-1)), 0))

    def testStopOnLeaves(self):
        self.assertEqual([[0, 1, -1]], path_sum(TreeNode(0, TreeNode(1, TreeNode(-1))), 0))
