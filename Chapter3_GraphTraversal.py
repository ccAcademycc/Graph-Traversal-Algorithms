import random


# Executes the BFS algorithm on a given graph `adj_list` with starting node `r`.
def bfs(adj_list, r):
    num_nodes = len(adj_list)
    parent = [-1] * num_nodes
    level = [-1] * num_nodes
    visit = [0] * num_nodes

    level[r] = 0
    visit[r] = 1
    Q = [r]

    while Q:
        u = Q.pop(0)
        unvisited_adj = [v for v in adj_list[u] if visit[v] == 0]

        for v in unvisited_adj:
            parent[v] = u
            level[v] = level[u] + 1
            visit[v] = 1
            Q.append(v)

    return parent, level, visit


# Removes duplicate elements from the stack,
# preserving only the most recently added element if it occurs more than once in the stack.
def remove_duplicates(stack):
    seen = set()
    result_stack = []
    while stack:
        current = stack.pop()
        if current not in seen:
            seen.add(current)
            result_stack.append(current)
    result_stack.reverse()
    return result_stack


# Executes the DFS algorithm on a given graph `adj_list` with starting node `r`.
# Uses the "remove_duplicates" function.
def dfs(adj_list, r):
    num_nodes = len(adj_list)
    parent = [-1] * num_nodes
    level = [-1] * num_nodes
    visit = [0] * num_nodes

    level[r] = 0
    S = [r]

    while S:
        u = S.pop()

        visit[u] = 1
        unvisited_adj = [v for v in adj_list[u] if visit[v] == 0]
        random.shuffle(unvisited_adj)
        for v in unvisited_adj:
            parent[v] = u
            level[v] = level[u] + 1
            S.append(v)
            S = remove_duplicates(S)

    return parent, level, visit


# Executes the DFS algorithm on a given graph `adj_list` with starting node `r`.
# Typical implementation of DFS, with an if condition that checks whether a popped node is visited.
def dfs_basic_version(adj_list, r):
    num_nodes = len(adj_list)
    parent = [-1] * num_nodes
    level = [-1] * num_nodes
    visit = [0] * num_nodes

    level[r] = 0
    S = [r]

    while S:
        u = S.pop()
        if visit[u] == 0:
            visit[u] = 1
            unvisited_adj = [v for v in adj_list[u] if visit[v] == 0]
            random.shuffle(unvisited_adj)
            for v in unvisited_adj:
                parent[v] = u
                level[v] = level[u] + 1
                S.append(v)

    return parent, level, visit


# Graph - Example (5x5 Kings Graph, see Chapter 2)
adj_list_example = {
    0: [1, 5, 6],
    1: [0, 2, 5, 6, 7],
    2: [1, 3, 6, 7, 8],
    3: [2, 4, 7, 8, 9],
    4: [3, 8, 9],
    5: [0, 1, 6, 10, 11],
    6: [0, 1, 2, 5, 7, 10, 11, 12],
    7: [1, 2, 3, 6, 8, 11, 12, 13],
    8: [2, 3, 4, 7, 9, 12, 13, 14],
    9: [3, 4, 8, 13, 14],
    10: [5, 6, 11, 15, 16],
    11: [5, 6, 7, 10, 12, 15, 16, 17],
    12: [6, 7, 8, 11, 13, 16, 17, 18],
    13: [7, 8, 9, 12, 14, 17, 18, 19],
    14: [8, 9, 13, 18, 19],
    15: [10, 11, 16, 20, 21],
    16: [10, 11, 12, 15, 17, 20, 21, 22],
    17: [11, 12, 13, 16, 18, 21, 22, 23],
    18: [12, 13, 14, 17, 19, 22, 23, 24],
    19: [13, 14, 18, 23, 24],
    20: [15, 16, 21],
    21: [15, 16, 17, 20, 22],
    22: [16, 17, 18, 21, 23],
    23: [17, 18, 19, 22, 24],
    24: [18, 19, 23]
}

# Application of BFS on the above graph
parent_example1, level_example1, visit_example1 = bfs(adj_list_example, 12)

# Print the results
print('----------------------------------')
print("BFS - Parent:", parent_example1)
print("BFS - Level:", level_example1)
print("BFS - Visit:", visit_example1)
print(' ')
print("BFS - Visualization of the levels:")
for i in range(len(level_example1), -1, -5):
    row = level_example1[i:i + 5]
    formatted_row = ' '.join(f'{num:2}' for num in row)
    print(formatted_row)
print(' ')

# Application of DFS on the above graph
parent_example2, level_example2, visit_example2 = dfs(adj_list_example, 23)

# Print the results
print('----------------------------------')
print("DFS - Parent:", parent_example2)
print("DFS - Level:", level_example2)
print("DFS - Visit:", visit_example2)
print(' ')
print("DFS - Visualization of the levels:")
for i in range(len(level_example2), -1, -5):
    row = level_example2[i:i + 5]
    formatted_row = ' '.join(f'{num:2}' for num in row)
    print(formatted_row)
print('----------------------------------')
print(' ')

# # Application of DFS on the above graph
# parent_example3, level_example3, visit_example3 = dfs_basic_version(adj_list_example, 23)
# # Print the results
# print("DFS_BasicVersion - Parent:", parent_example3)
# print("DFS_BasicVersion - Level:", level_example3)
# print("DFS_BasicVersion - Visit:", visit_example3)
# print(' ')
# print("DFS_BasicVersion - Visualization of the levels:")
# for i in range(len(level_example3),-1, -5):
#     row = level_example3[i:i+5]
#     formatted_row = ' '.join(f'{num:2}' for num in row)
#     print(formatted_row)
# print('----------------------------------')