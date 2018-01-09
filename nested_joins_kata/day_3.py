import unittest


def join_left(left_set, right_set):
    return _nested_join(left_set, right_set, _left_compact)


def _left_compact(key, primary_val, secondary_val):
    return key, primary_val, secondary_val


def join_right(left_set, right_set):
    return _nested_join(right_set, left_set, _right_compact)


def _right_compact(key, primary_val, secondary_val):
    return key, secondary_val, primary_val


def _nested_join(primary, secondary, compact_tuple):
    return {compact_tuple(key, value, _find_secondary_value(secondary, key)) for key, value in primary}


def _find_secondary_value(values_set, key):
    return next(_extract_value_from(values_set, key), None)


def _extract_value_from(values_set, key):
    return map(lambda t: t[1], _find_tuple_by_key(values_set, key))


def _find_tuple_by_key(values_set, key):
    return filter(lambda t: t[0] == key, values_set)


class NestedJoinsTest(unittest.TestCase):
    def testResultSetIsEmpty_whenJoinLeftTwoEmptySets(self):
        self.assertEqual(set(), join_left(set(), set()))

    def testResultSetHasNoneOnRight_whenJoinLeftNonemptyAndEmptySet(self):
        self.assertEqual(
            {(1, 'l1', None), (2, 'l2', None), (3, 'l3', None)},
            join_left(
                {(1, 'l1'), (2, 'l2'), (3, 'l3')},
                set()
            )
        )

    def testResultSetHasValueOnRight_forCorrespondingKeysInRightSet_whenJoinLeft(self):
        self.assertEqual(
            {(1, 'l1', 'r1'), (2, 'l2', None), (3, 'l3', 'r3')},
            join_left(
                {(1, 'l1'), (2, 'l2'), (3, 'l3')},
                {(1, 'r1'), (3, 'r3')}
            )
        )

    def testResultSetIsEmpty_whenJoinRightTwoEmptySets(self):
        self.assertEqual(set(), join_right(set(), set()))

    def testResultSetHasNoneOnLeft_whenJoinRightEmptyAndNonemptySet(self):
        self.assertEqual(
            {(1, None, 'r1'), (2, None, 'r2'), (3, None, 'r3')},
            join_right(
                set(),
                {(1, 'r1'), (2, 'r2'), (3, 'r3')}
            )
        )

    def testResultSetHasValuesOnLeft_forCorrespondingKeysInLeftSet_whenJoinRight(self):
        self.assertEqual(
            {(1, 'l1', 'r1'), (2, None, 'r2'), (3, 'l3', 'r3')},
            join_right(
                {(1, 'l1'), (3, 'l3')},
                {(1, 'r1'), (2, 'r2'), (3, 'r3')}
            )
        )
