import this 
import sys
import random 

ans=True
while ans:
    quations= int(input("Ask the magic 5 ball aquation: (press enter to quit):"))
    Answers=random.randint(1,5)

    if quations == "":
        break
    elif  Answers== 1:
        print("its certain")
    elif Answers ==2:
        print("out look good:")
    elif Answers == 3:
        print ("you may realy on me")
    elif Answers == 4:
        print("Ask me again later")
    elif Answers ==5:
        print("replay hazy try again")
    else:
        print("you are not human")
        break




