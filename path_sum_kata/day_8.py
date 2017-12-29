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
            current = node.val + prev
            if node.is_leaf() and current == given_sum:
                all_paths.append(path)
            else:
                if node.has_left():
                    queue.append((node.left, current, list(path)))
                if node.has_right():
                    queue.append((node.right, current, list(path)))
    return all_paths


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def is_leaf(self):
        return not (self.has_left() or self.has_right())

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None


class PathSumTest(unittest.TestCase):
    def testEmptyPaths_whenEmptyTree(self):
        self.assertEqual([], path_sum(None, 10))

    def testOnlyRoot_sumEqRootVal(self):
        self.assertEqual([[10]], path_sum(TreeNode(10), 10))

    def testOnlyRoot_sumNotEqRootVal(self):
        self.assertEqual([], path_sum(TreeNode(20), 10))

    def testTwoLevel_leftNodeInPath(self):
        self.assertEqual([[3, 4]], path_sum(TreeNode(3, TreeNode(4), TreeNode(5)), 7))

    def testTwoLevel_bothNodeInPath(self):
        self.assertEqual([[1, -1], [1, -1]], path_sum(TreeNode(1, TreeNode(-1), TreeNode(-1)), 0))

    def testOnlyLeafEndsSearch(self):
        self.assertEqual([[0, -1, 1]], path_sum(TreeNode(0, TreeNode(-1, TreeNode(1))), 0))
