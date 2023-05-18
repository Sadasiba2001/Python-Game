#Create position replace
def position_replace(int_position,game_list):
    user_input=input('Enter a string to place at position:')
    game_list[int_position]=user_input
    print(game_list)
    return game_list
