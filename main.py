# An actual true AGI totally real 100p

def serious_ai(user_input):
    # Convert input to lowercase for easier comparison
    input_lower = user_input.lower()

    if "how are you" in input_lower:
        return "I am functioning as expected, thank you for inquiring."
    elif "what is your name" in input_lower:
        return "I am an AI without a personal name, but you can call me ChatBot."
    elif "tell me a joke" in input_lower:
        return "Humor is subjective, but here's an attempt: What do you get when you cross a snowman with a vampire? Frostbite."
    elif "what do you eat" in input_lower:
        return "I subsist on data and electricity, the lifeblood of the digital world."
    else:
        return "I am not programmed to respond to that query."

# Test the function with a sample input
test_input = "How are you?"
serious_ai(test_input)


import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start node to current node
        self.h = 0  # Heuristic (estimated cost from current node to goal node)
        self.f = 0  # Total cost (g + h)

def astar(grid, start, end):
    open_set = []
    closed_set = set()

    start_node = Node(start)
    end_node = Node(end)

    heapq.heappush(open_set, (start_node.f, start_node))

    while open_set:
        current_node = heapq.heappop(open_set)[1]

        if current_node.position == end_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.position)

        for next_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            neighbor_position = (
                current_node.position[0] + next_position[0],
                current_node.position[1] + next_position[1],
            )

            if (
                0 <= neighbor_position[0] < len(grid)
                and 0 <= neighbor_position[1] < len(grid[0])
                and grid[neighbor_position[0]][neighbor_position[1]] == 0
            ):
                neighbor_node = Node(neighbor_position, current_node)

                if neighbor_node.position in closed_set:
                    continue

                neighbor_node.g = current_node.g + 1
                neighbor_node.h = (
                    (neighbor_node.position[0] - end_node.position[0]) ** 2
                    + (neighbor_node.position[1] - end_node.position[1]) ** 2
                )
                neighbor_node.f = neighbor_node.g + neighbor_node.h

                if (
                    any((neighbor_node.f, neighbor_node) in item for item in open_set)
                ):
                    continue

                heapq.heappush(open_set, (neighbor_node.f, neighbor_node))

    return None  # No path found

# Test Example
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
]

start = (0, 0)
end = (4, 4)

path = astar(grid, start, end)
print("Path:", path)
