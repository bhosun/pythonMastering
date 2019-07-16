salary = input("Input your salary! ")

try:
    salary = float(salary)
except ValueError:
    salary = -1

if salary < 0:
    print("Invalid Amount ")
elif salary < 50000:
    print("Tax: {tax}".format(
        tax=(5 / 100) * salary
        ))
elif salary < 200000:
    print("Tax: {tax}".format(
        (10 / 100) * salary
        ))
else:
    print("Tax: {tax}".format(
        (15 / 100) * salary
        ))

