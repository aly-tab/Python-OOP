from pet import Pet

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

mo = Ninja("Mo", "Lightning", "turtle bacon", "turtle food", Pet("Speed Racer", "turle", "hides"))

mo.walk().feed().bathe()