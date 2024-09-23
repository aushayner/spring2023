'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: Problem 2.2
Description: Read the radius and length of a cylinder and compute
the area and volume

'''
#import the math module for the pi constant
import math

#prompt the user to enter values for radius and length
radius, length = eval(input("Enter the radius and length of a cylinder: "))

#Calculate the area and volume
area = radius * radius * math.pi
volume = area * length

#Ouput the area and volume
print(f"The area is {round(area, 4)}\n The volume is {round(volume, 1)}")




