import unittest


def path_sum(root, given_sum):
    return path_sum_recursive(root, given_sum, 0, [])


def path_sum_recursive(root, given_sum, prev, path):
    if root is not None:
        path.append(root.val)
        current = root.val + prev
        if root.is_leaf() and current == given_sum:
            return [path]
        else:
            return path_sum_recursive(root.left, given_sum, current, list(path)) \
                   + path_sum_recursive(root.right, given_sum, current, list(path))
    return []


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None


class PathSumTest(unittest.TestCase):
    def testEmptyPaths_whenEmptyTree(self):
        self.assertEqual([], path_sum(None, 10))

    def testOnlyRoot_sumEqRootVal(self):
        self.assertEqual([[10]], path_sum(TreeNode(10), 10))

    def testOnlyRoot_sumNotEqRootVal(self):
        self.assertEqual([], path_sum(TreeNode(20), 10))

    def testTwoLevel_leftInPath(self):
        self.assertEqual([[3, 4]], path_sum(TreeNode(3, TreeNode(4), TreeNode(5)), 7))

    def testTwoLevel_bothInPath(self):
        self.assertEqual([[1, -1], [1, -1]], path_sum(TreeNode(1, TreeNode(-1), TreeNode(-1)), 0))

    def testStopsOnLeaves(self):
        self.assertEqual([[0, 0]], path_sum(TreeNode(0, TreeNode(0)), 0))

    def testBigTree(self):
        self.assertEqual(
            path_sum(
                TreeNode(
                    5,
                    TreeNode(
                        4,
                        TreeNode(
                            11,
                            TreeNode(7),
                            TreeNode(2)
                        ),
                    ),
                    TreeNode(
                        8,
                        TreeNode(13),
                        TreeNode(
                            4,
                            TreeNode(5),
                            TreeNode(1)
                        )
                    )
                ),
                22
            ),
            [[5, 4, 11, 2], [5, 8, 4, 5]]
        )
