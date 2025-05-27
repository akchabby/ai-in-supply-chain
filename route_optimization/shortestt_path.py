import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_dist, current_node = heapq.heappop(queue)
        for neighbor, weight in graph[current_node]:
            dist = current_dist + weight
            if dist < distances[neighbor]:
                distances[neighbor] = dist
                heapq.heappush(queue, (dist, neighbor))
    return distances

# Example graph
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('C', 1), ('D', 7)],
    'C': [('A', 4), ('B', 1), ('D', 3)],
    'D': [('B', 7), ('C', 3)]
}

if __name__ == "__main__":
    start = 'A'
    distances = dijkstra(graph, start)
    for dest, dist in distances.items():
        print(f"Shortest distance from {start} to {dest}: {dist}")
