answer = input("1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n \nEnter an option: ")

if answer == "1":
    celsius_value = input("Kindly Input your celsius value: ")
    celsius_converted = float(celsius_value)
    fahrenheit = str((celsius_converted * (9.0 / 5.0)) + 32.0)
    print("Your celsius value " + celsius_value + " is " + fahrenheit + " degrees fahrenheit.")
elif answer == "2":
    fahrenheit_value = input("Input your Fahrenheit value: ")
    fahrenheit_converted = float(fahrenheit_value)
    celsius = str(((fahrenheit_converted - 32.0) * (5.0 / 9.0)))
    print("Your fahrenheit value " + fahrenheit_value + " is " + celsius + " degrees celsius.")
else:
    print("Not a right Input!")