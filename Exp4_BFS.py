def bfs(graph, start_vertex):
    visited = []  # List to keep track of visited nodes.
    queue = []  # Initialize a queue
    # Add the start vertex to the queue and visited list
    queue.append(start_vertex)
    visited.append(start_vertex)

    while queue:
        # Remove the first element from the queue and print it
        vertex = queue.pop(0)
        print(vertex, end=" ")
        # Get all adjacent vertices of the dequeued vertex
        # If an adjacent vertex has not been visited, then mark it visited and enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
"""
  TEST CASE 2
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
  OUTPUT:  5 3 7 2 4 8
"""
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_vertex = input("Enter the start vertex: ").upper()
if start_vertex in graph:
    print("BFS traversal starting from vertex", start_vertex, ":")
    bfs(graph, start_vertex)
else:
    print("Start vertex not in graph.")
