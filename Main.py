'''
Rosibel Useda
Assignment: A* pathfinder
Due: April 12th, 2024
Instructor: Darren Reid
'''

from AStar import AStarPathfinder


h = 1.0
start_x = int(input("Please enter initial row value: "))
start_y = int(input("Please enter initial column value: "))
goal_x = int(input("Please enter goal row value: "))
goal_y = int(input("Please enter goal column value: "))
pathfinder = AStarPathfinder('map.txt', h)
pathfinder.print_map()

path = pathfinder.find_path(start_x, start_y, goal_x, goal_y)
if len(path)> 0:
    print("Path: (row, column): ")
    print(path)

else:
    print("No path found. ")

#map[row][column]