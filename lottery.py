import random


count = True
while count:
    input("Press a key: ")
    lottery_values = random.sample(range(0, 10), 3)
    print("{first}, {second}, {third}".format(
        first=lottery_values[0],
        second=lottery_values[1],
        third=lottery_values[2]
    ))
    if 7 in lottery_values:
        print("Congratulations!!")
        count = False
    else:
        print("Better luck next time!!!")   
        count = False     

