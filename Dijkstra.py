import heapq

# Define the game map as a grid
# 0: Walkable path, 1: Obstacle
# Example of a grid with weights

I = 1 #Numero Inicial Sin valor
x = float('inf')

game_map = [
    [I, 1, 1, x, 1],
    [x, x, 2, x, 1],
    [1, 4, 2, 9, 1],
    [1, x, x, x, 1],
    [1, 3, 1, 1, 0],  # 0: Heavily weighted tile
]


# Directions for movement: up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Dijkstra's algorithm implementation
def dijkstra(grid, start):
    rows, cols = len(grid), len(grid[0])
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = 0
    priority_queue = [(0, start)]  # (distance, (row, col))

    while priority_queue:
        current_dist, (x, y) = heapq.heappop(priority_queue)

        if grid[x][y] == 0:  # Found the treasure
            return current_dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != float('inf'):
                new_dist = current_dist + grid[nx][ny]
                if new_dist < distances[nx][ny]:
                    distances[nx][ny] = new_dist
                    heapq.heappush(priority_queue, (new_dist, (nx, ny)))

    return float('inf')  # Treasure not reachable


# Starting point (row, col)
start_point = (0, 0)

# Run the game logic
shortest_path = dijkstra(game_map, start_point)

# Output the result
if shortest_path < float('inf'):
    print(f"The shortest path to the treasure is {shortest_path} steps.")
else:
    print("The treasure is not reachable.")
