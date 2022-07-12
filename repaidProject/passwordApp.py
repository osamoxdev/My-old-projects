# Creating a password system

pass_word = 'liver1pool1892'

message = 'Enter your password (Notise that you have only 5 tries): '

user_input = input(message)

trais = 5

while trais > 1 :

    if user_input == pass_word :

        print('Wolcom sir')

        break

    elif user_input != pass_word :

        trais -= 1
        
        message2 = f'You have only {trais} Trais '

        print('Wrong password try agian', end = '')

        user_input = input(f" {'it is your last Try !'if trais == 1  else message2} : ")

        

else :

    print('You\'re out of trais !')


