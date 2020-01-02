from hitbox_class import *
# import pygame

class player(object):
	def __init__(self, number, image):
		self.number = number
		self.image = image
		self.x = 300
		self.y = 500
		self.width = 64
		self.height = 64
		self.vel = 10
		self.health = 20
		self.hit_cooldown = 0
		self.color = (255,0,0)
		self.facing_UP = True
		self.facing_RIGHT = False
		self.facing_DOWN = False
		self.facing_LEFT = False
		self.hitbox = hitbox(self.x, self.y, self.width, self.height, self)
		self.spell_list = []
	
	# updates the players health when their hit by an attack as well
	# as starts the hit_cooldown timer
	def hit(self, ammount):
		self.health -= ammount
		if self.health <= 0:
			self.dies()
		self.hit_cooldown = 50
		print(self.health)
	
	# When a player is hit, this function counts down that players
	# invincibility frames.
	def hit_cooldown_tick(self):
		if self.hit_cooldown > 0:
			self.hit_cooldown -= 1
	
	# function run uppon player death
	def dies(self):
		print('Player', self.number, 'has died')
	
	# used in the redraw_game_window() function
	def draw(self, win):
		self.hitbox = hitbox(self.x, self.y, self.width, self.height, self)
		win.blit(self.image, (self.x, self.y))
		# uncomment line below and the import pygame line at the top of
		# this file to view the actual player hitbox.
		# pygame.draw.rect(win, self.color, (self.hitbox.x, self.hitbox.y, self.hitbox.width, self.hitbox.height), 1)
	
	# returns the players hitbox class
	def get_hitbox(self):
		return self.hitbox
	
	def get_number(self):
		return self.number
	
	def get_hit_cooldown(self):
		return self.hit_cooldown