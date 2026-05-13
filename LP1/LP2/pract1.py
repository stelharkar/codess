""" Implement depth first search algorithm and Breadth First Search algorithm, Use an undirected
graph and develop a recursive algorithm for searching all the vertices of a graph or tree data
structure. """


# BFS and DFS using Graph

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = set()

# Depth First Search
def dfs(node):

    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbour in graph[node]:
            dfs(neighbour)

# Breadth First Search
def bfs(start):

    visited = []
    queue = []

    visited.append(start)
    queue.append(start)

    while queue:

        node = queue.pop(0)
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("DFS Traversal:")
dfs('A')

print("\nBFS Traversal:")
bfs('A')