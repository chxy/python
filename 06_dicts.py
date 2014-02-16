# Dict operations


a_dict = {'key1': 'value1', 'key2': 2}


# Accessing a dict
print 'Complete dict:', a_dict
print 'Length of the dict:', len(a_dict)
print 'Value for key key1:', a_dict['key1']
print 'Value for key key2:', a_dict['key2']
print 'Keys:', a_dict.keys() # List; no guaranteed order
print 'Values:', a_dict.values() # List; no guaranteed ord
print 'Keys and value items:', a_dict.items() # List of tuples; no guaranteed order
print


# Modifying a dict
print 'dict before modification:', a_dict
del a_dict['key1'] # Delete the mapping from 'key1': 'value1'
print 'dict after deleting key1:', a_dict
a_dict['key3'] = True # Add a new mapping
print 'dict with key3 added:', a_dict


# Useful idiom
a_dict.setdefault('key4', 4) # Set key4 to 4 iff it does not contain a key4 already