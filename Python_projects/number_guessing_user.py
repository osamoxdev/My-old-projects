# user guessing 

import random


# def guessing (x) :

#     number = random.randint(1, x)

#     trais = 0


#     while trais < 5 : 

#         guessing = int(input(f'Guess a number between 1 and {x} : ')) 

#         trais += 1 

#         if guessing < number :

#             print(f' {guessing} is too low ')

#         elif guessing > number : 

#             print(f' {guessing} is too High ')

#         elif guessing == number :

#             print(f' Yes!, you guessed the number {number} correctly')
#             break

#     print(f' Unfortonately You did not guessed it right , the number was {number}')

# guessing(25)



# computer guessing

def computer_guessing(x): 

    low = 1

    high = x

    feadback = ''
    print(f'Guess a number between 1 and {x} ')

    while feadback != 'right'  :

        if low != high : 

            number = random.randint(low, high) # a point
        else : 
            number = low # or high 

        feadback = input(f'Is it {number} ?  \n') 

        if feadback == 'high' :

            high = number -1 

        elif feadback == 'low' : 

            low  = number + 1
            
        elif feadback == 'right' :

            print(f' Yes!, I guessed the number {number} correctly')
            break

        
computer_guessing(15)
