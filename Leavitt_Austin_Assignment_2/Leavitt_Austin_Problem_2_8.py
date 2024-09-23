'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: 2.8
Description: This program will calculate the energy needed to heat water from
an initial tempurature to a final tempurature.

'''
# Prompt the user for mass, initial tempurature, and final tempurature
mass = eval(input("Enter the amount of water in kilograms: "))

initialTempurature = eval(input("Enter the initial tempurature: "))

finalTempurature = eval(input("Enter the final tempurature: "))

# Calculate the amount of energy needed
energy = mass * (finalTempurature - initialTempurature) * 4184

# Output the results
print(f"The energy needed is {round(energy, 1)}")
