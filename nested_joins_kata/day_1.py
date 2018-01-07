import unittest


def join_left(left_set, right_set):
    return _outer_join(left_set, right_set)


def join_right(left_set, right_set):
    result_set = set()
    for (key, right_value, left_value) in _outer_join(right_set, left_set):
        result_set.add((key, left_value, right_value))
    return result_set


def _outer_join(primary_set, secondary_set):
    result_set = set()
    for (main_key, main_value) in primary_set:
        found_secondary_value = None
        for (secondary_key, secondary_value) in secondary_set:
            if secondary_key == main_key:
                found_secondary_value = secondary_value
                break
        result_set.add((main_key, main_value, found_secondary_value))
    return result_set


class NestedJoinTest(unittest.TestCase):
    def testResultSetIsEmpty_whenJoinLeftOfEmptySets(self):
        self.assertEqual(set(), join_left(set(), set()))

    def testResultSetHasNoneValue_whenJoinLeftNonemptySetWithEmpty(self):
        self.assertEqual(
            {(1, 'l1', None), (2, 'l2', None), (3, 'l3', None)},
            join_left(
                {(1, 'l1'), (2, 'l2'), (3, 'l3')},
                set()
            )
        )

    def testResultSetHasValue_forCorrespondingKeysInRightSet(self):
        self.assertEqual(
            {(1, 'l1', 'r1'), (2, 'l2', None), (3, 'l3', 'r3')},
            join_left(
                {(1, 'l1'), (2, 'l2'), (3, 'l3')},
                {(1, 'r1'), (3, 'r3')}
            )
        )

    def testResultSetIsEmpty_whenJoinRightOfEmptySets(self):
        self.assertEqual(set(), join_right(set(), set()))

    def testResultSetHasNoneValue_whenJoinRightEmptySetWithNonempty(self):
        self.assertEqual(
            {(1, None, 'r1'), (2, None, 'r2'), (3, None, 'r3')},
            join_right(
                set(),
                {(1, 'r1'), (2, 'r2'), (3, 'r3')}
            )
        )

    def testResultHasValue_forCorrespondingKeysInLeftSet(self):
        self.assertEqual(
            {(1, 'l1', 'r1'), (2, None, 'r2'), (3, 'l3', 'r3')},
            join_right(
                {(1, 'l1'), (3, 'l3')},
                {(1, 'r1'), (2, 'r2'), (3, 'r3')}
            )
        )
