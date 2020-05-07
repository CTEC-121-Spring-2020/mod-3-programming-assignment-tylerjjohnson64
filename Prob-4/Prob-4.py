# Module 3
#   Programming Assignment 4
#     Prob-4.py

# Tyler Johnson 

# Author: Bruce Elgort
# Date: July 12, 2017

"""
The Elgorte coffee shop sells coffee at $16.50 a pound
plus the cost of shipping. Each order ships for $0.76
per pound plus $1.25 fixed cost for overhead. If the
number of pounds of the coffee order exceeds 10, then
the shipping cost is waived. Write a program that
calculates the cost of an order. Name your function
coffeeProcessor()
"""

def coffeeProcessor():

    # define variables
    overHead = 1.25
    quantity = 0.00 #quantity intitialized 
    priceOfCoffee = 16.50
    shippingPerPound = 0.00 #created shipping variable 

    quantity = eval(input("How many pounds of coffee would you like to order? ")) #missing end quotation, function is eval not evaluate and needed extra parenthethis 
    
    if quantity < 10.00:
        shippingPerPound = .76
    elif quantity == 10.00:  #double ==, setting variable directly equal to 10.00 float value 
        shippingPerPound = .76
    else: 
        shippingPerPound = 0      

    costOfOrder = ((quantity * priceOfCoffee) + ((quantity * shippingPerPound) + overHead)) #quantity misspelled, quotations around overhead addition  

    # Print result
    print("The cost of the order is:",costOfOrder) # missing front quotation 

# start the program
coffeeProcessor() #deleted go