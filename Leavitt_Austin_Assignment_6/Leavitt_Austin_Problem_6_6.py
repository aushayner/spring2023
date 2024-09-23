'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#:
Description: Display pattern

'''

#Create the main function
def main():
    #prompt the user to enter a line number value
    lineNumber = eval(input("Enter line number: "))

    #Invoke the displayPattern function
    displayPattern(lineNumber)

def displayPattern(n):

    #Nested for loop to iterate throught the pattern
    for row in range(1, n + 1):
        #print spaces
        for i in range(row, n):
            print(" ", end = "")

        #print the values
        for i in range(row, 0, -1):
            print(f"{i:3d}", end = "")

        #jump to newline
        print()

#invoke the main function
main()
