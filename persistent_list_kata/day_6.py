import unittest


class PersistentList(object):
    def __repr__(self):
        return ''

    def prepend(self, item):
        return _Node(item, self)

    def head(self):
        pass

    def tail(self):
        return self

    def __add__(self, other):
        return other

    def filter(self, predicate):
        return self

    def map(self, mapper):
        return self

    def __eq__(self, other):
        return isinstance(other, self.__class__) \
               and other.head() is None


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
        return isinstance(other, self.__class__) \
               and self.head() == other.head() \
               and self.tail() == other.tail()

    def __add__(self, other):
        return (self.tail() + other).prepend(self.head())

    def filter(self, predicate):
        if predicate(self.head()):
            return self.tail().filter(predicate).prepend(self.head())
        else:
            return self.tail().filter(predicate)

    def map(self, mapper):
        return self.tail().map(mapper).prepend(mapper(self.head()))


class PersistentListTest(unittest.TestCase):
    def setUp(self):
        self.empty = PersistentList()

    def testCreateList(self):
        self.assertEqual('', repr(self.empty))

    def testPrependList(self):
        nonempty = self.empty.prepend(1).prepend(2).prepend(3)

        self.assertEqual('3, 2, 1', repr(nonempty))

    def testHeadOfEmptyList(self):
        self.assertEqual(None, self.empty.head())

    def testHeadOfNonemptyList(self):
        nonempty = self.empty.prepend(1).prepend(2).prepend(3)

        self.assertEqual(3, nonempty.head())

    def testTailOfEmptyList(self):
        self.assertEqual(self.empty, self.empty.tail())

    def testTailOfNonemptyList(self):
        nonempty = self.empty.prepend(1).prepend(2).prepend(3)

        self.assertEqual(self.empty.prepend(1).prepend(2), nonempty.tail())

    def testConcatenationOfTwoEmptyLists(self):
        self.assertEqual(self.empty, self.empty + self.empty)

    def testConcatenationOfEmptyAndNonemptyLists(self):
        nonempty = self.empty.prepend(1).prepend(2).prepend(3)

        self.assertEqual(nonempty, nonempty + self.empty)
        self.assertEqual(nonempty, self.empty + nonempty)

    def testConcatenationOfTwoNonemptyLists(self):
        nonempty = self.empty.prepend(1).prepend(2).prepend(3)
        the_other_nonempty = self.empty.prepend(4).prepend(5).prepend(6)

        self.assertEqual('6, 5, 4, 3, 2, 1', repr(the_other_nonempty + nonempty))

    def testFilteredEmptyList(self):
        self.assertEqual(self.empty, self.empty.filter(lambda e: e > 1))

    def testFilterNonemptyList(self):
        nonempty = self.empty.prepend(1).prepend(2).prepend(3)

        self.assertEqual('3, 1', repr(nonempty.filter(lambda e: e != 2)))

    def testMapEmptyList(self):
        self.assertEqual(self.empty, self.empty.map(lambda e: e * 2))

    def testMapNonemptyList(self):
        nonempty = self.empty.prepend(1).prepend(2).prepend(3)

        self.assertEqual(self.empty.prepend(1).prepend(4).prepend(9), nonempty.map(lambda e: e ** 2))
