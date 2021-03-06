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
        self._entries = []
        self._preallocate_entries()
        self._size = 0
        self._external = external

    def _preallocate_entries(self):
        for _ in range(PAGE_SIZE):
            self._entries.append(None)

    def __getitem__(self, index):
        return self._entries[index]

    def __setitem__(self, index, item):
        self._entries[index] = item

    def add_item(self, item):
        if self._external:
            self._add_entry(Entry(item))
            if self._size == PAGE_SIZE:
                return self.split()
        else:
            index = self._page_index_for_item(item)
            page = self[index]._page.add_item(item)
            if page is not self[index]._page:
                left, right = self.add_page(page)
                if right is not None:
                    return right
                else:
                    return left
        return self

    def add_page(self, page):
        self._add_entry(Entry(page[0]._key, page))
        if self._size == PAGE_SIZE:
            return self, self.split()
        else:
            return self, None

    def _add_entry(self, entry):
        self[self._size] = entry
        self._size += 1

    def __contains__(self, item):
        if self._external:
            return any(self[:self._size])
        else:
            index = self._page_index_for_item(item)
            return item in self[index]

    def _page_index_for_item(self, item):
        for index in range(self._size):
            if self[index] > item:
                return index - 1
        return self._size - 1

    def split(self):
        half = self._size // 2
        page = Page(self._external)
        for index in range(half, self._size):
            if self._external:
                page.add_item(self[index]._key)
            else:
                page.add_page(self[index]._page)
            self[index] = None
        self._size = half
        return page


class Entry(object):
    def __init__(self, key, page=None):
        self._key = key
        self._page = page

    def __gt__(self, item):
        return self._key > item

    def __eq__(self, item):
        return self._key == item

    def __contains__(self, item):
        return item in self._page


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

    def testListContainsValuesMoreThanPage(self):
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
