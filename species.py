class Species:

    def __init__(self, species_name, classification, designation, average_height, species_skin_color,species_hair_color, species_eye_color, average_lifespan, language ):
        self._species_name = species_name
        self._classification = classification
        self._designation = designation
        self._average_height = average_height
        self._species_skin_color = species_skin_color
        self._species_hair_color = species_hair_color
        self._species_eye_color = species_eye_color
        self._average_lifespan = average_lifespan
        self._language = language

    @property
    def species_name(self):
        return self._species_name
    @property
    def classification(self):
        return self._classification
    @property
    def designation(self):
        return self._designation
    @property
    def average_height(self):
        return self._average_height
    @property
    def species_skin_color(self):
        return self._species_skin_color
    @property
    def species_hair_color(self):
        return self._species_hair_color
    @property
    def species_eye_color(self):
        return self._species_eye_color
    @property
    def average_lifespan(self):
        return self._average_lifespan
    @property
    def language(self):
        return self._language

    @species_name.setter
    def species_name(self, value):
        self._species_name = value
    @classification.setter
    def classification(self, value):
        self._classification = value
    @designation.setter
    def designation(self, value):
        self._designation = value
    @average_height.setter
    def average_height(self, value):
        self._average_height = value
    @species_skin_color.setter
    def species_skin_color(self, value):
        self._species_skin_color = value
    @species_hair_color.setter
    def species_hair_color(self, value):
        self._species_hair_color = value
    @species_eye_color.setter
    def species_eye_color(self, value):
        self._species_eye_color = value
    @average_lifespan.setter
    def average_lifespan(self, value):
        self._average_lifespan = value
    @language.setter
    def language(self, value):
        self._language = value