class straight_line(object):
	def __init__(self, type, coordinate, owner):
		self.owner = owner
		self.type = type
		self.coordinate = coordinate
		
		if self.type == 'horizontal':
			self.Y_intersect = coordinate
			self.X_intersect = None
		elif self.type == 'vertical':
			self.Y_intersect = None
			self.X_intersect = coordinate
		else:
			print('Non valid line type')
		
		self.two_points = self.find_two_points_on_line()
	
	# (self -> (tuple of int), (tuple of int))
	# Used only in the __init__ funtion of the strait_line class.
	# Returns two points on the line in tuple form ex. (x, y)
	def find_two_points_on_line(self):
		if self.type == 'horizontal':
			return(((0, self.coordinate), (1, self.coordinate)))
		else:
			return(((self.coordinate, 0), (self.coordinate, 1)))
	
	# returns a tuple containing two points on the line
	def get_two_points(self):
		return(self.two_points)
	
	# returns the coordinate
	def get_value(self):
		return(self.coordinate)