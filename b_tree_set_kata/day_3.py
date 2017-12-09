import unittest

PAGE_SIZE = 16


class BtreeSet(object):
    def __init__(self):
        self._root = Page(True)

    def __iadd__(self, item):
        right = self._root.add(item)
        if right is not self._root:
            left = self._root
            self._root = Page(False)
            self._root.put(left)
            self._root.put(right)
        return self

    def __contains__(self, item):
        return item in self._root


class Page(object):
    def __init__(self, external):
        self._items = []
        for _ in range(PAGE_SIZE):
            self._items.append(None)
        self._size = 0
        self._external = external

    def add(self, item):
        if self._external:
            entry = Entry(item)
            self._items[self._size] = entry
            self._size += 1
            if self.is_full():
                return self.split()
        else:
            index = self._size - 1
            for i in range(self._size):
                if self._items[i].key_greater_than(item):
                    index = i - 1
                    break
            page = self._items[index]._next.add(item)
            if page is not self._items[index]._next:
                left, right = self.put(page)
                if right is not None:
                    return right
                else:
                    return left
        return self

    def __contains__(self, item):
        if self._external:
            return item in map(lambda i: i.key(), self._items[:self._size])
        else:
            index = self._size - 1
            for i in range(self._size):
                if self._items[i].key_greater_than(item):
                    index = i - 1
                    break
            return item in self._items[index]._next

    def __repr__(self):
        return '[' + ', '.join(map(repr, self._items[:self._size])) + ']'

    def is_full(self):
        return self._size == PAGE_SIZE

    def split(self):
        half = self._size // 2
        page = Page(self._external)
        for i in range(half, self._size):
            if page._external:
                page.add(self._key_at(i))
            else:
                page.put(self._items[i]._next)
            self._items[i] = None
        self._size = half
        return page

    def put(self, page):
        entry = Entry(page._first_key(), page)
        self._items[self._size] = entry
        self._size += 1
        if self.is_full():
            return self, self.split()
        else:
            return self, None

    def _first_key(self):
        return self._key_at(0)

    def _key_at(self, index):
        return self._items[index].key()


class Entry(object):
    def __init__(self, key, next=None):
        self._key = key
        self._next = next

    def __repr__(self):
        return repr(self._key)

    def key_greater_than(self, item):
        return self._key > item

    def key(self):
        return self._key


class BtreeSetTest(unittest.TestCase):
    def setUp(self):
        self.set = BtreeSet()

    def testContainsAddedValue(self):
        self.set += 1

        self.assertTrue(1 in self.set)

    def testContainsManyAddedValues(self):
        self.set += 1
        self.set += 2
        self.set += 3

        self.assertTrue(1 in self.set)
        self.assertTrue(2 in self.set)
        self.assertTrue(3 in self.set)

    def testSetContainsAllAddedValuesMoreThanPage(self):
        for i in range(PAGE_SIZE + 1):
            self.set += i

        for i in range(PAGE_SIZE + 1):
            self.assertTrue(i in self.set)

    def testSetContainsAllAddedValues_moreThanOneLevelOfPages(self):
        for i in range(PAGE_SIZE * PAGE_SIZE + 1):
            self.set += i

        for i in range(PAGE_SIZE * PAGE_SIZE + 1):
            self.assertTrue(i in self.set)
