#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from add import add, times

class TestAdd(unittest.TestCase):

  def test_add(self):
    actual = add(1, 2)
    expected = 3
    self.assertEqual(expected, actual)

class TestTimes(unittest.TestCase):

  def test_times(self):
    actual = times(2, 3)
    expected = 6
    self.assertEqual(expected, actual)


if __name__ == '__main__':
  unittest.main()
