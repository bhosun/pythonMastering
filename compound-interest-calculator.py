principal = input("Kindly Input your principal! ")

try:
    principal = float(principal)
except ValueError:
    print("Invalid principal amount")
    exit(0)

rate = input("Kindly Input the rate you want!: ")

try:
    rate = float(rate)
except ValueError:
    print("Invalid Rate")
    exit(0)

years = input("Kindly Input the Number of years you want it to work!: ")

try:
    years = int(years)
except ValueError:
    print("Invalid number of years: ")
    exit(0)

if principal <= 0 or rate <= 0 or years <= 0:
    print("Invalid Principal, or rate or number of years!!")
    exit(0)

year = 1
while year <= years:
    interest = (principal * rate) / 100
    print("Year {year}".format(
        year=year
    ))
    print("Compound Interest: {interest}".format(
        interest=interest
    ))
    principal += interest
    print("Principal amount: {principal}".format(
        principal=principal
    ))
    year += 1
print(" ")
