"""
This class will handle all the environment that creatures interact inside of including:
Vegetation food sources, terrain, temperature, day/night cycles.
This information is all stored inside of a map file.
TO-DO (Later): Random map generator - this should only be started when we decide on a game engine.
"""

class environment:
    def __init__(self, seed="aaaaaa"):
        # Map constants
        self.seed = seed # For random generation
        self.averageTemperature = 20

        # Global variables
        self.temperature = 20 # Assumes temperature is uniform across the map
        self.time = 0 # Scale of 0-10000. 0:7500 = day; 7500:10000 = night; Subject to change
        self.night = False

    def tick(self):
        # This block handles the day-night cycle
        self.time += 1
        if self.time > 10000:
            self.time = 0
        self.updateTwilight()

        # Block to handle temperature change?
        self.updateTemperature

    def updateTwilight(self):
        if self.time >= 7500:
            self.night = True
        else:
            self.night = False

    def updateTemperature(self):
        if self.night: # Night temperature should drop to half the average.
            if self.temperature > self.averageTemperature/2:
                self.temperature += -1

