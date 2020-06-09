# Problem

# This problem was asked by Microsoft.

# Given a number in the form of a list of digits, return all possible
# permutations.

# For example, given
# [1,2,3]
# return
# [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].

# Solution

def _permutations(items, start=0, perms=[]):
    if start == len(items):
        perms.append(items.copy())
        return

    for i in range(start, len(items)):
        items[start], items[i] = items[i], items[start]
        _permutations(items, start+1, perms)
        items[start], items[i] = items[i], items[start]


def all_permutations(items):
    perms = []
    _permutations(items, 0, perms)
    return perms


print(all_permutations([1, 2, 3]))