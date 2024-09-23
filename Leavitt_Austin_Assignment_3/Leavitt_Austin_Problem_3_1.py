'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: Problem 3.1
Description: Prompt the user for the lenth from the center of a pentagon to
a vertex and compute the area of the pentagon.

'''
#import the math library for use of pi and sqrt
import math

#prompt user for a value for radius
radius = eval(input("Enter the length from the center to a vertex: "))

#compute the lenth of a side for use in the area formula
sideLength = 2 * radius * math.sin(math.pi / 5)

#compute the area
area = ( (3 * math.sqrt(3)) / 2 )*(sideLength ** 2)

#print the result
print(f"The area of the pentagon is {area :.2f}")


