class Ninja:
	def __init__(self, first_name, last_name, treats, pet_food, pet):
		self. first_name = first_name
		self.last_name = last_name
		self.treats = treats
		self.pet_food = pet_food
		self.pet = pet

	def walk(self):
		self.pet.play(self.pet)
		return self
	def feed(self):
		self.pet.eat(self.pet, self.pet)
		return self
	def bathe(self):
		self.pet.noise(self.pet)
		return self

class Pet:
	def __init__(self, name, type1, tricks): 
		self.name = name
		self.type1 = type1
		self.tricks = tricks
		self.health = 100
		self.energy = 25
	def sleep(self, energy):
		self.energy + 25
		print("Energy:" , self.energy)
	def eat(self, health, energy):
		self.health = 10
		self.energy = 5
		print("Health:" , self.health)
		print("Energy:" , self.energy)
	def play(self, health):
		self.health = 5
		print("Health:" , self.health)
	def noise(self, noise):
		print("Zzzzzrp")


mo = Ninja("Mo", "Lightning", "turtle bacon", "turtle food", Pet("Speed Racer", "turtle", "hiding in shell"))

mo.walk().feed().bathe()