# Functions used in the dodgeing phase.
import pygame

# (player, (list of user inputs), int, int -> None)
# Using the list of user inputs (as well as the player and screen dimentions),
# moves player 2 according to what buttons are being pressed. 
# Player 1 uses WASD to move.
def player_1_move(p1, keys, screen_width, screen_height):
	if keys[pygame.K_w] and p1.y >= p1.vel and keys[pygame.K_a] and p1.x >= p1.vel:
		p1.y -= p1.vel*0.6
		p1.x -= p1.vel*0.6
		p1.facing_UP, p1.facing_LEFT, p1.facing_DOWN, p1.facing_RIGHT = True, True, False, False
	elif keys[pygame.K_a] and p1.x >= p1.vel and keys[pygame.K_s] and p1.y+p1.height <= screen_height-p1.vel:
		p1.x -= p1.vel*0.6
		p1.y += p1.vel*0.6
		p1.facing_UP, p1.facing_LEFT, p1.facing_DOWN, p1.facing_RIGHT = False, True, True, False
	elif keys[pygame.K_s] and p1.y+p1.height <= screen_height-p1.vel and keys[pygame.K_d] and p1.x+p1.width <= screen_width-p1.vel:
		p1.y += p1.vel*0.6
		p1.x += p1.vel*0.6
		p1.facing_UP, p1.facing_LEFT, p1.facing_DOWN, p1.facing_RIGHT = False, False, True, True
	elif keys[pygame.K_d] and p1.x+p1.width <= screen_width-p1.vel and keys[pygame.K_w] and p1.y >= p1.vel:
		p1.x += p1.vel*0.6
		p1.y -= p1.vel*0.6
		p1.facing_UP, p1.facing_LEFT, p1.facing_DOWN, p1.facing_RIGHT = True, False, False, True
	elif keys[pygame.K_w] and p1.y >= p1.vel:
		p1.y -= p1.vel
		p1.facing_UP, p1.facing_LEFT, p1.facing_DOWN, p1.facing_RIGHT = True, False, False, False
	elif keys[pygame.K_a] and p1.x >= p1.vel:
		p1.x -= p1.vel
		p1.facing_UP, p1.facing_LEFT, p1.facing_DOWN, p1.facing_RIGHT = False, True, False, False
	elif keys[pygame.K_s] and p1.y+p1.height <= screen_height-p1.vel:
		p1.y += p1.vel
		p1.facing_UP, p1.facing_LEFT, p1.facing_DOWN, p1.facing_RIGHT = False, False, True, False
	elif keys[pygame.K_d] and p1.x+p1.width <= screen_width-p1.vel:
		p1.x += p1.vel
		p1.facing_UP, p1.facing_LEFT, p1.facing_DOWN, p1.facing_RIGHT = False, False, False, True


# (player, (list of user inputs), int, int -> None)
# Using the list of user inputs (as well as the player and screen dimentions),
# moves player 2 according to what buttons are being pressed. 
# Player 2 uses the arrow keys to move.
def player_2_move(p2, keys, screen_width, screen_height):
	if keys[pygame.K_UP] and p2.y >= p2.vel and keys[pygame.K_LEFT] and p2.x >= p2.vel:
		p2.y -= p2.vel*0.6
		p2.x -= p2.vel*0.6
		p2.facing_UP, p2.facing_LEFT, p2.facing_DOWN, p2.facing_RIGHT = True, True, False, False
	elif keys[pygame.K_LEFT] and p2.x >= p2.vel and keys[pygame.K_DOWN] and p2.y+p2.height <= screen_height-p2.vel:
		p2.x -= p2.vel*0.6
		p2.y += p2.vel*0.6
		p2.facing_UP, p2.facing_LEFT, p2.facing_DOWN, p2.facing_RIGHT = False, True, True, False
	elif keys[pygame.K_DOWN] and p2.y+p2.height <= screen_height-p2.vel and keys[pygame.K_RIGHT] and p2.x+p2.width <= screen_width-p2.vel:
		p2.y += p2.vel*0.6
		p2.x += p2.vel*0.6
		p2.facing_UP, p2.facing_LEFT, p2.facing_DOWN, p2.facing_RIGHT = False, False, True, True
	elif keys[pygame.K_RIGHT] and p2.x+p2.width <= screen_width-p2.vel and keys[pygame.K_UP] and p2.y >= p2.vel:
		p2.x += p2.vel*0.6
		p2.y -= p2.vel*0.6
		p2.facing_UP, p2.facing_LEFT, p2.facing_DOWN, p2.facing_RIGHT = True, False, False, True
	elif keys[pygame.K_UP] and p2.y >= p2.vel:
		p2.y -= p2.vel
		p2.facing_UP, p2.facing_LEFT, p2.facing_DOWN, p2.facing_RIGHT = True, False, False, False
	elif keys[pygame.K_LEFT] and p2.x >= p2.vel:
		p2.x -= p2.vel
		p2.facing_UP, p2.facing_LEFT, p2.facing_DOWN, p2.facing_RIGHT = False, True, False, False
	elif keys[pygame.K_DOWN] and p2.y+p2.height <= screen_height-p2.vel:
		p2.y += p2.vel
		p2.facing_UP, p2.facing_LEFT, p2.facing_DOWN, p2.facing_RIGHT = False, False, True, False
	elif keys[pygame.K_RIGHT] and p2.x+p2.width <= screen_width-p2.vel:
		p2.x += p2.vel
		p2.facing_UP, p2.facing_LEFT, p2.facing_DOWN, p2.facing_RIGHT = False, False, False, True

