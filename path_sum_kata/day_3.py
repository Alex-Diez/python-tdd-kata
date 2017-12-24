import unittest


def path_sum(root, given_sum):
    all_path = []
    path_sum_recursive(root, given_sum, 0, [], all_path)
    return all_path


def path_sum_recursive(root, given_sum, prev, path, all_paths):
    if root is not None:
        path.append(root.val)
        if root.is_leaf() and root.val + prev == given_sum:
            all_paths.append(path)
        else:
            path_sum_recursive(root.left, given_sum, root.val + prev, list(path), all_paths),
            path_sum_recursive(root.right, given_sum, root.val + prev, list(path), all_paths)


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
