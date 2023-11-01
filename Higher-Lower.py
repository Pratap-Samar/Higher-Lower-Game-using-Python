import random

#welcome and rules
print("welcome to the Higher-Lower game \nThe Rules of the game are: \nThe computer will give you random number \nYou will have to guess if the next generated number will be higher or lower than the given number\nAfter each correct guess you get 5 points and it's game over if your guess is wrong \n\n\n")

#points tracking
point=0

#Game begains
game="Y"or'y'
while game=="Y":
    num1=random.randint(0,100)
    print("\nThe generated number is", num1)
    print("\ntype 'H' for Higher and 'L' for Lower")
    Guess=input("will the next number be Higher or Lower:")
    num2=random.randint(0,100)
    print('\n\nnext number is',num2)
    if num2>num1 and Guess=='H':
        print("congratulation you got 5 points")
        point=point+5
        print('your point is', point)
    elif num1>num2 and Guess=='L':
        print("congratulation you got 5 points")
        point=point+5
        print('your point is', point)
    else:
        print("oops wrong guess")
        break
    a=input("\n\ncontinue the game(Y/N)?")
    if a=='Y' or a=='y':
        game=="Y"

#Game ends 
print("Your Final Point is=", point)
game_over=input('\nGame Over!!!\ntype any key to close:')
