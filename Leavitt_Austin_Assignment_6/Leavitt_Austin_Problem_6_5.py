'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#:
Description: Sort three numbers in ascending order

'''

#Create sorting function
def displaySortedNumbers(num1, num2, num3):
    #Check to see if num1 is greater than num2
    #if true then swap the values
    if num1  > num2:
        num1,num2 = num2,num1

    #Check if num2 is greater than num2
    #if true then swap the values
    if num2 > num3:
        num2, num3 = num3, num2

    #Recheck num1 and num2
    if num1  > num2:
        num1, num2 = num2, num1

    #print the sorted result
    print(f"The sorted numbers are {num1}, {num2}, {num3}")







#Create the main function
def main():
    #prompt the user to input three values
    num1, num2, num3 = eval(input("Enter three numbers: "))

    #invoke the sorting function
    displaySortedNumbers(num1, num2, num3)



#invoke the main function
main()
