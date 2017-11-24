import unittest


class EmptyList(object):
    def __repr__(self):
        return ''

    def append(self, item):
        return PersistentList(item, self)

    def __add__(self, other):
        return other

    def map(self, mapper):
        return self


_EMPTY_LIST = EmptyList()


class PersistentList(object):
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def __repr__(self):
        tail = repr(self.tail)
        if tail is '':
            return repr(self.head)
        else:
            return repr(self.head) + ', ' + tail

    def append(self, item):
        return PersistentList(item, self)

    def __add__(self, other):
        return (self.tail + other).append(self.head)

    def map(self, mapper):
        return self.tail.map(mapper).append(mapper(self.head))


class PersistentListTest(unittest.TestCase):
    def setUp(self):
        self.empty_list = EmptyList()

    def testAppendItems(self):
        self.assertEqual('3, 2, 1', repr(self.empty_list.append(1).append(2).append(3)))

    def testConcatTwoEmptyList(self):
        self.assertEqual('', repr(self.empty_list + self.empty_list))

    def testConcatEmptyWithNonemptyList(self):
        nonempty_list = self.empty_list.append(1).append(2).append(3)
        self.assertEqual('3, 2, 1', repr(nonempty_list + self.empty_list))
        self.assertEqual('3, 2, 1', repr(self.empty_list + nonempty_list))

    def testConcatenationOfTwoNonemptyLists(self):
        nonempty_list = self.empty_list.append(1).append(2).append(3)
        the_other_nonempty_list = self.empty_list.append(4).append(5).append(6)

        self.assertEqual('6, 5, 4, 3, 2, 1', repr(the_other_nonempty_list + nonempty_list))

    def testEmptyList_mapToEmptyList(self):
        self.assertEqual(self.empty_list, self.empty_list.map(lambda e: repr(e)))

    def testMapNonemptyList(self):
        nonempty_list = self.empty_list.append(1).append(2).append(3)

        self.assertEqual('6, 4, 2', repr(nonempty_list.map(lambda e: e * 2)))