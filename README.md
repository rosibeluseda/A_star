# A_star
This Python class implements A* pathfinding logic. It reads the map from the local disk and navigates using up, down, left, and right directions. The class supports dynamic adjustment of floating-point variables to assign different values to the heuristic weight, allowing for flexible and customizable pathfinding behavior. This implementation provides an efficient and adaptable solution for various pathfinding needs in grid-based maps.
The A* algorithm is a popular pathfinding and graph traversal algorithm. It is widely used in game development and robotics for its efficiency and accuracy. The algorithm works by maintaining a priority queue of nodes to be evaluated, prioritizing nodes with the lowest estimated cost to reach the goal.

<p align="center">
     <img src="https://github.com/rosibeluseda/A_star/assets/145386489/6232c902-a1dc-4464-a2ad-9af9b8f9185a" alt="Astar">
</p>

# Project Structure
* AStar.py: This file contains the implementation of the A* algorithm, which is responsible for finding the optimal path from a start node to a goal node.
* Main.py: The main script to run the A* pathfinding algorithm. It initializes the map, sets the start and goal positions, and executes the pathfinding.
* Map.py: This file handles the creation and management of the map grid, including loading the map from a file and displaying the grid.
* Node.py: Defines the Node class, which represents each cell in the grid. It includes properties such as position, cost, and parent node.
* map.txt: A text file representing the grid map. Each number corresponds to a type of terrain with different movement costs.

# Example Map
```csharp
1 4 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
2 3 1 3 3 3 3 3 3 1 2 3 3 3 3 3 3 3 3 1
3 6 2 3 4 1 2 2 2 1 3 2 2 3 4 1 2 2 2 1
1 2 2 2 2 2 2 3 4 1 1 2 2 2 2 2 2 3 4 1
1 3 4 3 2 3 2 4 4 1 1 3 4 3 2 3 2 4 4 1
3 3 3 3 3 2 3 3 1 1 3 3 3 3 3 2 3 3 2 1
1 1 1 6 5 5 5 5 1 6 1 1 1 6 5 5 5 5 2 1
9 1 1 6 1 1 1 1 1 1 1 1 1 6 1 1 1 1 3 1
9 1 1 6 1 1 1 1 1 1 1 1 1 6 1 1 1 1 2 1
1 1 1 6 1 1 1 1 1 1 1 1 1 6 1 1 1 1 2 1
1 1 1 6 1 1 1 1 9 9 1 1 1 6 1 1 1 1 2 1
1 1 1 6 1 1 1 1 9 9 1 1 1 6 1 1 1 1 2 1
1 1 1 6 1 1 1 1 1 1 1 1 1 6 1 1 1 1 2 1
1 1 1 6 1 1 1 1 1 1 1 1 1 6 1 1 1 1 2 1
1 1 1 6 1 1 1 1 1 1 1 1 1 6 1 1 1 1 2 1
1 1 1 6 1 1 1 1 1 1 1 1 1 6 1 1 1 1 2 1
1 1 1 6 1 1 1 1 1 1 1 1 1 6 1 1 1 1 1 1
1 1 1 6 1 1 1 1 1 1 1 1 1 6 1 1 1 1 1 6
1 1 1 6 1 1 1 1 1 1 1 1 1 6 1 1 1 1 1 1
1 1 1 6 1 1 1 1 9 9 1 1 1 6 1 1 1 1 2 1
```

### Key Classes and Functions

#### AStar Class (AStar.py)
- **__init__**: Initializes the algorithm with the start and goal nodes.
- **heuristic**: Calculates the heuristic cost (Manhattan distance) from the current node to the goal.
- **find_path**: Executes the A* algorithm to find the optimal path.

#### Node Class (Node.py)
- **__init__**: Initializes a node with its position, cost, and parent.
- **__lt__**: Less than operator for comparing nodes based on their cost.

#### Map Class (Map.py)
- **__init__**: Initializes the map with a given width and height.
- **load_map**: Loads the map from a text file.
- **get_neighbors**: Retrieves the neighboring nodes of a given node.

### Output

When you run the `Main.py` script, the A* algorithm will process the map and print the optimal path from the start node to the goal node, if a path exists. The output will include the sequence of steps taken to reach the goal.





