class MapLoader:
    def __init__(self, map_file):
        self.map_file = map_file

    def load_map(self):
        map_data = []
        with open(self.map_file, 'r') as file:
            lines = file.readlines()
            for line in lines[2:]:
                map_data.append([int(x) for x in line.split()])
        return map_data