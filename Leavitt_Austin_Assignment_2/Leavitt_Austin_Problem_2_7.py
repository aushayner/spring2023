'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: 2.7
Description: This program will calculate the number of years and days from
an input number of minutes assuming a year is 365 days

'''

#Prompt the user for a number of minutes
minutes = eval(input("Enter the number of minutes: "))



#Calculate the total number of days
days = minutes // (60 * 24)

#Calculate the number of years
years = days // 365

#Calculate the remaining days
days %= (years * 365)

#Output the results
print(f"{minutes} minutes is approximately {years} years and {days} days")
