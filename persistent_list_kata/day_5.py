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

    def __eq__(self, other):
        return isinstance(other, self.__class__) \
               and other.head() is None

    def __add__(self, other):
        return other


class _Node(PersistentList):
    def __init__(self, head, tail):
        self._head = head
        self._tail = tail

    def __repr__(self):
        tail_repr = repr(self._tail)
        if tail_repr is '':
            return repr(self._head)
        else:
            return repr(self._head) + ', ' + repr(self._tail)

    def head(self):
        return self._head

    def tail(self):
        return self._tail

    def __eq__(self, other):
        return isinstance(other, self.__class__) \
               and self.head() is other.head() \
               and self.tail() == other.tail()

    def __add__(self, other):
        return (self.tail() + other).prepend(self.head())

    def __iter__(self):
        return _PersistentListIter(self)


class _PersistentListIter(object):
    def __init__(self, persistent_list):
        self._persistent_list = persistent_list

    def __iter__(self):
        return self

    def next(self):
        item = self._persistent_list.head()
        if item is not None:
            return item
        else:
            raise StopIteration()


class zrange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return zrange_iter(self.n)


class zrange_iter:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        # Iterators are iterables too.
        # Adding this functions to make them so.
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


class PersistentListTest(unittest.TestCase):
    def setUp(self):
        self.empty = PersistentList()

    def testCreateEmptyList(self):
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

    def testConcatenationOfEmpty_andNonemptyLists(self):
        nonempty = self.empty.prepend(1).prepend(2).prepend(3)

        self.assertEqual(nonempty, self.empty + nonempty)
        self.assertEqual(nonempty, nonempty + self.empty)

    def testConcatenationOfTwoNonemptyLists(self):
        nonempty = self.empty.prepend(1).prepend(2).prepend(3)
        the_other_nonempty = self.empty.prepend(4).prepend(5).prepend(6)

        self.assertEqual('3, 2, 1, 6, 5, 4', repr(nonempty + the_other_nonempty))
