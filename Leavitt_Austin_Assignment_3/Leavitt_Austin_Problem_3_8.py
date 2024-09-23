'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: Problem 3.8
Description: Rewrite ComputeChange.py to fix possible loss of accuracy.
Enter the amount as a whole number of pennies.

'''

# Receive the amount
amount = eval(input("Enter an amount, for example, 1156 is $11.56: "))
remainingAmount = amount

# Find the number of one dollars
numberOfDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

# Find the number of quarters in the remaining amount
numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25

# Find the number of dimes in the remaining amount
numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

# Find the number of nickels in the remaining amount
numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

# Find the number of pennies in the remaining amount
numberOfPennies = remainingAmount

# Display the results
print(f"Your amount {amount} consists of \n\
\t{numberOfDollars} dollars\n\
\t{numberOfQuarters} quarters\n\
\t{numberOfDimes} dimes\n\
\t{numberOfNickels} nickels\n\
\t{numberOfPennies} penies")
