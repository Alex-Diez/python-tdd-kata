import unittest


def join_left(left_set, right_set):
    result_set = set()
    for (left_key, left_val) in left_set:
        found_right_val = None
        for (right_key, right_val) in right_set:
            if right_key == left_key:
                found_right_val = right_val
                break
        result_set.add((left_key, left_val, found_right_val))
    return result_set


def join_right(left_set, right_set):
    result_set = set()
    for (key, r_val, l_val) in join_left(right_set, left_set):
        result_set.add((key, l_val, r_val))
    return result_set


class NestedJoinTest(unittest.TestCase):
    def testResultSetIsEmpty_whenJoinLeftTwoEmptySets(self):
        self.assertEqual(set(), join_left(set(), set()))

    def testResultSetHasNone_whenNonemptySetJoinedWithEmpty(self):
        self.assertEqual(
            {(1, 'l1', None), (2, 'l2', None), (3, 'l3', None)},
            join_left(
                {(1, 'l1'), (2, 'l2'), (3, 'l3')},
                set()
            )
        )

    def testResultSetHasValue_forCorrespondingKeysInLeftSet(self):
        self.assertEqual(
            {(1, 'l1', 'r1'), (2, 'l2', None), (3, 'l3', 'r3')},
            join_left(
                {(1, 'l1'), (2, 'l2'), (3, 'l3')},
                {(1, 'r1'), (3, 'r3')}
            )
        )

    def testResultSet_ofRightJoinTwoNonemptySet(self):
        self.assertEqual(
            {(1, 'l1', 'r1'), (2, None, 'r2'), (3, 'l3', 'r3')},
            join_right(
                {(1, 'l1'), (3, 'l3')},
                {(1, 'r1'), (2, 'r2'), (3, 'r3')}
            )
        )
