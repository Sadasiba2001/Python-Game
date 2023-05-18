from Game_Displaying_Function import *
from position_choice import *
from position_replace import *
from game_run import *
game_on = True
game_list = [0, 1, 2]
while game_on==True:
    display_game(game_list)
    int_position=position_choose()
    game_list=position_replace(int_position,game_list)
    game_on=game_run()