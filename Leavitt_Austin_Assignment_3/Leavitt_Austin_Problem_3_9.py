'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: Problem 3.9
Description: Read employee information and output a payrole statement

'''
# Receive employee information
name = input("Enter employee's name: ")
hours = eval(input("Enter number of hours worked in a week: "))
hourlyPayRate = eval(input("Enter hourly pay rate: "))
federalTaxRate = eval(input("Enter federal tax withholding rate: "))
stateTaxRate = eval(input("Enter state tax withholding rate: "))
print()

# Calculate gross pay, federal tax, state tax, total deduction, and net pay
grossPay = hours * hourlyPayRate
federalTax = grossPay * federalTaxRate
stateTax = grossPay * stateTaxRate
totalDeduction = federalTax + stateTax
netPay = grossPay - totalDeduction

# Output the payrole statement
print(f"Employee Name: {name}")
print(f"Hours Worked: {hours}")
print(f"Pay Rate: ${hourlyPayRate}")
print(f"Gross Pay: ${grossPay:.2f}")
print(f"Deductions: ")
print(f"\tFederal Withholding ({federalTaxRate * 100}%): ${federalTax:.2f}")
print(f"\tState Withholding ({stateTaxRate * 100}%): ${stateTax:.2f}")
print(f"\tTotal Deduction: ${totalDeduction:.2f}")
print(f"Net Pay: ${netPay:.2f}")

