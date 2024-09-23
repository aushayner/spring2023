'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: Problem 3.5
Description: Calculate the area of a regulate polygon given the
number of sides and the length of a side given by the user

'''

#import the math library for the use of tan and pi
import math

#prompt the user for the number of sides and the length of the sides
numberSides = eval(input("Enter the number of sides: "))
sideLength = eval(input("Enter the side: "))

#Calculate the area
area = (numberSides * (sideLength ** 2)) / \
       (4 * math.tan(math.pi / numberSides))

#Ouput the results
print(f"The area of the polygon is {area}")
