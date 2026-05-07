from perlin_noise import PerlinNoise
import random
import MapTileObject

class MapGenerator:
    def __init__(self,WIDTH,HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SCALE = 5.0
        self.noise = PerlinNoise(octaves=1, seed=random.randint(0,100))
    
    #Generating a raw perlin map with no constraint
    def Generate_Default_PerlinMap(self):
        self.map = []
        
        raw_values = []
        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                v = self.noise([x/self.SCALE,y/self.SCALE])
                raw_values.append(v)
        
        min_v = min(raw_values)
        max_v = max(raw_values)
        index = 0

        for y in range(self.HEIGHT):
            row = []
            for x in range(self.WIDTH):
                value = raw_values[index]
                index += 1

                # normalize to 0 to 1
                norm = (value - min_v) / (max_v - min_v + 1e-9)
                
                if norm < 0.2:
                    tile = MapTileObject.Terrain.WATER
                elif norm < 0.5:
                    tile = MapTileObject.Terrain.DIRT
                elif norm < 0.7:
                    tile = MapTileObject.Terrain.BASE_MOUNTAIN
                elif norm < 0.8:
                    tile = MapTileObject.Terrain.MIDDLE_MOUTAIN
                else:
                    tile = MapTileObject.Terrain.TOP_MOUNTAIN
                
                row.append(tile)
            self.map.append(row)
    
    def Generate_Water_PerlinMap(self):
        self.map = []