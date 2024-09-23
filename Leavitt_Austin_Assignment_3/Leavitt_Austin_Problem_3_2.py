'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: 3.2
Description: Calculate the great circle distance between two
points on the earth given two coordinates.

'''

#Import the math module
import math

#prompt the user to enter in values for point one and point two
x1, y1 = eval(input("Enter point one (latitude and longitude) in degrees: "))
x2, y2 = eval(input("Enter point two (latitude and longitude) in degrees: "))

#Compute the distance
distance = 6371.01 * \
           (math.acos(math.sin(math.radians(x1)) * \
           math.sin(math.radians(x2)) + \
           math.cos(math.radians(x1)) * \
           math.cos(math.radians(x2)) * \
           math.cos(math.radians(y1 -y2)) ))

#print the results
print(f"The distance between the two points is {distance}.")
