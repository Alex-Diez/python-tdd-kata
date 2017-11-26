import unittest


class PersistentList(object):
    def __repr__(self):
        return ''

    def prepend(self, item):
        return _Node(item, self)

    def head(self):
        pass

    def tail(self):
        pass

    def __add__(self, other):
        return other

    def map(self, mapper):
        return self

    def filter(self, predicate):
        return self


class _Node(PersistentList):
    def __init__(self, head, tail):
        self._head = head
        self._tail = tail

    def __repr__(self):
        tail_repr = repr(self._tail)
        if tail_repr is '':
            return repr(self._head)
        else:
            return repr(self._head) + ', ' + tail_repr

    def head(self):
        return self._head

    def tail(self):
        return self._tail

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.head() is other.head() and self.tail() == self.tail()
        else:
            return False

    def __add__(self, other):
        return (self.tail() + other).prepend(self.head())

    def map(self, mapper):
        return self.tail().map(mapper).prepend(mapper(self.head()))

    def filter(self, predicate):
        filtered_tail = self.tail().filter(predicate)
        if predicate(self.head()):
            return filtered_tail.prepend(self.head())
        else:
            return filtered_tail


class PersistentListTest(unittest.TestCase):
    def setUp(self):
        self.empty = PersistentList()

    def testCreateList(self):
        self.assertEqual('', repr(self.empty))

    def testPrependToList(self):
        self.assertEqual('3, 2, 1', repr(self.empty.prepend(1).prepend(2).prepend(3)))

    def testHeadOfEmptyList(self):
        self.assertEqual(None, self.empty.head())

    def testHeadOfNonemptyList(self):
        nonempty = self.empty.prepend(1).prepend(2)

        self.assertEqual(2, nonempty.head())

    def testTailOfEmptyList(self):
        self.assertEqual(None, self.empty.tail())

    def testTailOfNonemptyList(self):
        nonempty = self.empty.prepend(1).prepend(2).prepend(3)

        self.assertEqual(self.empty.prepend(1).prepend(2), nonempty.tail())

    def testConcatenationOfTwoEmptyLists(self):
        self.assertEqual(self.empty, self.empty + self.empty)

    def testConcatenationOfEmpty_andNonemptyLists(self):
        nonempty = self.empty.prepend(1).prepend(2).prepend(3)

        self.assertEqual(nonempty, self.empty + nonempty)
        self.assertEqual(nonempty, nonempty + self.empty)

    def testConcatenationOfTwoNonemptyLists(self):
        nonempty = self.empty.prepend(1).prepend(2).prepend(3)
        the_other_nonempty = self.empty.prepend(4).prepend(5).prepend(6)

        self.assertEqual('6, 5, 4, 3, 2, 1', repr(the_other_nonempty + nonempty))
        self.assertEqual('3, 2, 1, 6, 5, 4', repr(nonempty + the_other_nonempty))

    def testMapOverEmptyList(self):
        self.assertEqual(self.empty, self.empty.map(lambda e: e * 2))

    def testMapOverNonemptyList(self):
        nonempty = self.empty.prepend(1).prepend(2).prepend(3)

        self.assertEqual(self.empty.prepend(2).prepend(4).prepend(6), nonempty.map(lambda e: e * 2))

    def testFilterEmptyList(self):
        self.assertEqual(self.empty, self.empty.filter(lambda e: e > 3))

    def testFilterNonemptyList(self):
        nonempty = self.empty.prepend(1).prepend(2).prepend(3)

        self.assertEqual(self.empty.prepend(1), nonempty.filter(lambda e: e < 2))