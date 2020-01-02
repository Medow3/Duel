# Dueling proof of concept game
import pygame
import sys

from player_class import *
from rune_class import *
from button_class import *

from dodge_phase import *
from spellcasting_phase import *

# pygame setup
pygame.init()
clock = pygame.time.Clock()

# screen dimentions
screen_width = 775
screen_height = 775

# object lists
players_list = []
runes_list = []
spell_list = []
UI_list = []

# images
rune_images = [pygame.image.load('fire_rune.png'), pygame.image.load('water_rune.png'), pygame.image.load('air_rune.png')]
player_images = [pygame.image.load('red_boi.png'), pygame.image.load('blue_boi.png')]
button_image = pygame.image.load('button.png')

# game window
win = pygame.display.set_mode((screen_width, screen_height))

# Starts the game in the spellcasting phase.
phase = 'spellcasting'


# sets the position of the inputed spell
def aim(spell):
	pygame.time.delay(50)
	is_clicking = False
	while not is_clicking:
		clock.tick(30)
		
		check_for_quit_action()
		
		is_clicking = pygame.mouse.get_pressed()[0]
		
		if is_clicking:
			spell.set_position(pygame.mouse.get_pos())
		
		redraw_game_window()


def is_mouse_hovering_over(region_hitbox):
	mouse_x, mouse_y = pygame.mouse.get_pos()
	
	if mouse_x >= r.x and mouse_x <= r.x+r.width and mouse_y >= r.y and mouse_y <= r.y+r.height:
		pass


# A weird pygame thing. Stops the game, then code when the game
# window is closed.
def check_for_quit_action():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()


# refreshes the game window, drawing in all the sprits 
def redraw_game_window():
	win.fill((255,255,255))
	
	for s in spell_list:
		s.draw(win)
	
	p1.draw(win)
	p2.draw(win)
	
	for r in runes_list:
		r.draw(win)
	
	for u in UI_list:
		u.draw(win)
	pygame.display.update()







# spawns in players and adds them to the player list.
p1 = player(1, player_images[0])
p2 = player(2, player_images[1])
players_list.append(p1)
players_list.append(p2)

# Main loop of the game. Right now, the only way to break out of this loop 
# and end the game is to close the game window. The check_for_quit_action()
# function handles this.
while 1:
	# the following line makes the game run at 30fps
	clock.tick(30)

	check_for_quit_action()
	
	if phase == 'spellcasting':
		clock.tick(30)
		
		for n in range(1):
			current_player = number_to_player(n, players_list)
			
			fire = rune('fire', (100, 100), rune_images[0])
			water = rune('water', (200, 100), rune_images[1])
			air = rune('air', (300, 100), rune_images[2])
			runes_list = [fire, water, air]
			
			end_spell_selection_button = end_rune_selection('end rune selection', (400, 132), (32, 32), button_image)
			UI_list.append(end_spell_selection_button)
			
			last_mouse_pos = False

			order_of_clicked_runes = []
			number_runes_clicked = 0
			spell_cast = None

			
			while number_runes_clicked < 3:
				clock.tick(30)
				
				check_for_quit_action()
				
				mouse_x, mouse_y = pygame.mouse.get_pos()
				is_clicking = pygame.mouse.get_pressed()[0]
				
				
				if is_clicking and not last_mouse_pos:
					for r in runes_list:
						if r.hitbox.cords_within_box((mouse_x, mouse_y)):
							r.clicked()
							number_runes_clicked += 1
							order_of_clicked_runes.append(r)
					
					for u in UI_list:
						if u.hitbox.cords_within_box((mouse_x, mouse_y)):
							if u.get_purpose() == 'end rune selection':
								number_runes_clicked = u.clicked()
								
				
				last_mouse_pos = is_clicking
				
				redraw_game_window()
			
			
			# deleat the rune objects and clear the rune_list
			del fire
			del water
			del air
			runes_list = []
			
			# deleat the end_rune_selection object
			for u in range(len(UI_list)):
				if UI_list[u].get_purpose() == 'end rune selection':
					del UI_list[u]
			
			
			name_of_spell = convert_bases_to_spell(order_of_clicked_runes)
			spell = create_spell_from_name(name_of_spell, current_player)
			if spell.get_aim_needed() == True:
				aim(spell)
			spell_list.append(spell)
		
		phase = 'dodgeing'
						
	

	
	elif phase == 'dodgeing':
		# timer = seconds * 30fps
		timer = 10 * 30
		start_time = timer
		
		while timer > 0:
			clock.tick(30)
			
			check_for_quit_action()
			
			# tick player invinsibility frames
			for p in players_list:
				p.hit_cooldown_tick()
			
			# check spell activations
			for spell in spell_list:
				if start_time - timer == spell.get_windup():
					spell.set_is_active(True)
				elif start_time - timer == spell.get_duration() + spell.get_windup():
					spell.set_is_active(False)
			
			# get list of user inputs
			keys = pygame.key.get_pressed()
			
			# move players
			player_1_move(p1, keys, screen_width, screen_height)
			player_2_move(p2, keys, screen_width, screen_height)
			
			# check collisions
			for player in players_list:
				for spell in spell_list:
					if player.hitbox.is_colliding(spell.hitbox) and spell.get_is_active() and player.get_hit_cooldown() == 0:
						player.hit(spell.get_damage())
			
			timer -= 1
			redraw_game_window()
		
		# deleat the spell objects
		for s in range(len(spell_list)):
			del spell_list[s]
		
		phase = 'spellcasting'
			
	redraw_game_window()
