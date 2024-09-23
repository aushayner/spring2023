'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: 5.6
Description: convert miles to km and km to miles

NOTE: 1 mile is 1.609 km and 1 km is .621 mi
'''
#Output header
print(f"{'Miles':<10}{'Kilometers':>10}{'|':^11}{'Kilometers':<10}{'Miles'}")


km = 20 #counter for the pound amount

#Out put conversions
for i in range(1, 11):
    print(f"{i:<10}{i * 1.609: 10.3f}{'|':^11}{km:<10}{km / 1.609: 10.3f}")
    km += 5
