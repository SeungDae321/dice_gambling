import random

def dice_num():
    return random.randrange(1,7)

intro =     '''
  __________________
   # ROLL THE DICE!#
  ㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    -press ENTER- 
         
         '''      

input(intro)

user_score1 = dice_num()
print(
f'''
#################################
     Your dice choose:          
            {user_score1}       
    You have to ROLL AGAIN!    
#################################
        
''')

input(intro)

user_score2 = dice_num()

print(f'''
#############################################################
                 now your dice number is                    
                     {user_score1} + {user_score2} = {user_score1 + user_score2} 
#############################################################
 ''')

if user_score1 == user_score2:
    print(f'''You have the DOUBLE!{user_score1, user_score2}''')
    input(intro)
    chance_score = dice_num()
    print(
    f'''
    #################################################

    Your totall score is {user_score1} + {user_score2} + {chance_score} = {user_score1 + user_score2 + chance_score}
    
    #################################################
    '''
    )

if user_score1 == user_score2 == chance_score:
    print(
        '''
            ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
           | ARE YOU KIDDING ME?|
            ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        '''
        )




