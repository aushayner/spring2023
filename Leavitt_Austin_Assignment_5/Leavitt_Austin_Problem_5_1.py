'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: 5_1
Description: Count positive and negative numbers and compute the average
of numbers

'''
#Counter, total, and flag variables
positiveCounter = 0
negativeCounter = 0
total = 0
flag = True

#Get integers from user and total themwhile the flag is true
#set to false when input is 0
while flag == True:
    num = eval(input("Enter an integer, the input ends if it is 0: "))

    if num > 0 :
        positiveCounter += 1
        total += num
    elif num < 0:
        negativeCounter += 1
        total += num
    else:
        flag = False

#output        
if total != 0:
    print(f"The number of positives is {positiveCounter}")
    print(f"The number of negatives is {negativeCounter}")
    print(f"The total is {total}")
    print(f"The average is {total / (negativeCounter + positiveCounter)}")
else:
    print("You didn't enter any number")
