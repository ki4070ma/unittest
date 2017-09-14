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
## Run test via command line

```
(specific file)
$ python test_file.py

(specific class)
$ python -m unittest test_file.test-class

(all files, test files needs to be test_*.py)
$ python -m unittest discover
```
