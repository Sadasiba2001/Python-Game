def full_game():
    user_choice='Hii'
    check='Yes'
    user_wish='No'
    #Display numbers
    game_list=[0,1,2]
    print(game_list)
    #Creating Position Choice
    while user_choice not in ['0','1','2'] or check==True:
        user_choice=input('Enter your choice in (0,1,2):')
        if user_choice not in ['0','1','2']:
            print('Wrong Choice')
        else:
            print('your choice:-',user_choice)
            convert_user_choice=int(user_choice)
        #Taking replace string
            user_input=input('Enter somthing for replacement:').upper()
            game_list[convert_user_choice]=user_input
            print(game_list)
        #while user_wish not in ['Y','N']:
            user_wish=input('Do You want to play more (Y or N):').upper()
            if user_wish not in ['Y','N']:
                print('Wrong Choice')
            else:
                if user_wish=='Y':
                    print('Good Choice')
                    check = True
                else:
                    print('Game Over')
                    break
full_game()
