def find_nearest_city(current_city, visited, distances):
    nearest_city = None
    min_distance = float('inf')
    for city, distance in enumerate(distances[current_city]):
        if city not in visited and distance < min_distance:
            min_distance = distance
            nearest_city = city
    return nearest_city

def tsp_greedy(distances):
    num_cities = len(distances)
    visited = set()
    route = []
    total_distance = 0

    # Start at the first city
    current_city = 0
    visited.add(current_city)
    route.append(current_city)

    # Find the rest of the route
    while len(visited) < num_cities:
        next_city = find_nearest_city(current_city, visited, distances)
        if next_city is not None:
            visited.add(next_city)
            route.append(next_city)
            total_distance += distances[current_city][next_city]
            current_city = next_city
    
    # Return to the starting city
    total_distance += distances[current_city][0]
    route.append(0)

    return route, total_distance

# Example Usage
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

route, total_distance = tsp_greedy(distances)
print("Route:", route)
print("Total Distance:", total_distance)

