# Problem

# This problem was asked by Airbnb.

# We're given a hashmap associating each courseId key with a list of courseIds
# values, which represents that the prerequisites of courseId are courseIds.
# Return a sorted ordering of courses such that we can finish all courses.

# Return null if there is no such ordering.

# For example, given:
# {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}
# should return:
# ['CSC100', 'CSC200', 'CSCS300']


# Solution

def TopologicalSort(adjacency_list):
    sort = []
    not_visited = set(adjacency_list.keys())

    while len(not_visited) != 0:
        node = not_visited.pop()
        stack = [node]

        while len(stack) != 0:
            node = stack[-1]

            visited_all_children = True
            for child in adjacency_list[node]:

                if child == stack[0]:
                    return None

                if child in not_visited:
                    not_visited.remove(child)
                    stack.append(child)
                    visited_all_children = False

            if visited_all_children:
                sort.append(stack.pop())

    return sort


print(TopologicalSort({
    'CSC300': ['CSC100', 'CSC200'],
    'CSC200': ['CSC100'],
    'CSC100': []}))
