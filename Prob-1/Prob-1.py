# Module 3
#   Programming Assignment 4
#     Prob-1.py

# Tyler Johnson

def shippingCost(orderSubTotal):
    if orderSubTotal < 10.00:
        shipping = 2.99
        print("subtotal is:",orderSubTotal)
        print("2.99 shipping")
    
    else:
        shipping=0.00
        print("subtotal is:",orderSubTotal)
        print("Free shipping")

    return shippingCost

def unitTest():
    print("Shipping cost if subtotal < 10.00:\t", shippingCost(2.99))
    
    shippingCost(9.99)
    shippingCost(10.00)
    shippingCost(11.00)
    
if __name__ == "__main__":
    unitTest()