'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: 5.7
Description: print the sin and cos value for every 10th degree

'''
#import the math module for use of trigonometric functions
import math

#Output header
print(f"{'Degree':<10}{'Sin':<10}{'Cos':<10}")



#Output conversions (convert to radians for use with math module functions)
for i in range(0, 361, 10):
    print(f"{i:<10}{math.sin(math.radians(i)):<10.4f}{math.cos(math.radians(i)):<10.4f}")
