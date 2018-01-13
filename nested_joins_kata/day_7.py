import unittest


def join_left(left_set, right_set):
    return _nested_join(left_set, right_set, _compose_left)


def _compose_left(key, primary_val, secondary_val):
    return key, primary_val, secondary_val


def _nested_join(primary, secondary, compose):
    return {compose(key, val, _retrieve_val_from_set_by_key(key, secondary)) for (key, val) in primary}


def _retrieve_val_from_set_by_key(key, secondary):
    return next(_extract_val_from_pair(key, secondary), None)


def _extract_val_from_pair(key, secondary):
    return map(lambda pair: pair[1], _find_pair_in_set_by_key(secondary, key))


def _find_pair_in_set_by_key(secondary_set, key):
    return filter(lambda pair: pair[0] == key, secondary_set)


def join_right(left_set, right_set):
    return _nested_join(right_set, left_set, _compose_right)


def _compose_right(key, primary_val, secondary_val):
    return key, secondary_val, primary_val


class NestedJoinsTest(unittest.TestCase):
    def testResultSetIsEmpty_whenLeftJoinTwoEmptySets(self):
        self.assertEqual(set(), join_left(set(), set()))

    def testResultSetHasNoneOnRight_whenLeftJoinNonemptyAndEmptySets(self):
        self.assertEqual(
            {(1, 'l1', None), (2, 'l2', None), (3, 'l3', None)},
            join_left(
                {(1, 'l1'), (2, 'l2'), (3, 'l3')},
                set()
            )
        )

    def testResultSetHasValuesOnRight_forCorrespondingKeys_whenLeftJoinTwoNonemptySets(self):
        self.assertEqual(
            {(1, 'l1', 'r1'), (2, 'l2', None), (3, 'l3', 'r3')},
            join_left(
                {(1, 'l1'), (2, 'l2'), (3, 'l3')},
                {(1, 'r1'), (3, 'r3')}
            )
        )

    def testResultSetIsEmpty_whenRightJoinTwoEmptySets(self):
        self.assertEqual(set(), join_right(set(), set()))

    def testResultSetHasNone_whenRightJoinEmptyAndNonemptySets(self):
        self.assertEqual(
            {(1, None, 'r1'), (2, None, 'r2'), (3, None, 'r3')},
            join_right(
                set(),
                {(1, 'r1'), (2, 'r2'), (3, 'r3')}
            )
        )

    def testResultSetHasValues_forCorrespondingKeys_whenRightJoinTwoNonemptySets(self):
        self.assertEqual(
            {(1, 'l1', 'r1'), (2, None, 'r2'), (3, 'l3', 'r3')},
            join_right(
                {(1, 'l1'), (3, 'l3')},
                {(1, 'r1'), (2, 'r2'), (3, 'r3')}
            )
        )
