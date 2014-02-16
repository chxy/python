# Lists, tuples, dicts, and other data structures can themselves contain other data structures

list_of_dicts = [{'key1': 1}, {'key1': 2}] # Two different dicts, so they can use the same key
print 'List of dicts:', list_of_dicts

list_of_lists = [['a', 'b'], ['a', 'a']]
print 'List of lists:', list_of_lists

dict_of_lists = {'key1': ['a', 'b'], 'key2': ['a', 'b'], 'key3': True}
print 'Dict of lists:', dict_of_lists

# Common idiom for creating a dict of lists: use setdefault with an empty list to create key: [] if necessary, then append to it
dict_of_lists_to_fill = {}
dict_of_lists_to_fill.setdefault('key1', []).append(1)
dict_of_lists_to_fill.setdefault('key1', []).append(2)
dict_of_lists_to_fill.setdefault('key2', []).append(5)
print 'Dict of lists to fill:', dict_of_lists_to_fill
