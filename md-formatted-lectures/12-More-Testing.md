

## TESTING... BUT MORE
## 1

## AUTOMATED TEST ENVIRONMENT
▪Automated Testing in Python with pytest, tox, and GitHub Actions (youtube.com) (27m)
## 2

## UNIT TESTING
▪Used to test individual components of a program
## 3

## PROJECT STRUCTURE
## ▪project/
## ▪src/
## ▪modulename/
## ▪file1.py
▪get_file_info(str) → dict
## ▪tests/
## ▪test_file1.py
## ▪test_get_file_info()
## 4

## EXPECTED BEHAVIOUR
print(get_file_info('/users/paul/info.txt'))
## {
## "path": "/users/paul",
## "name": "info",
## "ext": "txt"
## }
## 5

## PROJECT/SRC/MODULENAME/FILE1.PY
def get_file_info(filepath: str) -> dict:
## '''/users/paul/info.txt -> {
## "path": "/users/paul",
## "name": "info",
## "ext": "txt"
## }'''
file_info = {
## "path": '/'.join(filepath.split('/')[:-1]),
"name": filepath.split('/')[-1].split('.')[0],
"ext": filepath.split('.')[-1]
## }
return file_info
## 6

## EDGE CASE TESTS
('/users/paul/.gitignore', {"path": "/users/paul", "name": ".gitignore", "ext": None})
## ('/users/file.name.txt', {"path": "/users", "name": "file.name", "ext": "txt"})
## ('/users/paul/info', {"path": "/users/paul", "name": "info", "ext": None})
## ('/log.txt', {"path": "/", "name": "log", "ext": "txt"})
## ('/.archive.tar.gz', {"path": "/", "name": ".archive", "ext": "tar.gz"})
## 7

## TESTING OUR FUNCTION
▪With and without parametrization
▪Run using pytest
## 8

## PROJECT/TESTS/TEST_FILE1.PY
from modulename.file1 import get_file_info
def test_get_file_info():  # Without parametrization
## # Test 1
filepath = '/users/paul/info.txt’
expected = {
## "path": "/users/paul",
## "name": "info",
## "ext": "txt"
## }
result = get_file_info(filepath)
assert result == expected
... # More tests on this setup
## # Test 2
filepath2 = ...
## 9

## PROJECT/TESTS/TEST_FILE1.PY
import pytest
from modulename.file1 import get_file_info
@pytest.mark.parametrize('filepath, expected', [
('/users/paul/info.txt', {"path": "/users/paul", "name": "info", "ext": "txt"}),
('/users/john/file.pdf', {"path": "/users/john", "name": "file", "ext": "pdf"}),
## ('/users/john/file', {"path": "/users/john", "name": "file", "ext": ""}),
## ...
## ])
def test_get_file_info(filepath, expected):  # With parametrization
assert get_file_info(filepath) == expected
... # More tests on this setup
## 10