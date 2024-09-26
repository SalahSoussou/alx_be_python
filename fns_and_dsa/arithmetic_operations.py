num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = str(input("Enter the operation (add, subtract, multiply, divide): "))

"num1, num2, operation"

def perform_operation(num1,num2,operation):
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                return"Cannot divide by zero."
            elif num2 != 0 :
                return num1 / num2
