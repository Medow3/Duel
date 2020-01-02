from hitbox_class import *

class rune(object):
	def __init__(self, type, pos, image):
		self.type = type
		self.image = image
		self.x = pos[0]
		self.y = pos[1]
		self.width = 64
		self.height = 64
		self.hitbox = hitbox(self.x, self.y, self.width, self.height, self)
	
	def __str__(self):
		return(self.type)
	
	def __repr__(self):
		return(self.type)
	
	def __eq__(self, other):
		if other.type == rune and other.type == self.type:
			return True
		return False
	
	def get_type(self):
		return self.type
	
	def clicked(self):
		print(self.type)
	
	def draw(self, win):
		win.blit(self.image, (self.x, self.y))