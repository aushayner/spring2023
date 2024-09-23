'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#:5.4
Description: Miles to kilometers

'''

#Output header
print(f"{'Miles':<10}{'Kilometers':>10}")

#Out put conversions from 1 - 10 using a for loop
for i in range(1, 11):
    print(f"{i:<10}{i * 1.609: 10.3f}")
