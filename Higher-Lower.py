import random

#welcome and rules
print("welcome to the Higher-Lower game \nThe Rules of the game are: \nThe computer will give you random number \nYou will have to guess if the next generated number will be higher or lower than the given number\nAfter each correct guess you get 5 points and it's game over if your guess is wrong \n\n\n")

#points tracking
point=0

#Game begins
game="Y"
while game=="Y":
    num1=random.randint(0,100)
    print("\nThe generated number is", num1)
    print("\nType 'H' for Higher and 'L' for Lower")
    Guess=input("will the next number be Higher or Lower:").upper()
    
    num2=random.randint(0,100)
    print('\n\nNext number is',num2)
        
    if num2>num1 and Guess=='H'or num1>num2 and Guess=='L':
        print("Congratulation you got 5 points")
        point=point+5
        print('Your point is', point)

    elif num2<num1 and Guess=='H'or num1<num2 and Guess=='L':
        print("oops wrong guess")
        break            
    else:
        print('invalid input')
        pass
#to keep the going on
    a=input("\n\nType Y to continue the game(Y)?").upper()
    if a=='Y':
        game=="Y"
    else:
        break

#game Over and display of final score 
print("Your Final Point is=", point)
game_over=input('\nGame Over!!!\ntype any key to close:')
       
        
