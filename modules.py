#class goes here

class Player():
	instances = []
	def __init__(self, name, score):
		# initialize attributes name and beginning score to player
		self.name = name
		self.score = score
		self.__class__.instances.append(self)



	def __str__(self):
		return self.name
		# return "{}: {} points".format(self.name, self.score)



