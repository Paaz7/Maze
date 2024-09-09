def find_path(maze, x, y, path):
    # Check if (x, y) is out of bounds or is a wall (1)
    if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]) or maze[x][y] == 1:
        return False

    # Check if we have reached the exit (bottom-right corner)
    if x == len(maze) - 1 and y == len(maze[0]) - 1:
        path.append((x, y))  # Add the exit point to the path
        return True

    # Mark the cell as part of the path by setting it to 1 (to avoid revisiting)
    maze[x][y] = 1

    # Explore the four possible directions (down, right, up, left)
    if find_path(maze, x + 1, y, path):  # Move down
        path.append((x, y))
        return True
    if find_path(maze, x, y + 1, path):  # Move right
        path.append((x, y))
        return True
    if find_path(maze, x - 1, y, path):  # Move up
        path.append((x, y))
        return True
    if find_path(maze, x, y - 1, path):  # Move left
        path.append((x, y))
        return True

    # Unmark this cell (backtrack) if no path is found
    maze[x][y] = 0
    return False

def solve_maze(maze):
    path = []
    if find_path(maze, 0, 0, path):
        return path[::-1]  # Return the path from start to exit
    else:
        return None  # No path found

# Example Maze (0 = path, 1 = wall)
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

# Solve the maze
result = solve_maze(maze)
if result:
    print("Path to exit:", result)
else:
    print("No path found")


