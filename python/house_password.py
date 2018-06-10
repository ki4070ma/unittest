#!/usr/bin/python

def checkio(data):
  import re
  return len(data) >= 10 and bool(re.search(r'[a-z]', data)) and bool(re.search(r'[A-Z]', data)) and bool(re.search(r'[0-9]', data))


if __name__ == '__main__':
  # These "asserts" using only for self-checking and not necessary for auto-testing
  assert checkio('A1213pokl') == False, "1st example"
  assert checkio('bAse730onE4') == True, "2nd example"
  assert checkio('asasasasasasasaas') == False, "3rd example"
  assert checkio('QWERTYqwerty') == False, "4th example"
  assert checkio('123456123456') == False, "5th example"
  assert checkio('QwErTy911poqqqq') == True, "6th example"
  # assert checkio('QwErTy911poqqqq') == False, "7th example"
  print 'All test passed'
