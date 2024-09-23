'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#:
Description: print pattern b

'''

#nested for loop to print out pattern
for i in range(7, 0, -1):
    for j in range(1, i):
        print(f"{j} ", end = '')
    print()
