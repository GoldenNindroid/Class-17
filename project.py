x = input("Enter your age: ")
try:
    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")

except ValueError as er:
    print("Exception: ", er)

except:
    print("Wrong Input")