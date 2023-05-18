#Create position choice
def position_choose():
    position='hii'
    while position not in ['0','1','2']:
        position=input('\n Pick a position (0,1,2):')
        if position not in ['0','1','2']:
            print('\nWrong choice!')
    int_position=int(position)
    return int_position


