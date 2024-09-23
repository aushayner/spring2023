'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#:
Description: Display prime numbers between 2 and 1000 inclusive
Display eight numbers per line

'''
def main():
    number = 2
    index = 1
    while number < 1001:
        if isPrime(number):
            print(f"{number:3}",end = " ")
            index += 1
            if index % 8 == 0:
                print()
                index = 1
        number += 1
        
        
#Check whether a number is prime
def isPrime(number):
    diviser = 2
    while diviser <= number / 2:
        if number % diviser == 0:
            return False

        diviser += 1
    return True

main()
