import unittest


def path_sum(root, given_sum):
    if root is not None:
        return path_sum_recursive(root, given_sum, 0, [])
    else:
        return []


def path_sum_recursive(node, given_sum, prev, path):
    paths = []
    path.append(node.val)
    if node.is_leaf() and node.val + prev == given_sum:
        paths.append(path)
    else:
        for child in node:
            paths += path_sum_recursive(child, given_sum, node.val + prev, list(path))
    return paths


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None

    def __iter__(self):
        return filter(lambda node: node is not None, [self.left, self.right])


class PathSumTest(unittest.TestCase):
    def testEmptyPath_whenEmptyTree(self):
        self.assertEqual([], path_sum(None, 10))

    def testOnlyRoot_sumEqRootVal(self):
        self.assertEqual([[10]], path_sum(TreeNode(10), 10))

    def testOnlyRoot_sumNotEqRootVal(self):
        self.assertEqual([], path_sum(TreeNode(20), 10))

    def testTwoLevels_leftInPath(self):
        self.assertEqual([[3, 4]], path_sum(TreeNode(3, TreeNode(4), TreeNode(5)), 7))

    def testTwoLevels_bothInPath(self):
        self.assertEqual([[1, -1], [1, -1]], path_sum(TreeNode(1, TreeNode(-1), TreeNode(-1)), 0))

    def testStopOnLeaves(self):
        self.assertEqual([[0, 1, -1]], path_sum(TreeNode(0, TreeNode(1, TreeNode(-1))), 0))

    def testBigTree(self):
        self.assertEqual(
            [[5, 4, 11, 2], [5, 8, 4, 5]],
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
            )
        )
