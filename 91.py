### Problem

# Good morning! Here's your coding interview problem for today.

# This problem was asked by Dropbox.

# What does the below code snippet print out? How can we fix the anonymous
# functions to behave as we'd expect?

# functions = []
# for i in range(10):
#     functions.append(lambda : i)

# for f in functions:
#     print(f())

### Solution
# The problem is that `i` is a local variable to the loop and changes at each
# iteration of the loop. To have a fixed value variable we need a local variable
# to the anonymous function. Something like below:

functions = []
for i in range(10):
    functions.append((lambda j: (lambda: j))(i))

for f in functions:
    print(f())
