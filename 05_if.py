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

# And one for lists
a_list = ['x', 'y']
if 'x' in a_list:
    print 'x is in the list'