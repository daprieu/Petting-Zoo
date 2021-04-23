# import the python datetime module to help us create a timestamp
from datetime import date

# But you should also take into consideration the fact that there are different types of animals at Critters and Croquettes. Specifically, there are critters in

# the petting area, such as donkeys, llamas, and goats
# the glass tank, like copperheads and rat snakes
# the pond, like mallards and goldfish
# With that in mind, make 5 critter types for each area. As you define each one, give it one of the following properties where most appropriate:

# self.swimming = True
# self.slithering = True
# self.walking = True

# the petting area
class Eevee:

    def __init__(self):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True

leopaws = Eevee()
leopaws.name = "Leopaws"
leopaws.species = "Eevee"

class Ninetales:

    def __init__(self):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True

leopaws = Ninetales()
leopaws.name = "Leopaws"
leopaws.species = "Eevee"

class Vulpix:

    def __init__(self):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True

leopaws = Vulpix()
leopaws.name = "Leopaws"
leopaws.species = "Eevee"

class Meowth:

    def __init__(self):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True

leopaws = Meowth()
leopaws.name = "Leopaws"
leopaws.species = "Eevee"

class Snorlax:

    def __init__(self):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True

leopaws = Snorlax()
leopaws.name = "Leopaws"
leopaws.species = "Eevee"

