# "Snake-Water-Gun Game using Python"
'''
1 for snake
-1 for water
0 for gun


'''
import random
computer = random.choice([-1,0,1])
youstr = input("Enter your choice(1 for snake , -1 for water,0 for gun): ")
youDict ={"1": 1, "-1": -1, "0": 0}
reverseDict={1:"snake", -1:"water", 0:"gun"}
you=youDict[youstr]
print(f"you choose{reverseDict[you]}\ncomputer choose{reverseDict[computer]}")

if(computer==you):
    print("Its draw")
if(computer == -1 and you==1):
    print("You win!")
elif(computer == -1 and you ==0):
    print("You lose!")
elif(computer == 1 and you==-1):
    print("You lose!")
elif(computer ==1 and you==0):
    print("You win!")
elif(computer == 0 and you==-1):
    print("You win!")
elif(computer ==0 and you==1):
    print("You lose!")
else:
    print("Something wrong")
