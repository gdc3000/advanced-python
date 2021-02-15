
from weakref import WeakKeyDictionary

class Positive:
	
	def __init__(self):
		self._instance_data = WeakKeyDictionary()
	
	#Descriptor protocol section
	def __get__(self, instance, owner):
		return self._instance_data[instance]

	def __set__(self, instance, value):
		if value <= 0:
			raise ValueError("Value {} is not positive".format(value))
		self._instance_data[instance] = value

	def __delete__(self, instance):
		raise AttributeError("Cannot delete attribute")


class Planet:

    def __init__(self,
                name,
                radius_metres,
                mass_kg,
                orbital_period_secs,
                surface_temp_k):
        self.name = name
        self.radius_metres = radius_metres
        self.mass_kg = mass_kg
        self.orbital_period_secs = orbital_period_secs
        self.surface_temp_k = surface_temp_k

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Cannot set empty Planet.name")
        self._name = value

    radius_metres = Positive()
    mass_kg = Positive()
    orbital_period_secs = Positive()
    surface_temp_k = Positive()
