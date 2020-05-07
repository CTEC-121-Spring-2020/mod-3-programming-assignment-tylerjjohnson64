# Module 3
#   Programming Assignment 4
#     Prob-5.py

# <YOUR NAME>

def main():
    try:
        x = eval(2)
        print("x:", x)
    except TypeError:
        print("You are using an incorrect parameter for Eval()")
        exit
    
main()