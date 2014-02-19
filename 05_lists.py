# List operations


a_list = ['a string', 1, True, 'x']


# Accessing a list
print 'Complete list:', a_list
print 'Length of the list:', len(a_list)
print 'Element 0:', a_list[0] # 0-based indices
print 'Elements [0, 2):', a_list[0:2] # A "slice" of a_list
print 'Last element:', a_list[len(a_list)-1] # The list has len(a_list) elements has the index of the last element is len(a_list)-1, because the indices are 0-based
print 'Last element:', a_list[-1] # Shorthand for the above
print


# Modifying a list
print 'List before modification:', a_list
del a_list[0] # Delete the first element (index 0)
print 'List after deleting the 0-th element:', a_list
a_list.append('y') # Add an element to the end of the list
print 'List with y appended to the end:', a_list
a_list.insert(1, 'another string') # Insert an element before the element at index 1
print 'List with "another string" inserted into it:', a_list
a_list.sort()
print 'Sorted list', a_list