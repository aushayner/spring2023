'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: Problem 3.4
Description: Calculate the area of a pentagon based on the length
of a side given by the user.

'''
#import the math library for use of tan and pi
import math

#prompt user for the side length
sideLength = eval(input("Enter the side: "))

#calculate the area
area = (5 * (sideLength ** 2)) / (4 * math.tan(math.pi / 5))

#output the result
print(f"The area of the pentagon is {area}")


