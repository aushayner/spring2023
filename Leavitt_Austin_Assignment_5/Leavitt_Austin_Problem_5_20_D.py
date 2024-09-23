'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#:
Description:print pattern c

'''
#nested for loop to print out pattern
x = '  '
for i in range(7, -1, -1):
    print(x * i, end = '')
    for j in range(1, 7 - i):
        print(f"{j} ", end = '')
    print()
