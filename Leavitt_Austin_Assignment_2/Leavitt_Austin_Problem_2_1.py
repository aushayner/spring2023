'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: Problem 2.1
Description: Convert Celsius to Farehneit and display the result

'''

#Prompt user for an integer representing celsius to convert to farenheit
celsius = eval(input("Enter a degree in Celsius: "))

#Convertion calculation
farenheit = (9 / 5) * celsius + 32

#Ouput the result
print(f"{celsius} Celsius is {round(farenheit, 1)} farenheit")

