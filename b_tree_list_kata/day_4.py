import unittest

PAGE_SIZE = 16


class BtreeList(object):
    def __init__(self):
        self._root = Page(True)

    def __iadd__(self, item):
        right = self._root.add_key(item)
        if right is not self._root:
            left = self._root
            self._root = Page(False)
            self._root.add_page(left)
            self._root.add_page(right)
        return self

    def __contains__(self, item):
        return item in self._root


class Page(object):
    def __init__(self, external):
        self._items = []
        self._preallocate_items()
        self._external = external
        self._size = 0

    def _preallocate_items(self):
        for _ in range(PAGE_SIZE):
            self._items.append(None)

    def __contains__(self, item):
        if self._external:
            return item in [e.key() for e in self._items[:self._size]]
        else:
            index = self._size - 1
            for i in range(self._size):
                if self._items[i].key() > item:
                    index = i - 1
                    break
            return item in self._items[index]

    def add_key(self, item):
        if self._external:
            self._add_entry(Entry(item))
            if self.is_full():
                return self.split()
        else:
            index = self._size - 1
            for i in range(self._size):
                if self._items[i].key() > item:
                    index = i - 1
                    break
            page = self._items[index]._next.add_key(item)
            if page is not self._items[index]._next:
                left, right = self.add_page(page)
                if right is not None:
                    return right
                else:
                    return left
        return self

    def add_page(self, page):
        self._add_entry(Entry(page.first_key(), page))
        if self.is_full():
            return self, self.split()
        else:
            return self, None

    def is_full(self):
        return self._size == PAGE_SIZE

    def split(self):
        half = PAGE_SIZE // 2
        page = Page(self._external)
        for i in range(half, self._size):
            if self._external:
                page.add_key(self._items[i].key())
            else:
                page.add_page(self._items[i]._next)
            self._items[i] = None
        self._size = half
        return page

    def first_key(self):
        return self._items[0].key()

    def _add_entry(self, entry):
        self._items[self._size] = entry
        self._size += 1

    def __repr__(self):
        return '[' + ', '.join(map(repr, self._items)) + ']'


class Entry(object):
    def __init__(self, key, next=None):
        self._key = key
        self._next = next

    def key(self):
        return self._key

    def __repr__(self):
        return repr(self._key)

    def __contains__(self, item):
        if self._next is None:
            return self._key == item
        else:
            return item in self._next


class BtreeListTest(unittest.TestCase):
    def setUp(self):
        self.list = BtreeList()

    def testListContainsManyAddedValues(self):
        self.list += 1
        self.list += 2
        self.list += 3

        self.assertTrue(1 in self.list)
        self.assertTrue(2 in self.list)
        self.assertTrue(3 in self.list)

    def testListContainsMoreThanPage_addedValues(self):
        for i in range(PAGE_SIZE + 1):
            self.list += i

        for i in range(PAGE_SIZE + 1):
            self.assertTrue(i in self.list)

    def testListContainsMoreThanOneLevelOfAddedValues(self):
        for i in range(PAGE_SIZE ** 2 + 1):
            self.list += i

        for i in range(PAGE_SIZE ** 2 + 1):
            self.assertTrue(i in self.list)

    def testListContainsHugeAmountOfAddedValues(self):
        for i in range(PAGE_SIZE ** 4 + 1):
            self.list += i

        for i in range(PAGE_SIZE ** 4 + 1):
            self.assertTrue(i in self.list)
