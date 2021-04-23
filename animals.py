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

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

leopaws = Eevee("Leopaws", "Eevee")

class Ninetales:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

willows = Ninetales("Willows", "Ninetales")

class Vulpix:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

firefox = Vulpix("Firefox", "Vulpix")

class Meowth:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

kitKat = Meowth("KitKat", "Meowth")

class Snorlax:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

baymax = Snorlax("Baymax", "Snorlax")

# the glass tank
class Ekans:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

rattler = Ekans("Rattler", "Ekans")

class Charmander:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

char = Charmander("Char", "Charmander")

class Arbok:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

cobra = Arbok("Cobra", "Arbok")

class Bulbasaur:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

bulbs = Bulbasaur("Bulbs", "Bulbasaur")

class Squirtle:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

squirt = Squirtle("Squirt", "Squirtle")

# the pond
class Psyduck:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

psy = Psyduck("Psy", "Psyduck")

class Seadra:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

seabiscuit = Seadra("Seabiscuit", "Seadra")

class Tenacool:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

squid = Tenacool("Squid", "Tenacool")

class Shellder:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

shelly = Shellder("Shelly", "Shellder")

class Gyarados:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

gerald = Gyarados("Gerald", "Gyarados")

   