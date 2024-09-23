'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#:
Description: Kilgram/pound conversion


NOTE: 1 kilogram is 2.2 lbs and 1 pound is .45 kilos
'''
#Output header
print(f"{'Kilograms':<10}{'Pounds':>10}{'|':^11}{'Pounds':<10}{'Kilograms'}")


lbs = 20 #counter for the pound amount

#Out put conversions
for i in range(1, 200, 2):
    print(f"{i:<10}{i * 2.2: 10.1f}{'|':^11}{lbs:<10}{lbs / 2.2: 10.2f}")
    lbs += 5
