x = 1

if x > 0:
    # Note the indentation: that tells Python to execute the indented "block" of code if the condition is true
    print 'x is greater than 0'
print 'No longer in the block, so this will always be executed'

if x == 0:
    print 'x equals 0'
else:
    print 'x does not equal 0'

# Python will not let you write:
# if x = 0:
# == is comparison for equality
# = is assignment

if x == 0:
    print 'x equals 0'
elif x == 1:
    print 'x equals 1'
else:
    print 'x does not equal 1 or 0'

if True:
    print 'This will always execute'

y = x > 0
print type(x) # This will be?

# Comparison operators
print 'x > 0', x > 0
print 'x < 0', x < 0
print 'x >= 0', x >= 0 # Greater than or equals
print 'x <= 0', x <= 0 # Less than or equals
print 'x == 0', x == 0 # Equals
print 'x != 0', x != 0 # Not equals
print 'not (x == 0)', not (x == 0) # Negation

# Test if a list or tuple contains an element
a_list = ['x', 'y']
if 'x' in a_list:
    print 'x is in the list'


# Test if a dict contains a key
a_dict = {'key1': 'value1', 'key2': 'value2'}
if 'key1' in a_dict:
    print 'key1 is in the dict'
# Same as
if 'key1' in a_dict.keys():
    print 'key1 is in the dict'
# (The first form is more common and more efficient.)
if 'value1' in a_dict:
    print "This won't work"
if 'value1' in a_dict.values():
    print 'This will'


# Be careful with types
if '1' == 1:
    print "It looks true, but it isn't"
else:
    print "A string will never equal an integer -- one of the disadvantages of having types."
    # We'll see how to deal with this later.
