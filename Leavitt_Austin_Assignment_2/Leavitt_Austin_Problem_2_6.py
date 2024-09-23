'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: 2.6
Description: This program with read an integer between 0 and 1000 and
produce a sum of all of the digits

'''

#read the integer
integer = eval(input("Enter a number between 0 and 1000: "))

#Add the right most digit to the sum
digitSum = integer % 10

#Remove the right most digit
integer //= 10

#Add the new right most digit to the sum
digitSum += integer % 10

#Remove the right most digit
integer //= 10

#Add the final right most digit to the sum
digitSum += integer

#Output the sum
print(f"The sum of the digits is {digitSum}")


