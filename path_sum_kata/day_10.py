import unittest
import collections


def path_sum(root, given_sum):
    queue = collections.deque([])
    all_paths = []
    queue.append((root, 0, []))
    while len(queue) > 0:
        node, prev, path = queue.popleft()
        if node is not None:
            path.append(node.val)
            current = node.val + prev
            if current == given_sum and node.is_leaf():
                all_paths.append(path)
            else:
                queue.append((node.left, current, list(path)))
                queue.append((node.right, current, list(path)))
    return all_paths


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

    def testTwoLevel_bothNodeInPath(self):
        self.assertEqual([[1, -1], [1, -1]], path_sum(TreeNode(1, TreeNode(-1), TreeNode(-1)), 0))

    def testStopOnLeaves(self):
        self.assertEqual([[0, 1, -1]], path_sum(TreeNode(0, TreeNode(1, TreeNode(-1))), 0))

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
