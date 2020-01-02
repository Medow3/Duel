# Functions used in the spellcasting phase.
from spell_classes import *

# ((list of runes) -> spell)

def convert_bases_to_spell(list_of_base_runes):
	strings_of_base_runes = []
	for r in list_of_base_runes:
		strings_of_base_runes.append(r.get_type())
	
	spellbook_file = open('spellbook.txt', 'r')
	for line in spellbook_file:
		line = line.rstrip()
		line = line.split()
		sorted_bases = sorted(line[1:])
		if sorted_bases == sorted(strings_of_base_runes):
			spell_cast = line[0]
	spellbook_file.close()
	
	print(spell_cast)
	return spell_cast


# (int, (list of players) -> player)
# returns the player of number equal to the given integer from a list of players
def number_to_player(num, player_list):
	for p in player_list:
		if num == p.get_number():
			return p
	


# (string -> spell)
# returns a spell object with type equal the the inputed string.
def create_spell_from_name(name, current_player):
	if name == 'Ember':
		return(ember(current_player))
	elif name == 'Flamethrower':
		return(flamethrower(current_player))
		