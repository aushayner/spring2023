'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#:
Description: Output square roots for multiples of 2 up to 20

'''

#import the math module for use of sqrt
import math

#Output header
print(f"{'Number':<10}{'Square Root':<10}")



#Output squareroots
for i in range(0, 21, 2):
    print(f"{i:<10}{math.sqrt(i):<10.4f}")
