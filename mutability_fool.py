"""
In this Bite you are presented with a function that copies the given items data structure.

There is a problem though, the tests fail. Can you fix it?

This can be done in a one liner. If you know which module to use it will be easy, if not you will learn something new today.

Regardless we want you to think about Python's mutability. Have fun!
"""
import copy
items = [{'id': 1, 'name': 'laptop', 'value': 1000},
         {'id': 2, 'name': 'chair', 'value': 300},
         {'id': 3, 'name': 'book', 'value': 20}]


def duplicate_items(items):
    return copy.deepcopy(items)

print(duplicate_items(items))
print('_____')
items_copy = duplicate_items(items)
print(id(items))
print(id(items_copy))
items_copy[0]['name'] = 'macbook'
items_copy[1]['id'] = 4
items_copy[2]['value'] = 30

print(duplicate_items(items_copy))
print(id(duplicate_items(items_copy)))
print('....')
print(duplicate_items(items))
print(id(duplicate_items(items)))