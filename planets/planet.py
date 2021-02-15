
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

    
    def _get_name(self):
        return self._name

    def _set_name(self, value):
        if not value:
            raise ValueError("Cannot set empty Planet.name")
        self._name = value

    name = property(fget=_get_name, fset=_set_name)

    def _get_radius_metres(self):
        return self._radius_metres

    def _set_radius_metres(self, value):
        if value <= 0:
            raise ValueError("radius_metres value {} is not positive.".format(value))
        self._radius_metres = value

    radius_metres = property(fget=_get_radius_metres, fset=_set_radius_metres)
    
    def _get_mass_kg(self):
        return self._mass_kg
    
    def _set_mass_kg(self, value):
        if value <= 0:
            raise ValueError("mass_kg value {} is not positive.".format(value))
        self._mass_kg = value
    
    mass_kg = property(fget=_get_mass_kg, fset=_set_mass_kg)
    
    def _get_orbital_period_secs(self):
        return self._orbital_period_secs
    
    def _set_orbital_period_secs(self, value):
        if value <= 0:
            raise ValueError("orbital_period_secs value {} is not positive.".format(value))
        self._orbital_period_secs = value
    
    orbital_period_secs = property(fget=_get_orbital_period_secs, fset=_set_orbital_period_secs)

    def _get_surface_temp_k(self):
        return self._surface_temp_k

    def _set_surface_temp_k(self, value):
        if value <= 0:
            raise ValueError("surface_temp_k value {} is not positive.".format(value))
        self._surface_temp_k = value
    
    surface_temp_k = property(fget=_get_surface_temp_k, fset=_set_surface_temp_k)
