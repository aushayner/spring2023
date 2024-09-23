'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: 5.2
Description: Generate 10 addition problems and tracking the correct answers

'''

#Import random and time modules
import random, time

correctCount = 0 # count the number of correct anwered questions
count = 0 # count the number of questions
MAX_QUESTIONS = 10 #Constant of the maximum questions


#Start the timer of the test
startTime = time.time()

#While loop to generate 10 different questions and prompt the user to
#answer the questions
while count < MAX_QUESTIONS:

    #1. Generate two random single digit integers
    number1 = random.randint(1,15)
    number2 = random.randint(1,15)
    

    #2. Prompt the student to enter their answer
    answer = eval(input(f"What is {number1} + {number2}? "))

    #3. Grade the question and display results
    if number1 + number2 == answer:
        print("\nYou are correct!")
        correctCount +=1
    else:
        print("Your answer is wrong!")
        print(f"{number1} + {number2} is {number1 + number2}")

    #Increment count
    #count +=1

    #prompt the user to enter Y to continue
    continueLoop = input("Enter Y to continue and N to quit:")
#Stop time and calculate overall time
endTime = time.time()
testTime = int(endTime - startTime)

#Display the results
print(f"Correct count is {correctCount} out of {MAX_QUESTIONS}.")
print(f"Test time is {testTime} seconds.")
