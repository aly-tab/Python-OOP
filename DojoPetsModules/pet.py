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