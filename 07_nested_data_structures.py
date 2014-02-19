# Lists, tuples, dicts, and other data structures can themselves contain other data structures

list_of_dicts = [{'year': 1}, {'year': 2}] # Two different dicts, so they can use the same key
print 'List of dicts:', list_of_dicts

list_of_lists = [['a', 'b'], ['a', 'a']]
print 'List of lists:', list_of_lists

dict_of_lists = {'letters1': ['a', 'b'], 'letters2': ['a', 'b'], 'haveletters': True}
print 'Dict of lists:', dict_of_lists

# Common idiom for creating a dict of lists: use setdefault with an empty list to create key: [] if necessary, then append to it
dict_of_lists_to_fill = {}
dict_of_lists_to_fill.setdefault('names', []).append('Minor')
dict_of_lists_to_fill.setdefault('names', []).append('Gordon')
dict_of_lists_to_fill.setdefault('locations', []).append('Iowa')
print 'Dict of lists to fill:', dict_of_lists_to_fill
