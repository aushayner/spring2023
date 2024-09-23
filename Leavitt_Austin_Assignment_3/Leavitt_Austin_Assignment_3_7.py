'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: 3.7
Description: Display a random uppercase letter

'''

#import the time module
import time

#Give the time variable an integer value form the time function
time = (int(time.time()) % 26) + 65

#Map int to 65 - 90 (ASCII code 'A' - 'Z')
#code = (time % 26) + 65

#Display the results using the chr function to convert the decimal to a char
print(f"Random letter is {chr(time)}")
