name = input("What is your name? ")
age = int(input("What is your age? "))
favourite_food = input("What is your favourite food? ")
favourite_number = int(input("What is your favourite number? "))

print()
print("Hello,", name)
print("You are", age, "years old.")
print("Your favourite food is", favourite_food)
print("Your favourite number is", favourite_number)

if age >= 18:
    print("You are an adult.")
else:
    print("You are under 18.")

if favourite_number % 2 == 0:
    print("Your favourite number is even.")
else:
    print("Your favourite number is odd.")