import unittest


def join_left(left_set, right_set):
    return _nested_join(left_set, right_set, _left_combine)


def _left_combine(key, primary_val, secondary_val):
    return key, primary_val, secondary_val


def join_right(left_set, right_set):
    return _nested_join(right_set, left_set, _right_combine)


def _right_combine(key, primary_val, secondary_val):
    return key, secondary_val, primary_val


def _nested_join(primary, secondary, combine):
    return {combine(key, primary_val, _retrieve_value_from_set(secondary, key)) for key, primary_val in primary}


def _retrieve_value_from_set(data_set, key):
    return next(map(_extract_value, _find_value_by_key(data_set, key)), None)


def _extract_value(pair):
    return pair[1]


def _find_value_by_key(data_set, key):
    return filter(lambda pair: pair[0] == key, data_set)


class NestedJoinTest(unittest.TestCase):
    def testResultSetIsEmpty_whenJoinLeftTwoEmptySets(self):
        self.assertEqual(set(), join_left(set(), set()))

    def testResultSetHasNoneOnRight_whenJoinLeftNonemptyAndEmptySets(self):
        self.assertEqual(
            {(1, 'l1', None), (2, 'l2', None), (3, 'l3', None)},
            join_left(
                {(1, 'l1'), (2, 'l2'), (3, 'l3')},
                set()
            )
        )

    def testResultSetHasValuesOnRight_forCorrespondingKeys_whenJoinLeftTwoNonemptySets(self):
        self.assertEqual(
            {(1, 'l1', 'r1'), (2, 'l2', None), (3, 'l3', 'r3')},
            join_left(
                {(1, 'l1'), (2, 'l2'), (3, 'l3')},
                {(1, 'r1'), (3, 'r3')}
            )
        )

    def testResultSetIsEmpty_whenJoinRightTwoEmptySets(self):
        self.assertEqual(set(), join_right(set(), set()))

    def testResultSetHasNoneOnLeft_whenJoinRightEmptyAndNonemptySets(self):
        self.assertEqual(
            {(1, None, 'r1'), (2, None, 'r2'), (3, None, 'r3')},
            join_right(
                set(),
                {(1, 'r1'), (2, 'r2'), (3, 'r3')}
            )
        )

    def testResultSetHasValuesOnLeft_forCorrespondingKeys_whenJoinRightTwoNonemptySets(self):
        self.assertEqual(
            {(1, 'l1', 'r1'), (2, None, 'r2'), (3, 'l3', 'r3')},
            join_right(
                {(1, 'l1'), (3, 'l3')},
                {(1, 'r1'), (2, 'r2'), (3, 'r3')}
            )
        )
