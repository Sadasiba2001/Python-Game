def game_run():
   user_input='Wrong'
   while user_input not in ['Y','N'] or game_on==True:
      user_input=input('Do you want to play more (Y or N):').upper()
      if user_input not in ['Y','N']:
         print('Wrong Choice\nTry Again')
      elif user_input in ['Y','N']:
         if user_input=='Y':
            return True
         else:
            print('game_over')
            return False
