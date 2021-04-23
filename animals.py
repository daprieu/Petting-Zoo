from walking import(Eevee, Ninetales, Vulpix, Meowth, Snorlax)
from swimming import(Psyduck, Seadra, Tentacool, Shellder, Gyarados)
from slithering import(Ekans, Charmander, Arbok, Bulbasaur, Squirtle)
# But you should also take into consideration the fact that there are different types of animals at Critters and Croquettes. Specifically, there are critters in

# the petting area, such as donkeys, llamas, and goats
# the glass tank, like copperheads and rat snakes
# the pond, like mallards and goldfish
# With that in mind, make 5 critter types for each area. As you define each one, give it one of the following properties where most appropriate:

# self.swimming = True
# self.slithering = True
# self.walking = True

# the petting area
leopaws = Eevee("Leopaws", "Eevee", "midday", "Pokechow")
willows = Ninetales("Willows", "Ninetales", "morning", "Pokechow")
firefox = Vulpix("Firefox", "Vulpix", "morning", "Pokechow")
kitKat = Meowth("KitKat", "Meowth", "midday", "Pokechow")
baymax = Snorlax("Baymax", "Snorlax", "afternoon", "Pokechow")

# the pond
psy = Psyduck("Psy", "Psyduck")
seabiscuit = Seadra("Seabiscuit", "Seadra")
squid = Tentacool("Squid", "Tentacool")
shelly = Shellder("Shelly", "Shellder")
gerald = Gyarados("Gerald", "Gyarados")

# the glass tank
rattler = Ekans("Rattler", "Ekans")
char = Charmander("Char", "Charmander")
cobra = Arbok("Cobra", "Arbok")
bulbs = Bulbasaur("Bulbs", "Bulbasaur")
squirt = Squirtle("Squirt", "Squirtle")
print(gerald)
print(baymax.feed())
print(f'{baymax.name} the {baymax.species} is available to pet during the {baymax.shift} shift.')