# Module 3
#   Programming Assignment 4
#     Prob-3.py

# Tyler Johnson


def letterGrade(score):
    score=0
    score=eval(input("Enter a score between 0 and 5: "))
    if score == 5:
        letterGrade="A"
        print("This is your grade: ",letterGrade)
        return letterGrade
    elif score ==4:
        letterGrade="B"
        print("This is your grade: ",letterGrade)
        return letterGrade
    elif score == 3:
        letterGrade="C"
        print("This is your grade: ",letterGrade)
        return letterGrade
    elif score == 2:
        letterGrade ="D"
        print("This is your grade: ",letterGrade)
        return letterGrade
    elif score==1:
        letterGrade = "F"
        print("This is your grade: ",letterGrade)
        return letterGrade
    elif score ==0:
        letterGrade = "F"
        print("This is your grade: ",letterGrade)
        return letterGrade
    else:
        print("Invalid input")
        return oops
    return letterGrade

def oops():
    exit
oops()  

  
def unitTest():
    letterGrade(0)
    letterGrade(1)
    letterGrade(2)
    letterGrade(3)
    letterGrade(4)
    letterGrade(5)
    
    
    
if __name__ == "__main__":
    unitTest()
    