'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#:
Description: Conversion from kilograms to pounds

'''
#Output header
print(f"{'Kilograms':<10}{'Pounds':>10}")

#Out put 200 conversions using a for loop
for i in range(1,200):
    print(f"{i:<10}{i * 2.2: 10.1f}")
