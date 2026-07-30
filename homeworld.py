class Homeworld:
    def __init__(self, world_name, rotation_period, orbital_period, diameter, climate, gravity, terrain, surface_water, population):
        self._world_name = world_name
        self._rotation_period = rotation_period
        self._orbital_period = orbital_period
        self._diameter = diameter
        self._climate = climate
        self._gravity = gravity
        self._terrain = terrain
        self._surface_water = surface_water
        self._population = population

    @property
    def world_name(self):
        return self._world_name
    @property
    def rotation_period(self):
        return self._rotation_period
    @property
    def orbital_period(self):
        return self._orbital_period
    @property
    def diameter(self):
        return self._diameter
    @property
    def climate(self):
        return self._climate
    @property
    def gravity(self):
        return self._gravity
    @property
    def terrain(self):
        return self._terrain
    @property
    def surface_water(self):
        return self._surface_water
    @property
    def population(self):
        return self._population

    @name.setter
    def name(self, name):
        self._name = name
    @rotation_period.setter
    def rotation_period(self, rotation_period):
        self._rotation_period = rotation_period
    @orbital_period.setter
    def orbital_period(self, orbital_period):
        self._orbital_period = orbital_period
    @diameter.setter
    def diameter(self, diameter):
        self._diameter = diameter
    @climate.setter
    def climate(self, climate):
        self._climate = climate
    @gravity.setter
    def gravity(self, gravity):
        self._gravity = gravity
    @terrain.setter
    def terrain(self, terrain):
        self._terrain = terrain
    @surface_water.setter
    def surface_water(self, surface_water):
        self._surface_water = surface_water
    @population.setter
    def population(self, population):
        self._population = population

