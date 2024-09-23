'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: 2.16
Description: This program will calculate average acceleration given a
starting velocity, ending velocity, and timespan

'''

#Prompt user for starting velocity, ending velocity, and timespan
startVelocity, endVelocity, time = eval(input("Enter v0, v1, and t: "))

#Calculate the average acceleration
acceleration = (endVelocity - startVelocity) / time

#Output the results
print(f"The average acceleration is {round(acceleration, 4)}")
