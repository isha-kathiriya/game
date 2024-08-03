import random
list1 = [1,2,3]
num=(random.choice(list1))
print(" 1=Snake\n","2=Water\n","3=Gun")
print("\nselect any one number to win against the computer")
inp=int(input("Enter your Number:"))
print("Computer select num is:",num)
if (inp==num):
    print("Draw")
elif (inp==1 and num==2):
    print("Player Win")
elif(inp==1 and num==3):
    print("Computer win")
elif(inp==2 and num==3):
    print("player win")
elif(inp==2 and num==1):
    print("Computer win")
elif(inp==3 and num==1):
    print("Playerr win")
elif(inp==3 and num==2):
    print("Computer win")
else:
    print("wrong inpute")
