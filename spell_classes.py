from hitbox_class import *
import pygame
spell_images = [pygame.image.load('ember.png'), pygame.image.load('flame.png'), pygame.image.load('flamethrower.png')]

class spell(object):
	def __init__(self, owner):
		self.owner = owner
	
	def move(self):
		pass
	
	def draw(self, win):
		self.hitbox = hitbox(self.x, self.y, self.width, self.height, self)
		if self.is_active:
			win.blit(self.image, (self.x, self.y))
	
	def set_position(self, center):
		self.center = center
		self.x = self.center[0] - self.width/2
		self.y = self.center[1] - self.height/2
		self.hitbox = hitbox(self.x, self.y, self.width, self.height, self)
	
	def get_aim_needed(self):
		return self.aim_needed
	
	def get_damage(self):
		return self.damage
	
	def get_is_active(self):
		return self.is_active
	
	def get_windup(self):
		return self.windup
	
	def get_duration(self):
		return self.duration
	
	# (bool -> None)
	# sets is_active to inputed bool
	def set_is_active(self, input):
		self.is_active = input
		
	
	

# Ember fire
# Flame fire fire
# Flamethrower fire fire fire
# Breeze air
# Air_Cutter air air
# Wind_Slice air air air
# Dribble water
# Water_Shot water water
# Hydro_Cannon water water water
# Boiling_Pulse fire water
# Flame_Tornado fire air
# Mist air water
# Scalding_Water fire fire water
# Enlarged_Flame fire fire air
# Flame_Tornato_Cutter air air fire
# Mist_Cutter air air water
# Boiling_Wave water water fire
# Heavy_Fog water water air
# Steam fire air water

class ember(spell):
	def __init__(self, owner):
		self.name = 'Ember'
		self.image = spell_images[0]
		self.windup = 1.5 * 30 # seconds * 30fps
		self.duration = 5 * 30 # seconds * 30fps
		self.damage = 1
		self.vel = 0
		self.width = 100
		self.height = 100
		self.aim_needed = True
		self.is_active = False


class flame(spell):
	def __init__(self, owner):
		self.name = 'Flame'
		self.image = spell_images[1]
		self.windup = 1 * 30 # seconds * 30fps
		self.duration = 7 * 30 # seconds * 30fps
		self.damage = 2
		self.vel = 0
		self.width = 200
		self.height = 200
		self.aim_needed = True
		self.is_active = False


class flamethrower(spell):
	def __init__(self, owner):
		self.name = 'Flamethrower'
		self.image = spell_images[2]
		self.windup = round(0.5 * 30) # seconds * 30fps
		self.duration = 9 * 30 # seconds * 30fps
		self.damage = 3
		self.vel = 0
		self.width = 300
		self.height = 300
		self.aim_needed = True
		self.is_active = False
		




















