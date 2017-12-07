import unittest

PAGE_SIZE = 16


class BtreeSet(object):
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

    def contains(self, item):
        return item in self._root


class Page(object):
    def __init__(self, external):
        self._children = []
        for _ in range(PAGE_SIZE):
            self._children.append(None)
        self._size = 0
        self._external = external

    def add(self, item):
        if self._external:
            entry = Entry(item, None)
            self._children[self._size] = entry
            self._size += 1
        else:
            index = -1
            for i in range(self._size):
                if self._children[i]._key > item:
                    index = i
            if index == -1:
                self._children[self._size - 1]._lower_page.add(item)
            else:
                self._children[index]._lower_page.add(item)

    def is_full(self):
        return self._size == PAGE_SIZE

    def __contains__(self, item):
        if self._external:
            for i in range(self._size):
                if self._children[i]._key == item:
                    return True
            return False
        else:
            index = -1
            for i in range(self._size):
                if self._children[i]._key > item:
                    index = i - 1
                    break
            if index == -1:
                return item in self._children[self._size - 1]._lower_page
            else:
                return item in self._children[index]._lower_page

    def split(self):
        page = Page(True)
        for i in range(PAGE_SIZE // 2):
            page.add(self._children[i + PAGE_SIZE // 2]._key)
        self._size = PAGE_SIZE // 2
        return page

    def put(self, page):
        self._children[self._size] = Entry(page._children[0]._key, page)
        self._size += 1

    def __repr__(self):
        return ', '.join(map(repr, self._children[0:self._size]))


class Entry(object):
    def __init__(self, key, lower_page):
        self._key = key
        self._lower_page = lower_page

    def __repr__(self):
        return repr(self._key)


class BtreeSetTest(unittest.TestCase):
    def setUp(self):
        self.set = BtreeSet()

    def testSetContainsAddValue(self):
        self.set.add(1)

        self.assertTrue(self.set.contains(1))

    def testSetDoesNotContainNotAddedValue(self):
        self.set.add(1)

        self.assertFalse(self.set.contains(0))

    def testSetContainsManyAddedValues(self):
        self.set.add(1)
        self.set.add(2)
        self.set.add(3)

        self.assertTrue(self.set.contains(1))
        self.assertTrue(self.set.contains(2))
        self.assertTrue(self.set.contains(3))

    def testSetContainsMoreThanOnePageAddedValues(self):
        for i in range(PAGE_SIZE + 1):
            self.set.add(i)

        for i in range(PAGE_SIZE + 1):
            self.assertTrue(self.set.contains(i))
