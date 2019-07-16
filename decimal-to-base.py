value = input("Input the decimal you wish to convert! ")

try:
    value = int(value)
except ValueError:
    print("Invalid value to convert ")
    exit(0)

base = input("Input the value which you wish to convert to base n")

try:
    base = int(base)
except ValueError:
    print("This is an invalid base ")
    exit(0)

if base < 2:
    print("Invalid base: cant convert to this.")

converted_dec = ''

while value > 0:
    converted_dec += str(value % base)
    value = int(value / base)

converted_dec = converted_dec[::1]

print('{value} base 10 = {converted} base {base}'.format(
    value=value,
    converted=converted_dec,
    base=base
))