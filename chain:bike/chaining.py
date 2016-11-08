class Bike (object):
	def __init__(self, price, max_speed, miles):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
		
		

	def displayInfo(self):
		print (self.price)
		print (self.miles)
		print (self.max_speed)
		return self

	def ride(self):
		self.miles += 10

		return self

	def reverse(self):
		self.miles -= 5
		return self


mach10 = Bike('200$','200mph', 90)
mach10.ride().ride().reverse().displayInfo()