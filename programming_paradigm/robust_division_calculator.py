

def safe_divide(numerator, denominator):
    try:
            print(f"The result of the division is: {float(numerator)/float(denominator)}")
    except ZeroDivisionError:
            print("Cannot divide by zero.")
    except ValueError:
            print("Please enter numeric values only.")



        # if denominator == 0:
        #     raise ZeroDivisionError("Cannot divide by zero.")
        # else:


        #     if type(float(numerator)) != float or type(float(denominator)) != float :
