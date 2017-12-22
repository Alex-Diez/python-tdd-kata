import unittest


def path_sum(root, given_sum):
    all_paths = []
    if root is not None:
        path_sum_recursive(root, 0, [], given_sum, all_paths)
    return all_paths


def path_sum_recursive(root, prev, path, given_sum, all_paths):
    if root is not None:
        path.append(root.val())
        current = root.val() + prev
        if root.is_leaf() and given_sum == current:
            all_paths.append(path)
        else:
            path_sum_recursive(root.left(), current, list(path), given_sum, all_paths)
            path_sum_recursive(root.right(), current, list(path), given_sum, all_paths)


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self._val = val
        self._left = left
        self._right = right

    def val(self):
        return self._val

    def is_leaf(self):
        return self._left is None and self._right is None

    def left(self):
        return self._left

    def right(self):
        return self._right


class PathSumTest(unittest.TestCase):
    def testPathSumOfNullTree(self):
        self.assertEqual(path_sum(None, 10), [])

    def testOnlyRoot_sumEqRootVal(self):
        self.assertEqual(path_sum(TreeNode(10), 10), [[10]])

    def testOnlyRoot_sumNotEqRootVal(self):
        self.assertEqual(path_sum(TreeNode(20), 10), [])

    def testTwoLevelTree_leftInPath(self):
        self.assertEqual(path_sum(TreeNode(3, TreeNode(5), TreeNode(4)), 8), [[3, 5]])

    def testNegativeSum(self):
        self.assertEqual(path_sum(TreeNode(0, TreeNode(-1), TreeNode(-1)), -1), [[0, -1], [0, -1]])

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
