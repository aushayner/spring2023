'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: 2.3
Description: This program will read a number in feet, convert it to meters, and
display the result

'''
#get input for the value in feet
feet = eval(input("Enter a value for feet: "))

#perform the conversion to meters
meters = feet * 0.305

#ouput the converted value
print(f"{feet} feet is {round(meters, 4)} meters")
