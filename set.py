#!python

from hashtable import HashTable


class Set(object):

    def __init__(self, elements=None):
        """Initialize this set and add elements if specified."""
        self.data = HashTable()

        # add elements if specified
        if elements is not None:
            for element in elements:
                self.add(element)

    def __str__(self):
        """Return a formatted string representation of this set."""
        elements = ['{!r}'.format(key) for key in self.data.keys()]
        return '{' + ', '.join(elements) + '}'

    def size(self):
        """Return the size of the set.
        Runtime: O(1) Space: O(1)"""
        return self.data.size

    def contains(self, element):
        """Return True if the element is contained in the set, or return
        False otherwise.
        Runtime: O(1) Space: O(1)"""
        return self.data.contains(element)

    def add(self, element):
        """Add an element to the set.
        Runtime: O(1) Space: O(1)"""
        self.data.set(element, None)

    def remove(self, element):
        """Remove an item from the set.
        Runtime: O(1) Space: O(-1)"""
        self.data.delete(element)  # raise a KeyError if element does not exist

    def union(self, other_set):
        """Return a new set containing all elements from the first and second set.
        Runtime: O(n + k) Space: O(n + k)"""
        return Set(self.data.keys() + other_set.data.keys())

    def intersection(self, other_set):
        """Return a new set containing elements that are located in both the first
        and second set.
        Runtime: O(n) Space: O(n)"""
        return Set([key for key in self.data.keys() if other_set.data.contains(key)])

    def difference(self, other_set):
        """Return a new set containing elements that are in the first set but not in
        the second set.
        Runtime: O(n) Space: O(n)"""
        return Set([key for key in self.data.keys() if not other_set.data.contains(key)])

    def is_subset(self, other_set):
        """Return True if the second set is a subset of the first set, otherwise
        return False.
        Runtime: O(n) Space: O(1)"""
        return other_set.difference(self).data.size == 0


def test_set():
    set1 = Set(["one", "two", "three"])
    set2 = Set(["one", "two", "nine", "ten"])
    print("Set 1: " + str(set1))
    print("Size of set 1: {}\n".format(set1.size()))
    print("Set 2: " + str(set2))
    print("Size of set 2: {}\n".format(set2.size()))
    print("Union: {}\n".format(set1.union(set2)))
    print("Intersection: {}\n".format(set1.intersection(set2)))
    print("Difference: {}\n".format(set1.difference(set2)))
    print("Subset: {}\n".format(set1.is_subset(set2)))


if __name__ == '__main__':
    test_set()
