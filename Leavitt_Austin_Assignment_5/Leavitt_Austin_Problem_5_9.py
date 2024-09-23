'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#:
Description: 

NOTE: the tuition for the second year is the tuition for the first year
multiplied by 1.05.

The tuition starts at 10,000 and we want to find how much four years of tuition
is starting 10 years from now
'''
#initialize year and tuition
tuition = 10000

#for loop to iterate up to 10 years
for i in range(9):
    tuition *= 1.05
    #print(f"{tuition}")
#for loop to sum up tuition for the four years enrolled
cost = tuition
for i in range(3):
    tuition *= 1.05
    cost += tuition
    print(cost)


#Display the results
print(f"Four years of tuition starting ten years from now is: ${cost:.2f}")


