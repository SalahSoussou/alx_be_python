FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5





def convert_to_celsius(fahrenheit):
    result = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print (f"({fahrenheit}°F is {result}°C")






def convert_to_fahrenheit(celsius):
    result = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    print (f"({celsius}°C is {result}°F")





temp = float(input("Enter the temperature to convert: "))
unit = str(input("Is this temperature in Celsius or Fahrenheit? (C/F):"))

if unit == "F":
    convert_to_celsius(temp)
elif unit == "C":
    convert_to_fahrenheit(temp)
else:
    print("unvalid unit")
    print("Invalid temperature. Please enter a numeric value.")