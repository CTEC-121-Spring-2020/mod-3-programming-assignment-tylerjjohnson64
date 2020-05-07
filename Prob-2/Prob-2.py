# Module 3
#   Programming Assignment 4
#     Prob-2.py

# <YOUR NAME>

'''
Your IPO comment goes here
'''
from math import *
def main():
    # your code goes here
    wage=0
    overtimewages=0
    overtime=0
    regularwages=0
    TotalTakeHome=0
    name=input("Enter your name: ")
    wage=eval(input("Enter your hourly wage: "))
    hours=eval(input("How many hours did you work: "))
    if hours > 40:
        overtime= (hours-40)
        hours=40

    overtimewage=(wage*1.5)
    tax = .20
    medical = .10
    regularwages=(wage*hours)
    overtimewages=(overtime * overtimewage)
    totalwages= (overtimewages + regularwages)
    taxwithheld= (totalwages*tax)
    medicalwithheld=(totalwages*medical)
    TotalTakeHome=((totalwages-taxwithheld)-medicalwithheld)
    print("Employee name:",name)
    print("Hourly Wage:" ,wage)
    print("Normal Hour Wages:",regularwages)
    print("Overtime Wages:",overtimewages)
    print("Total Wages:",totalwages)
    print("Taxes Withheld:",taxwithheld)
    print("Medical Withheld:",medicalwithheld)
    print("Total Take Home:",TotalTakeHome)
    print()
    

main()