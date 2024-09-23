'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: 5.29
Description: Display all leap years from 2001 to 2100 ten per line

'''

# A year is a leap-year if it is divisible by
#four but not 100 or is divisible by 400
index = 1 # index for line length

#for loop iterates through every year in the range and determines
#whether that year is a leap year
for year in range (2001, 2101): 
    if(year % 4 ==0 and year % 100 != 0) or (year % 400 == 0):
        print(year, end = ' ')
        index += 1
        if index == 10: #print a new line if the index is now equal to 10
            index = 1
            print()
        
