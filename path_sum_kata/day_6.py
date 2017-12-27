import unittest
import collections


def path_sum(root, given_sum):
    all_path = []
    queue = collections.deque([])
    if root is not None:
        queue.append(TreeNodeWrapper(root, 0, []))
        while len(queue) > 0:
            node = queue.popleft()
            node.append_path()
            if node.is_leaf() and node.current_val() == given_sum:
                all_path.append(node.path)
            else:
                if node.has_left():
                    queue.append(node.left_node())
                if node.has_right():
                    queue.append(node.right_node())
    return all_path


class TreeNodeWrapper(object):
    def __init__(self, node, prev, path):
        self.node = node
        self.prev = prev
        self.path = path

    def append_path(self):
        self.path.append(self.node.val)

    def current_val(self):
        return self.prev + self.node.val

    def is_leaf(self):
        return self.node.left is None and self.node.right is None

    def has_left(self):
        return self.node.left is not None

    def left_node(self):
        return TreeNodeWrapper(self.node.left, self.current_val(), list(self.path))

    def has_right(self):
        return self.node.right is not None

    def right_node(self):
        return TreeNodeWrapper(self.node.right, self.current_val(), list(self.path))


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class PathSumTest(unittest.TestCase):
    def testEmptyPaths_whenEmptyTree(self):
        self.assertEqual([], path_sum(None, 10))

    def testRootOnly_sumEqRootVal(self):
        self.assertEqual([[10]], path_sum(TreeNode(10), 10))

    def testRootOnly_sumNotEqRootVal(self):
        self.assertEqual([], path_sum(TreeNode(20), 10))

    def testTwoLevelTree_whenLeftNodeInPath(self):
        self.assertEqual([[3, 4]], path_sum(TreeNode(3, TreeNode(4), TreeNode(5)), 7))

    def testTwoLevelTree_whenBothNodeInPath(self):
        self.assertEqual([[0, -1], [0, -1]], path_sum(TreeNode(0, TreeNode(-1), TreeNode(-1)), -1))

    def testSumOverflow(self):
        self.assertEqual([], path_sum(TreeNode(1, TreeNode(-1), TreeNode(-1)), 1))
