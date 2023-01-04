##################################PROJECT-2#########################################
############################# THE PERFECT GUESS ################################

import random

def checkRange(num):
    if a<1 and a>100:
        print("Invalid input")

print("********************************_WELCOME TO THE PERFECT GUESS GAME_******************************")
print("\n\t\t_Computer is gonna generate a number_")
print("\t\t\t  From 1 to 100")
print("\t\t\tGuess the number :)")
randNum = random.randint(1,100)
print("\n\t->->->->->->->Computer generated a Number<-<-<-<-<-<-<-<-")
print("\n\t->->->->->->->->->Time to guess<-<-<-<-<-<-<-<-<-<-")

a = int(input("\t\t\t\t"))
checkRange(a)
attempt = 1

while(randNum != a):
    if(a < randNum):
        attempt+=1
        print("Oops, Number is smaller than Generated Number\nTry Again!!")
        print("Guess No. -> ", attempt)
        a = int(input("\t\t\t\t"))
        checkRange(a)
    else:
        attempt+=1
        print("Oops, Number is Greater than Generated Number\nTryAgain!!")
        print("Guess No. -> ", attempt)
        a = int(input("\t\t\t\t"))
        checkRange(a)



if randNum == a:
    print("Congratulations!! That's a Perfect Guess!!\nNumber of Attempt = ",attempt)

#STORING HIGH SCORE

with open("hiScore.txt",'r') as f:
    hiScore = int(f.read())
if(attempt < hiScore):
    print("\n\t\t\t\tYahooooooo..!!")
    print("\t->->->->->->->->->->->You Broke The High Score<-<-<-<-<-<-<-<-<-<-<-")
    with open("hiScore.txt", 'w') as f:
        f.write(str(attempt))
