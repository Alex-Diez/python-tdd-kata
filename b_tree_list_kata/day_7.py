import unittest

PAGE_SIZE = 16


class BtreeList(object):
    def __init__(self):
        self._root = Page(True)

    def __iadd__(self, item):
        right = self._root.add_item(item)
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
        self._size = 0
        self._items = []
        self._preallocate_items()
        self._external = external

    def _preallocate_items(self):
        for _ in range(PAGE_SIZE):
            self._items.append(None)

    def is_full(self):
        return self._size == PAGE_SIZE

    def add_item(self, item):
        if self._external:
            self._add_entry(Entry(item))
            if self.is_full():
                return self.split()
        else:
            page = self._next_page(item).add_item(item)
            if page is not self._next_page(item):
                left, right = self.add_page(page)
                if right is not None:
                    return right
                else:
                    return left
        return self

    def _add_entry(self, entry):
        self._items[self._size] = entry
        self._size += 1

    def _index_of_next_page(self, item):
        for i in range(self._size):
            if self._items[i].key() > item:
                return i - 1
        return self._size - 1

    def _next_page(self, item):
        index = self._index_of_next_page(item)
        return self._items[index].next()

    def __contains__(self, item):
        if self._external:
            return any(map(lambda e: e.as_key(item), self._items[:self._size]))
        else:
            return item in self._next_page(item)

    def split(self):
        half = self._size // 2
        page = Page(self._external)
        for index in range(half, self._size):
            if self._external:
                page.add_item(self._items[index].key())
            else:
                page.add_page(self._items[index].next())
            self._items[index] = None
        self._size = half
        return page

    def add_page(self, page):
        self._add_entry(Entry(page._items[0].key(), page))
        if self.is_full():
            return self, self.split()
        else:
            return self, None


class Entry(object):
    def __init__(self, key, next=None):
        self._key = key
        self._next = next

    def as_key(self, item):
        return self._key == item

    def key(self):
        return self._key

    def next(self):
        return self._next


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

    def testListContainsMoreThanPage(self):
        for i in range(PAGE_SIZE + 1):
            self.list += i

        for i in range(PAGE_SIZE + 1):
            self.assertTrue(i in self.list)

    def testListContainsMoreThanOneLevel(self):
        for i in range(PAGE_SIZE ** 2 + 1):
            self.list += i

        for i in range(PAGE_SIZE ** 2 + 1):
            self.assertTrue(i in self.list)

    def testListContainsHugeNumberOfItems(self):
        for i in range(PAGE_SIZE ** 4 + 1):
            self.list += i

        for i in range(PAGE_SIZE ** 4 + 1):
            self.assertTrue(i in self.list)
