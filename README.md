[![CircleCI](https://circleci.com/gh/ki4070ma/unittest.svg?style=svg)](https://circleci.com/gh/ki4070ma/unittest)

# Javascript
## Installation
```
$ npm install --save-dev jest
```

## Run test via command line
* config file has settings

```
(specific file)
$ jest test_file.js --notify --config=config.json

(all test files)
$ jest --notifiy --config=config.json
```

# Python
## Run test via command line - unittest

```
(specific file)
$ python test_file.py

(specific class)
$ python -m unittest test_file.test-class

(all files, test files needs to be test_*.py)
$ python -m unittest discover
```

## Run test via command line - pytest

```
$ python3 -m pytest
============================================================================================ test session starts =============================================================================================
platform linux -- Python 3.5.2, pytest-4.0.1, py-1.7.0, pluggy-0.8.0
plugins: cov-2.6.0
collected 28 items

test_calculator.py .....................                                                                                                                                                               [ 75%]
test_samples.py .......                                                                                                                                                                                [100%]

========================================================================================= 28 passed in 0.05 seconds ==========================================================================================
```

## Run test on PyCharm
1. Jump between method and testcase
   * Ctrl + Shift + T on each method
1. Run each test case
   * Ctrl + Shift + F10 on test method
