import unittest


def join_left(left_set, right_set):
    return _nested_join(left_set, right_set, _combine_left)


def _combine_left(key, primary_val, secondary_val):
    return key, primary_val, secondary_val


def join_right(left_set, right_set):
    return _nested_join(right_set, left_set, _combine_right)


def _combine_right(key, primary_val, secondary_val):
    return key, secondary_val, primary_val


def _nested_join(primary, secondary, combine):
    return {combine(key, val, _found_secondary_val(secondary, key)) for (key, val) in primary}


def _found_secondary_val(secondary, key):
    return next(_extract_value(key, secondary), None)


def _extract_value(key, secondary):
    return map(lambda pair: pair[1], _find_pair(secondary, key))


def _find_pair(secondary, key):
    return filter(lambda pair: pair[0] == key, secondary)


class NestedJoinsTest(unittest.TestCase):
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
