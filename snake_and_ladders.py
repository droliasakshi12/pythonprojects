print("welcome to snake and ladders game")
print("rules:")
print("1.if snake bites you will fall")
print("2. if there is a ladder you will climb")
print("enjoy playing!")
add=0
import random
def dice():
    global add
    dice1=random.randint(1,6)
    print("generated value is :",dice1)
    add=dice1+add
    print("added value is :",add)


def snl():
    global add
    snake={26:14,67:45,97:78}
    ladder={12:34,30:77,59:90}
    s=list(snake.keys())
    l=list(ladder.keys())
    if(add in s):
        print("oops!there is a snake")
        add=snake[add]
    if(add in l):
        print("yay!you climbed a ladder")
        add=ladder[add]
    




    
n='y'
while(n=='y'):
    if(n=='y'):
        dice()
        snl()
    if(add>=100):
        print("yay!you won")
        break
    if(n=='n'):
        print("thanks for playing ! byeee")
        
    n=input("roll the dice again: 'y' for yes and 'n' for no:")

