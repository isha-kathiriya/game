import random

print(" 1=Snake\n","2=Water\n","3=Gun")
print('For leave the game type "0"')
print("\nselect any one number to win against the computer")
while True:
    list1 = [1,2,3]
    num=(random.choice(list1))
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
    elif(inp==0):
        print(".....Thanks for playing.......")
    else:
        print("wrong inpute")

    if inp==0:
      break



