import unittest


def join_left(left_set, right_set):
    return _nested_join(left_set, right_set, _left_compose)


def _left_compose(key, primary_val, secondary_val):
    return key, primary_val, secondary_val


def join_right(left_set, right_set):
    return _nested_join(right_set, left_set, _right_compose)


def _right_compose(key, primary_val, secondary_val):
    return key, secondary_val, primary_val


def _nested_join(primary, secondary, compose):
    return {compose(key, val, _find_val_in_set(key, secondary)) for (key, val) in primary}


def _find_val_in_set(key, secondary):
    return next(_extract_val(secondary, key), None)


def _extract_val(secondary, key):
    return map(lambda pair: pair[1], _find_pair_by_key(secondary, key))


def _find_pair_by_key(secondary, key):
    return filter(lambda pair: pair[0] == key, secondary)


class NestedJoinsTest(unittest.TestCase):
    def testResultSetIsEmpty_whenJoinLeftTwoEmptySets(self):
        self.assertEqual(set(), join_left(set(), set()))

    def testResultSetsHasNoneOnRight_whenJoinLeftNonemptyAndEmptySets(self):
        self.assertEqual(
            {(1, 'l1', None), (2, 'l2', None), (3, 'l3', None)},
            join_left(
                {(1, 'l1'), (2, 'l2'), (3, 'l3')},
                set()
            )
        )

    def testResultSetsHasValuesOnRight_forCorrespondingKeys_whenJoinTwoNonemptySets(self):
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

    def testResultSetHasValueOnLeft_forCorrespondingKeys_whenJoinRightTwoNonemptySets(self):
        self.assertEqual(
            {(1, 'l1', 'r1'), (2, None, 'r2'), (3, 'l3', 'r3')},
            join_right(
                {(1, 'l1'), (3, 'l3')},
                {(1, 'r1'), (2, 'r2'), (3, 'r3')}
            )
        )
