from hitbox_class import *

class button(object):
	def __init__(self, purpose, pos, dimentions, image):
		self.purpose = purpose
		self.image = image
		self.x = pos[0]
		self.y = pos[1]
		self.width = dimentions[0]
		self.height = dimentions[1]
		self.hitbox = hitbox(self.x, self.y, self.width, self.height, self)
	
	def get_purpose(self):
		return self.purpose
	
	def draw(self, win):
		win.blit(self.image, (self.x, self.y))


class end_rune_selection(button):
	def __init__(self, purpose, pos, dimentions, image):
		self.purpose = purpose
		self.image = image
		self.x = pos[0]
		self.y = pos[1]
		self.width = dimentions[0]
		self.height = dimentions[1]
		self.hitbox = hitbox(self.x, self.y, self.width, self.height, self)
	
	def clicked(self):
		print(self.purpose, 'clicked')
		return(1000)