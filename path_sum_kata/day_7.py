import unittest


def path_sum(root, give_sum):
    return path_sum_recursive(root, give_sum, 0, [])


def path_sum_recursive(node, given_sum, prev, path):
    if node is not None:
        path.append(node.val)
        current_val = node.val + prev
        if current_val == given_sum:
            return [path]
        else:
            return path_sum_recursive(node.left, given_sum, current_val, list(path)) \
                   + path_sum_recursive(node.right, given_sum, current_val, list(path))
    return []


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class PathSumTest(unittest.TestCase):
    def testEmptyPaths_whenEmptyTree(self):
        self.assertEqual([], path_sum(None, 10))

    def testOnlyRoot_sumEqRootVal(self):
        self.assertEqual([[10]], path_sum(TreeNode(10), 10))

    def testOnlyRoot_sumNotEqRootVal(self):
        self.assertEqual([], path_sum(TreeNode(20), 10))

    def testTwoLevelTree_leftInPaths(self):
        self.assertEqual([[3, 4]], path_sum(TreeNode(3, TreeNode(4), TreeNode(5)), 7))

    def testTwoLevelTree_bothInPaths(self):
        self.assertEqual([[-1, 1], [-1, 1]], path_sum(TreeNode(-1, TreeNode(1), TreeNode(1)), 0))

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
