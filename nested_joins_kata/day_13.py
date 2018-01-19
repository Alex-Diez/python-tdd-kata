import unittest


def join_left(left_set, right_set):
    return _nested_join(left_set, right_set, _compose_left)


def _compose_left(key, primary, secondary):
    return key, primary, secondary


def join_right(left_set, right_set):
    return _nested_join(right_set, left_set, _compose_right)


def _compose_right(key, primary, secondary):
    return key, secondary, primary


def _nested_join(primary_set, secondary_set, compose):
    return {compose(key, val, _retrieve_val_from_set_by_key(key, secondary_set)) for (key, val) in primary_set}


def _retrieve_val_from_set_by_key(key, secondary_set):
    return next(_extract_value(key, secondary_set), None)


def _extract_value(key, secondary_set):
    return map(lambda pair: pair[1], _find_pair_in_set(secondary_set, key))


def _find_pair_in_set(secondary_set, key):
    return filter(lambda pair: pair[0] == key, secondary_set)


class NestedJoinsTest(unittest.TestCase):
    def testResultSetIsEmpty_whenJoinLeftTwoEmptySets(self):
        self.assertEqual(set(), join_left(set(), set()))

    def testResultSetHasNonesOnRight_whenJoinLeftNonemptyAndEmptySets(self):
        self.assertEqual(
            {(1, 'l1', None), (2, 'l2', None), (3, 'l3', None)},
            join_left(
                {(1, 'l1'), (2, 'l2'), (3, 'l3')},
                set()
            )
        )

    def testResultSetHasValues_forCorrespondingKeys_whenJoinLeftTwoNonemptySets(self):
        self.assertEqual(
            {(1, 'l1', 'r1'), (2, 'l2', None), (3, 'l3', 'r3')},
            join_left(
                {(1, 'l1'), (2, 'l2'), (3, 'l3')},
                {(1, 'r1'), (3, 'r3')}
            )
        )

    def testResultSetIsEmpty_whenJoinRightTwoEmptySets(self):
        self.assertEqual(set(), join_right(set(), set()))

    def testResultSetHasNonesOnLeft_whenJoinRightNonemptyAndEmptySets(self):
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
