salary = input("Kindly Input how much you earn ")

try:
    salary = float(salary)
except ValueError:
    salary = -1

if salary < 0:
    print("Invalid Amount ")
elif salary < 50000:
    print("Basic Earner ")
elif  salary < 200000:
    print("Mid-Earner ")
else:
    print("High earner ")