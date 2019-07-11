firstName = str(input("What is your firstName? "))
lastName = str(input("What is your lastName? "))
age = input("how old are you? ")
stringed_age = int(age)

year_of_birth = str(2019 - stringed_age)

print("Welcome " + firstName + " " + lastName + " (" + age + ")")
print("Welcome " + firstName + " " + lastName + " (" + year_of_birth + ")")

gender = str(input("What is your gender? "))
converted_gender = gender.lower()

if converted_gender == "male":
    print("Welcome " + firstName + " son of " + lastName + " (" + year_of_birth + ")")
else:
    print("Welcome " + firstName + " daughter of " + lastName + " (" + year_of_birth + ")")