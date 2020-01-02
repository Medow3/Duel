from straight_line_class import *

class hitbox(object):
	def __init__(self, x, y, width, height, owner):
		self.owner = owner
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.top = straight_line('horizontal', y, self)
		self.bottom = straight_line('horizontal', y + height, self)
		self.right = straight_line('vertical', x + width, self)
		self.left = straight_line('horizontal', x, self)
		self.sides = [self.top, self.bottom, self.right, self.left]
	
	def __str__(self):
		return('hitbox')
	
	def __repr__(self):
		return(self.owner.type + ' hitbox')
	
	# ((tuple of int) -> bool)
	# Input a point in the form of a tuple ex. (x, y). Returns whether
	# the given point in within the hitbox.
	def cords_within_box(self, point):
		x, y = point[0], point[1]
		if self.left.get_value() <= x and self.right.get_value() >= x and self.top.get_value() <= y and self.bottom.get_value() >= y:
			return True
		return False
	
	# small helper function used in the is_colliding function
	def det(self, a, b):
		return a[0] * b[1] - a[1] * b[0]
	
	# (hitbox -> bool)
	# returns whether the inputed hit box is coliding with this hitbox
	def is_colliding(self, other):
		for i in self.sides:
			line1 = i.get_two_points()
			for j in other.get_sides():
				line2 = j.get_two_points()
				
				xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
				ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

				div = self.det(xdiff, ydiff)
				if div == 0:
					continue

				d = (self.det(*line1), self.det(*line2))
				x = self.det(d, xdiff) / div
				y = self.det(d, ydiff) / div
				
				if self.cords_within_box((x, y)) and other.cords_within_box((x, y)):
					return True
		return False
	
	def get_sides(self):
		return(self.sides)







		