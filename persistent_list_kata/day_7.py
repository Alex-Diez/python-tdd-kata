import unittest


class PersistentList(object):
    def __repr__(self):
        return ''

    def prepend(self, item):
        return ListNode(item, self)

    def head(self):
        pass

    def tail(self):
        return self

    def __eq__(self, other):
        return isinstance(other, self.__class__) \
               and self.head() == other.head()

    def __add__(self, other):
        return other

    def map(self, mapper):
        return self


class ListNode(PersistentList):
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

    def map(self, mapper):
        return self.tail().map(mapper).prepend(mapper(self.head()))


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
        nonempty = self.empty.prepend(1).prepend(2).prepend(3)

        self.assertEqual(3, nonempty.head())

    def testTailOfEmptyList(self):
        self.assertEqual(PersistentList(), self.empty.tail())

    def testTailOfNonemptyList(self):
        nonempty = self.empty.prepend(1).prepend(2).prepend(3)

        self.assertEqual(self.empty.prepend(1).prepend(2), nonempty.tail())

    def testEquality(self):
        nonempty = self.empty.prepend(1).prepend(2).prepend(3)
        the_other = self.empty.prepend(0).prepend(0).prepend(3)

        self.assertNotEqual(nonempty, the_other)

    def testConcatenationOfTwoEmptyLists(self):
        self.assertEqual(self.empty, self.empty + self.empty)

    def testConcatenationOfEmptyAndNonemptyLists(self):
        nonempty = self.empty.prepend(1).prepend(2).prepend(3)

        self.assertEqual(nonempty, self.empty + nonempty)
        self.assertEqual(nonempty, nonempty + self.empty)

    def testConcatenationOfTwoNonemptyLists(self):
        nonempty = self.empty.prepend(1).prepend(2).prepend(3)
        the_other = self.empty.prepend(4).prepend(5).prepend(6)

        self.assertEqual('6, 5, 4, 3, 2, 1', repr(the_other + nonempty))

    def testMapEmptyList(self):
        self.assertEqual(self.empty, self.empty.map(lambda e: e * 2))

    def testMapNonemptyList(self):
        nonempty = self.empty.prepend(1).prepend(2).prepend(3)

        self.assertEqual(self.empty.prepend(1).prepend(4).prepend(9), nonempty.map(lambda e: e ** 2))
