def dfs(visited, graph, node): 
    if node not in visited:
        print(node, end=' ')
        visited.add(node)  # Mark node as visited
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)  # Visit neighbours
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()  # Set to keep track of visited nodes.
start_vertex = input("Enter the start vertex: ").upper()

if start_vertex in graph:
    print("DFS traversal starting from vertex", start_vertex, ":")
    dfs(visited, graph, start_vertex)
else:
    print("Start vertex not in graph.")
