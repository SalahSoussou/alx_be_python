

def safe_divide(numerator, denominator):
    try:
            return "The result of the division is {:.1f}".format(float(numerator)/float(denominator))
    except ZeroDivisionError:
            return "Error: Cannot divide by zero."
    except ValueError:
            return "Error: Please enter numeric values only."

