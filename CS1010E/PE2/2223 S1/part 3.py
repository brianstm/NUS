# Part 3


from collections import deque


def min_no_of_turns(L):
    if not L:  # if the tuple is empty, no turn is needed
        return 0
    # Convert the tuple to a list and create a dictionary to count each integer
    counts = {}
    for num in L:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    turns = 0  # Initialize the count of turns
    # Iterate through the sorted keys of the dictionary
    for num in sorted(counts.keys()):
        # While the count of the current number is not 0
        while counts[num] > 0:
            # Reduce the count of each consecutive number by 1 in each turn
            i = num
            while i in counts and counts[i] > 0:
                counts[i] -= 1
                i += 1
            turns += 1  # Increment the count of turns

    return turns


print(min_no_of_turns((1, 8, 3, 6, 5, 7, 2, 1)))
print(min_no_of_turns((1, 8, 3, 6, 5, 7, 2, 1, 4)))
tup3 = (6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15, 16, 6, 5, 16, 16)
print(min_no_of_turns(tup3))
print(min_no_of_turns((1, 8, 3, 6, 5, 7, 2, 1, 2, 9)))


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)
            queue.extend(graph[vertex] - visited)


visited = set()


def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


def selection_sort(input_list):
    sort = []
    while input_list:
        smallest = input_list[0]
        for element in input_list:
            if element < smallest:
                smallest = element
        input_list.remove(smallest)
        sort.append(smallest)
    return sort
