'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: 2.4
Description: This program will read a value in pounds, convert the value to
kilograms, and display the result

'''

#read the value for pounds
pounds = eval(input("Enter a value for pounds: "))

#convert from pounds to kilograms
kilograms = pounds * 0.454

#ouput the result of the conversion
print(f"{pounds} pounds is {round(kilograms, 3)} in kilograms")
