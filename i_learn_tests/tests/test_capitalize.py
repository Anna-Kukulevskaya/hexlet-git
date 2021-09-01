from capitalize import capitalize

assert capitalize('hello') == 'Hello'
assert capitalize('') == ''

print('Все тесты пройдены!')

#PYTHONPATH=package-name python3 tests/test_capitalize.py