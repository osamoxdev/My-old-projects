import random 



# while trais > 0 : 
for game in range(3) :

    def play() : 

        # global trais
        # trais = 3



        user = input("What do you choese 'r' for rock 'p' for paper 's' for scissor : ")
        # trais -= 1
        opponent = random.choice(['r', 'p', 's'])

        print(opponent)

        if user == opponent : 
            return 'it\'s a Tie!'

        if win(user, opponent) : 

            return 'you won!'

        if win(opponent, user) :

            return 'You lost'

        # return 'You lost'



    def win(winer, loser) : 

    # r > s, s > p , p > r

        if (winer == 'r' and loser == 's') or (winer == 's' and loser == 'p') or \
        (winer == 'p' and loser == 'r'):

            return True


    print(play())

print('Game Over')
