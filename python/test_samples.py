#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from unittest import TestCase

from samples import add, times, check_uruu


class TestSamples(TestCase):
  def test_add(self):
    actual = add(1, 2)
    expected = 3
    self.assertEqual(expected, actual)

  def test_times(self):
    actual = times(2, 3)
    expected = 6
    self.assertEqual(expected, actual)

  def test_check_uruu_4_non100_non400(self):
    self.assertTrue(check_uruu(2004))

  def test_check_uruu_4_100_non400(self):
    self.assertFalse(check_uruu(2100))

  def test_check_uruu_4_100_400(self):
    self.assertTrue(check_uruu(2000))

  def test_check_uruu_minus(self):
    try:
      check_uruu(-100)
      self.fail()
    except ValueError:
      return
    self.fail()

  def test_check_uruu_non_int(self):
    try:
      check_uruu('a')
      self.fail()
    except ValueError:
      return
    self.fail()

if __name__ == '__main__':
  unittest.main()
