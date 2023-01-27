import random
#x,y=input("Enter the range of numbers you want to find a random number of: ").split(" ")
#x=int(x)
#y=int(y)
#print("The number is: "+str(random.randint(x,y)))



dice_count = input("how many dice? ")
dice_type = int(input("how many sides do the dice have? "))
dice_count = int(dice_count)
x=0
while x < dice_count:
    x=x+1
    roll = random.randint(1, dice_type)
    if roll == 1:
        print("Critical Fail! "+str(roll),end=" ")
    elif roll == dice_type:
        print("Critical hit! "+str(roll),end=" ")
    else:
        print(roll,end=" ")

    
    #print(random.randint(1,dice_type),end=" ")
