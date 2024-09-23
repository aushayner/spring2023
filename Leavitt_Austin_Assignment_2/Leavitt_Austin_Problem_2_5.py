'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: 2.5
Description: This programs will calculate tips using an input subtotal and
gratuity rate

'''

#get input for subtotal and gratuity rate
subtotal, gratuityRate = eval(input("Enter the subtotal and gratuity rate: "))

#calculate the gratuity
gratuity = (gratuityRate/100) * subtotal

#calculate the total
total = subtotal + gratuity

#ouput the results
print(f"The gratuity is {round(gratuity, 2)} and the total is {round(total, 2)}")
