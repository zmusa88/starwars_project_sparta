import homeworld
import film
import species

class Character(homeworld.Homeworld, film.Film, species.Species):

  def __init__(self, name, height, mass, hair_color, skin_color, eye_color, birth_year, gender, world_name, rotation_period, orbital_period, diameter, climate, gravity, terrain, surface_water, population, title, episode_id, opening_crawl, director, producer, release_date, species_name, classification, designation, average_height, species_skin_color,species_hair_color, species_eye_color, average_lifespan, language):
      self._name = name
      self._height = height
      self._mass = mass
      self._hair_color = hair_color
      self._skin_color = skin_color
      self._eye_color = eye_color
      self._birth_year = birth_year
      self._gender = gender

      super().__init__(world_name, rotation_period, orbital_period, diameter, climate, gravity, terrain, surface_water, population)
      super().__init__(title, episode_id, opening_crawl, director, producer, release_date)
      super().__init__(species_name, classification, designation, average_height, species_skin_color,species_hair_color, species_eye_color, average_lifespan, language)


  @property
  def name(self):
      return self._name
  @property
  def height(self):
      return self._height
  @property
  def mass(self):
      return self._mass
  @property
  def hair_color(self):
      return self._hair_color
  @property
  def skin_color(self):
      return self._skin_color
  @property
  def eye_color(self):
      return self._eye_color
  @property
  def birth_year(self):
      return self._birth_year
  @property
  def gender(self):
      return self._gender

  @name.setter
  def name(self, value):
      self._name = value
  @height.setter
  def height(self, value):
      self._height = value
  @mass.setter
  def mass(self, value):
      self._mass = value
  @hair_color.setter
  def hair_color(self, value):
      self._hair_color = value
  @skin_color.setter
  def skin_color(self, value):
      self._skin_color = value
  @eye_color.setter
  def eye_color(self, value):
      self._eye_color = value
  @birth_year.setter
  def birth_year(self, value):
      self._birth_year = value
  @gender.setter
  def gender(self, value):
      self._gender = value