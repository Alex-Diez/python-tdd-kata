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
        self._items = []
        for i in range(PAGE_SIZE):
            self._items.append(None)
        self._size = 0
        self._external = external

    def _is_full(self):
        return self._size == PAGE_SIZE

    def add_item(self, item):
        if self._external:
            self._add_entry(Entry(item))
            if self._is_full():
                return self.split()
        else:
            index = self._index_for(item)
            page = self[index].page.add_item(item)
            if page is not self[index].page:
                right = self.add_page(page)
                if right is not self:
                    return right
        return self

    def _index_for(self, item):
        for i in range(self._size):
            if self[i].key > item:
                return i - 1
        return self._size - 1

    def add_page(self, page):
        self._add_entry(Entry(page[0].key, page))
        if self._is_full():
            return self.split()
        else:
            return self

    def _add_entry(self, entry):
        self._items[self._size] = entry
        self._size += 1

    def __contains__(self, item):
        if self._external:
            return any(map(lambda e: e.key == item, self._items[:self._size]))
        else:
            index = self._index_for(item)
            return item in self[index].page

    def split(self):
        half = self._size // 2
        page = Page(self._external)
        for i in range(half, self._size):
            if self._external:
                page.add_item(self[i].key)
            else:
                page.add_page(self[i].page)
            self._items[i] = None
        self._size = half
        return page

    def __getitem__(self, index):
        return self._items[index]


class Entry(object):
    def __init__(self, key, page=None):
        self.key = key
        self.page = page


class BtreeListTest(unittest.TestCase):
    def setUp(self):
        self.list = BtreeList()

    def testListContainsAddedValues(self):
        self.list += 1
        self.list += 2
        self.list += 3

        self.assertTrue(1 in self.list)
        self.assertTrue(2 in self.list)
        self.assertTrue(3 in self.list)

    def testListContainsMoreThanOnePage(self):
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
