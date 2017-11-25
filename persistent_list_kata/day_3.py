import unittest


class PersistentList(object):
    def __repr__(self):
        return ''

    def prepend(self, item):
        return _NodeList(item, self)

    def head(self):
        pass

    def tail(self):
        return self

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.head() is self.head() and self.tail() is self.tail()
        else:
            return False

    def __add__(self, other):
        return other

    def map(self, mapper):
        return self


class _NodeList(PersistentList):
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

    def __add__(self, other):
        return (self.tail() + other).prepend(self.head())

    def map(self, mapper):
        return self.tail().map(mapper).prepend(mapper(self.head()))


class PersistentListTest(unittest.TestCase):
    def setUp(self):
        self.empty = PersistentList()

    def testCreateList(self):
        self.assertEqual('', repr(self.empty))

    def testPrependList(self):
        self.assertEqual('3, 2, 1', repr(self.empty.prepend(1).prepend(2).prepend(3)))

    def testHeadOfEmptyList(self):
        self.assertEqual(None, self.empty.head())

    def testHeadOfNonemptyList(self):
        nonempty = self.empty.prepend(1).prepend(2)
        self.assertEqual(2, nonempty.head())

    def testTailOfEmptyList(self):
        self.assertEqual(PersistentList(), self.empty.tail())

    def testTailOfNonemptyList(self):
        nonempty = self.empty.prepend(1).prepend(2).prepend(3)

        self.assertEqual('2, 1', repr(nonempty.tail()))

    def testConcatenationOfTwoEmptyLists(self):
        self.assertEqual('', repr(self.empty + self.empty))

    def testConcatenationOfEmptyAndNonemptyLists(self):
        nonempty = self.empty.prepend(1).prepend(2).prepend(3)

        self.assertEqual('3, 2, 1', repr(self.empty + nonempty))
        self.assertEqual('3, 2, 1', repr(nonempty + self.empty))

    def testConcatenationOfTwoNonemptyLists(self):
        nonempty = self.empty.prepend(1).prepend(2).prepend(3)
        the_other_nonempty = self.empty.prepend(4).prepend(5).prepend(6)

        self.assertEqual('3, 2, 1, 6, 5, 4', repr(nonempty + the_other_nonempty))

    def testMapOverEmptyList(self):
        self.assertEqual(self.empty, self.empty.map(lambda e: e * 2))

    def testMapOverNonemptyList(self):
        nonempty = self.empty.prepend(1).prepend(2).prepend(3)
        self.assertEqual('6, 4, 2', repr(nonempty.map(lambda e: e * 2)))
