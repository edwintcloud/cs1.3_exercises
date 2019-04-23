#!python

from set import Set
import unittest


class SetTest(unittest.TestCase):

    def test_init_empty(self):
        s = Set()
        assert s.size() == 0

    def test_init_with_elements(self):
        s = Set(['one', 'two', 'three'])
        assert s.size() == 3
        assert s.contains('one') is True
        assert s.contains('two') is True
        assert s.contains('three') is True

    def test_size(self):
        s = Set()
        assert s.size() == 0
        s.add('one')
        assert s.size() == 1
        s.add('two')
        assert s.size() == 2
        s.remove('two')
        assert s.size() == 1

    def test_contains(self):
        s = Set(['waffle', 'potato', 'three'])
        assert s.contains('three') is True
        assert s.contains('potato') is True
        assert s.contains('waffle') is True
        s.add('chicken')
        assert s.contains('chicken') is True
        s.add('chicken')
        assert s.contains('chicken') is True
        s.remove('waffle')
        assert s.contains('waffle') is False
        assert s.contains('four') is False

    def test_add(self):
        s = Set()
        assert s.size() == 0
        s.add('hello')
        assert s.contains('hello') is True
        assert s.size() == 1

    def test_remove(self):
        s = Set(['one', 'two', 'three'])
        assert s.size() == 3
        s.remove('one')
        assert s.contains('one') is False
        assert s.size() == 2
        s.remove('two')
        assert s.contains('two') is False
        assert s.size() == 1
        s.remove('three')
        assert s.contains('three') is False
        assert s.size() == 0
        with self.assertRaises(KeyError):
            s.remove('four')

    def test_union(self):
        s1 = Set(['one', 'two', 'three'])
        s2 = Set(['three', 'four', 'five'])
        s1_union = s1.union(s2)
        assert s1_union.size() == 5
        assert s1_union.contains('one') is True
        assert s1_union.contains('two') is True
        assert s1_union.contains('three') is True
        assert s1_union.contains('four') is True
        assert s1_union.contains('five') is True
        s2_union = s2.union(s1)
        assert s2_union.size() == 5
        assert s2_union.contains('one') is True
        assert s2_union.contains('two') is True
        assert s2_union.contains('three') is True
        assert s2_union.contains('four') is True
        assert s2_union.contains('five') is True

    def test_intersection(self):
        s1 = Set(['one', 'two', 'three', 'four'])
        s2 = Set(['three', 'four', 'five'])
        s1_intersection = s1.intersection(s2)
        assert s1_intersection.size() == 2
        assert s1_intersection.contains('one') is False
        assert s1_intersection.contains('three') is True
        assert s1_intersection.contains('four') is True
        s2_intersection = s2.intersection(s1)
        assert s2_intersection.size() == 2
        assert s2_intersection.contains('one') is False
        assert s2_intersection.contains('three') is True
        assert s2_intersection.contains('four') is True

    def test_difference(self):
        s1 = Set(['one', 'two', 'three'])
        s2 = Set(['three', 'four', 'five'])
        s1_difference = s1.difference(s2)
        assert s1_difference.size() == 2
        assert s1_difference.contains('one') is True
        assert s1_difference.contains('two') is True
        assert s1_difference.contains('three') is False
        assert s1_difference.contains('four') is False
        s2_difference = s2.difference(s1)
        assert s2_difference.size() == 2
        assert s2_difference.contains('one') is False
        assert s2_difference.contains('two') is False
        assert s2_difference.contains('three') is False
        assert s2_difference.contains('four') is True
        assert s2_difference.contains('five') is True

    def test_is_subset(self):
        s1 = Set(['one', 'two', 'three', 'four'])
        s2 = Set(['two', 'four'])
        assert s1.is_subset(s2) is True
        assert s2.is_subset(s1) is False


if __name__ == '__main__':
    unittest.main()
