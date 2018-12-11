#!/usr/bin/python
# -*- coding: utf-8 -*-

def add(a, b):
  return a + b

def times(a, b):
  return a * b

# 西暦が4で割り切れる年は閏年
# ただし、100で割り切れる年は閏年ではない
# ただし、400で割り切れる年は閏年
def check_uruu(year):
  if not isinstance(year, int):
    raise ValueError('{} is not int.'.format(year))
  if year < 0:
    raise ValueError('{} is minus.'.format(year))
  elif year % 400 == 0:
    return True
  elif year % 100 == 0:
    return False
  elif year % 4 == 0:
    return True
  else:
    return False


if __name__ == '__main__':
  print(add(1, 2))
