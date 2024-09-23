'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#:
Description:


'''

#use the binary search fucntion to find the key in the list
def binarySearch(lst,key):

    #low will denote the first index
    low = 0

    #high will denote the last index
    high = len(lst) - 1

    #while loop to iterate through the list till key is found
    #or we exhausted all indexes
    while high >= low:

        #Denote the index of the middle element
        mid = (low + high) // 2

        #Check the first half of the list
        if key < lst[mid]:
            high = mid -1

        #If we have an exact match
        elif key == lst[mid]:
            return mid

        #Chick the second half of the list
        else:
            low = mid + 1

    #Return a nefative value to indicate that the key is not in the list
    #return where it should be placed in the list
    return -low - 1

#create a main function
def main():

    #create a list
    lst = [2, 4, 7, 9, 11, 45, 50, 59, 60, 66, 69, 73, 79]

    #invoke the binary search function with different key values
    i = binarySearch(lst, 2)
    j = binarySearch(lst, 73)
    k = binarySearch(lst, 6)

    #DISPLAY I,J,K
    print(f"Index for i is: {i}")
    print(f"Index for j is: {j}")
    print(f"Index for k is: {k}")

#invoke the main function
main()
