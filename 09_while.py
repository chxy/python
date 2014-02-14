# What if we want to keep doing something depending on a condition?
# Loop ... while


print 'Loop'
x = 0
while x < 10: # Spoken "while x is less than 10"
    # Every pass through the loop -- executing this block -- is called an "iteration"
    print x
    x = x + 1
print 'Now x = ', x
print # Empty line


# Break
print 'Break before the loop completes'
x = 0 # Reset x
while x < 10:
    print x
    if x == 5:
        break # Out of the while loop
    x = x + 1
print 'Now x = ', x
print


# Same loop as the first, in "infinitive" form with a break
print "'Infinite' loop with break"
x = 0
while True:
    print x
    if x >= 10:
        break # Without this break we'd keep looping forever
    x = x + 1
print 'Now x = ', x
print


# Continue
print 'Loop with continue'
x = 0
while x < 10:
    print x
    if x == 5:
        x = x + 2
        continue # To 'while', skipping any statements after this
    x = x + 1
print 'Now x = ', x
print


print 'Some useful shorthand'
x = 0
while x < 10:
    print x
    x += 1 # Shorthand for x = x + 1
