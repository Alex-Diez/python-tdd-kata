import unittest

PAGE_SIZE = 16


class BtreeSet(object):
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
        self._items = []
        self._preallocate_items()
        self._size = 0
        self._external = external

    def _preallocate_items(self):
        for _ in range(PAGE_SIZE):
            self._items.append(None)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, item):
        self._items[index] = item

    def is_full(self):
        return self._size == PAGE_SIZE

    def add_item(self, item):
        if self._external:
            self._add_entry(Entry(item))
            if self.is_full():
                return self.split()
        else:
            index = self._page_index_for(item)
            page = self[index].page().add_item(item)
            if page is not self[index].page():
                left, right = self.add_page(page)
                if right is not None:
                    return right
                else:
                    return left
        return self

    def _page_index_for(self, item):
        for index in range(self._size):
            if self[index].key() > item:
                return index - 1
        return self._size - 1

    def add_page(self, page):
        self._add_entry(Entry(page[0].key(), page))
        if self.is_full():
            return self, self.split()
        else:
            return self, None

    def _add_entry(self, entry):
        self[self._size] = entry
        self._size += 1

    def __contains__(self, item):
        if self._external:
            return any(map(lambda e: e.as_key(item), self[:self._size]))
        else:
            index = self._page_index_for(item)
            return item in self[index].page()

    def split(self):
        half = self._size // 2
        page = Page(self._external)
        for index in range(half, self._size):
            if self._external:
                page.add_item(self[index].key())
            else:
                page.add_page(self[index].page())
            self[index] = None
        self._size = half
        return page


class Entry(object):
    def __init__(self, key, page=None):
        self._key = key
        self._page = page

    def as_key(self, item):
        return self._key == item

    def key(self):
        return self._key

    def page(self):
        return self._page


class BtreeSetTest(unittest.TestCase):
    def setUp(self):
        self.set = BtreeSet()

    def testSetContainsManyAddedValues(self):
        self.set += 1
        self.set += 2
        self.set += 3

        self.assertTrue(1 in self.set)
        self.assertTrue(2 in self.set)
        self.assertTrue(3 in self.set)

    def testSetContainsMoreThanOnePage(self):
        for i in range(PAGE_SIZE + 1):
            self.set += i

        for i in range(PAGE_SIZE + 1):
            self.assertTrue(i in self.set)

    def testSetContainsMoreThanOneLevel(self):
        for i in range(PAGE_SIZE ** 2 + 1):
            self.set += i

        for i in range(PAGE_SIZE ** 2 + 1):
            self.assertTrue(i in self.set)

    def testSetContainsHugeNumberOfItems(self):
        for i in range(PAGE_SIZE ** 4 + 1):
            self.set += i

        for i in range(PAGE_SIZE ** 4 + 1):
            self.assertTrue(i in self.set)
