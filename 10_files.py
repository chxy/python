# Reading a file:
# 1. Open the file
# 2. Read its contents
# 3. Close the file

# 1. Open the file named 'regents.csv' in the current directory and keep the
with open('regents.csv') as f:
    # Another block here, this time indicating where the file is opened and closed.
    for line in f.readlines():
        print line
    # Close is implicit at the end of the block

# This is the preferred idiom for ensuring the file is handled properly.
# We'll see other, older idioms later.
