def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Adam")  # Output: Hello, Adam!
say_hello("Eve")    # Output: Hello, Eve!
say_hello("John")   # Output: Hello, John!

def introduce(name, age):
    print("My name is", name)
    print("I am", age, "years old.")

introduce("Adam", 25)

def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)  # Output: 8

answer = add_numbers(10, 15)

double = answer * 2

print(double)  # Output: 50


def calculate_area(length, width):
    area = length * width
    return area

area = calculate_area(5, 10)
print(area)  # Output: 50

def is_adult(age):
    if age >= 18:
        return True
    else:
        return False

print(is_adult(25))  # Output: True
print(is_adult(15))  # Output: False