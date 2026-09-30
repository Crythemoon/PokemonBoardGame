import Map

class MapFactory:
    @staticmethod
    def create_map(map_size):
        return Map.create_map(None, map_size)