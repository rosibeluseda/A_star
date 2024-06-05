from Node import Node
from Map import MapLoader
import heapq

class AStarPathfinder:
    def __init__(self, map_file, heuristic_weight):
        self.heuristic_weight = heuristic_weight
        map_loader = MapLoader(map_file)
        self.map = map_loader.load_map()

    def goal_distance_estimate(self, x, y, goal_x, goal_y):
        return self.heuristic_weight * (abs(x - goal_x) + abs(y - goal_y))

    def print_map(self):
        for row in self.map:
            print(' '.join(str(cell) for cell in row))

    def find_path(self, start_x, start_y, goal_x, goal_y):
        open_list = []
        open_set = set()
        closed_set = set()
        node_map = {}  #store the nodes coordinates

        start_h = self.goal_distance_estimate(start_x, start_y, goal_x, goal_y)
        start_node = Node(None, start_x, start_y, 0, start_h)
        heapq.heappush(open_list, (start_node.f, start_node))
        open_set.add((start_x, start_y))
        node_map[(start_x, start_y)] = start_node

        while open_list:
            current_f, current_node = heapq.heappop(open_list)
            open_set.remove((current_node.x, current_node.y))
            closed_set.add((current_node.x, current_node.y))

            if (current_node.x, current_node.y) == (goal_x, goal_y):
                return self.construct_path(current_node)

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]    #left / right / up / down
            for direction in directions:
                x = current_node.x + direction[1] #row
                y = current_node.y + direction[0] #column

                if 0 <= x < len(self.map[0]) and 0 <= y < len(self.map):
                    new_g = current_node.g + self.map[x][y]

                    if (x, y) in closed_set:
                        continue

                    if (x, y) in open_set:
                        existing_node = node_map[(x, y)]
                        if new_g < existing_node.g:
                            existing_node.g = new_g
                            existing_node.h = self.goal_distance_estimate(x, y, goal_x, goal_y)
                            existing_node.f = existing_node.g + existing_node.h
                            existing_node.parent = current_node
                            heapq.heapify(open_list)
                    else:
                        h = self.goal_distance_estimate(x, y, goal_x, goal_y)
                        new_node = Node(current_node, x, y, new_g, h)
                        heapq.heappush(open_list, (new_node.f, new_node))
                        open_set.add((x, y))
                        node_map[(x, y)] = new_node

        return []

    def construct_path(self, goal_node):
        path = []
        current = goal_node
        while current:
            path.append((current.x, current.y))
            current = current.parent
        return path[::-1]  #reverse the path to print from start to goal
