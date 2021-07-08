class Ninja:
	def __init__(self, first_name, last_name, treats, pet_food, pet):
		self. first_name = first_name
		self.last_name = last_name
		self.treats = treats
		self.pet_food = pet_food
		self.pet = pet

	def walk(self):
		print(self.first_name , "is walking" , self.pet.name + ".")
		self.pet.play(self.pet)
		return self
	def feed(self):
		print(self.first_name , "is feeding" , self.pet.name + ".")
		self.pet.eat(self.pet, self.pet)
		return self
	def bathe(self):
		print(self.first_name , "is bathing" , self.pet.name + ".")
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
		self.energy += 25
		print(self.name + "'s energy is now" , self.energy + ".")
	def eat(self, health, energy):
		self.health += 10
		self.energy += 5
		print(self.name + "'s health is now" , str(self.health) + ".")
		print(self.name + "'s energy is now" , str(self.energy) + ".")
	def play(self, health):
		self.health += 5
		print(self.name + "'s health is now" , str(self.health) + ".")
	def noise(self, noise):
		print("Zzzzzrp")


mo = Ninja("Mo", "Lightning", "turtle bacon", "turtle food", Pet("Speed Racer", "turtle", "hiding in shell"))

mo.walk().feed().bathe()