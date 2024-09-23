'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: Problem 3.11
Description: Receive a four-digit integer and
display the number in reverse order

'''

# Receive the four digit integer
number = eval(input("Enter a four-digit integer: "))

# Reverse the number
newNumber = number // 1000
number %= 1000
newNumber += (number // 100) * 10
number %= 100
newNumber += (number // 10) * 100
number %= 10
newNumber += number * 1000

#Output the result
print(f"The reversed number is {newNumber}")
