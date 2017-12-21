import unittest


class BtreeList(object):
    def __init__(self):
        self._root = Page(True)

    def add(self, item):
        self._root.add(item)
        if self._root.is_full():
            left = self._root
            right = self._root.split()
            self._root = Page(False)
            self._root.put(left)
            self._root.put(right)

    def __contains__(self, item):
        return item in self._root


class Page(object):
    def __init__(self, external):
        self._external = external
        self._items = []
        self._size = 0

    def __contains__(self, item):
        if self._external:
            return item in map(lambda e: e._key, self._items)
        else:
            index = -1
            for i in range(self._size):
                if self._items[i]._key > item:
                    index = i - 1
                    break
            if index == -1:
                return item in self._items[self._size - 1]._next
            else:
                return item in self._items[index]._next

    def add(self, item):
        if self._external:
            entry = Entry(item, None)
            self._items.append(entry)
            self._size += 1
        else:
            index = -1
            for i in range(self._size):
                if self._items[i]._key > item:
                    index = i - 1
                    break
            if index == -1:
                self._items[self._size - 1]._next.add(item)
            else:
                self._items[index]._next.add(item)

    def put(self, page):
        entry = Entry(page._items[0]._key, page)
        self._items.append(entry)
        self._size += 1

    def is_full(self):
        return self._size == 16

    def split(self):
        page = Page(True)
        for i in range(16 // 2):
            page.add(self._items[i + 16 // 2]._key)
        self._size = 16 // 2
        return page

    def __repr__(self):
        return '[' + ', '.join(map(repr, self._items[0:self._size])) + ']'


class Entry(object):
    def __init__(self, key, next):
        self._key = key
        self._next = next

    def __repr__(self):
        return repr(self._key)


class BtreeListTest(unittest.TestCase):
    def setUp(self):
        self.list = BtreeList()

    def testListContainsAddedValue(self):
        self.list.add(1)

        self.assertTrue(1 in self.list)

    def testListDoesNotContainNotAddedValue(self):
        self.assertFalse(1 in self.list)

    def testListContainsAllItem_moreThanOnePage(self):
        for i in range(16 + 1):
            self.list.add(i)

        for i in range(16 + 1):
            self.assertTrue(i in self.list)
