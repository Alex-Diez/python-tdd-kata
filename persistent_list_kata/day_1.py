import unittest


class List(object):
    def append(self, item):
        return Node(item, self)

    def head(self):
        pass

    def tail(self):
        pass

    def __repr__(self):
        return ''

    def __add__(self, other):
        return other


class EmptyList(List):
    def head(self):
        return None

    def tail(self):
        return None

    def __repr__(self):
        return ''


class Node(List):
    def __init__(self, item, _next):
        self._item = item
        self._next = _next

    def head(self):
        return self._item

    def tail(self):
        return self._next

    def __repr__(self):
        next_str = repr(self._next)
        if next_str is '':
            return repr(self._item)
        else:
            return repr(self._item) + ', ' + next_str

    def __add__(self, other):
        if other.head() is None:
            return self
        else:
            return (self.tail() + other).append(self.head())


class PersistentListTest(unittest.TestCase):
    def testAppendToList(self):
        persistent_list = List().append(1)

        self.assertEqual('1', repr(persistent_list))

    def testAppendManyItemsToList(self):
        persistent_list = List().append(1).append(2).append(3)

        self.assertEqual('3, 2, 1', repr(persistent_list))

    def testHeadOfEmptyList_isNone(self):
        self.assertIsNone(List().head())

    def testHeadOfList_isTheFirstItem(self):
        persistent_list = List().append(1).append(2)

        self.assertEqual(2, persistent_list.head())

    def testTailOfEmptyList_isNone(self):
        self.assertIsNone(List().tail())

    def testTailOfList_isTheRestOfList_exceptTheFirstItem(self):
        persistent_list = List().append(1).append(2)
        self.assertEqual(persistent_list, persistent_list.append(3).tail())

    def testConcatenationOfTwoEmptyLists(self):
        self.assertEqual('', repr(List() + List()))

    def testConcatenationEmpty_andNonemptyList(self):
        self.assertEqual('3, 2, 1', repr(List() + List().append(1).append(2).append(3)))
        self.assertEqual('3, 2, 1', repr(List().append(1).append(2).append(3) + List()))

    def testConcatenationOfTwoNonemptyLists(self):
        the_nonempty = List().append(4).append(5).append(6)
        the_other_nonempty = List().append(1).append(2).append(3)
        self.assertEqual('6, 5, 4, 3, 2, 1', repr(the_nonempty + the_other_nonempty))
