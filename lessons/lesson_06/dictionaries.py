person = {
    "name" : "Adam",
    "age" : 25,
    "height" : 1.75,
    "likes_coding" : True
}

print(person)

person["age"] = 26

person["favourite_food"] = "Pizza"

del person["height"]

person.pop("likes_coding")

print(person["name"])  # Output: Adam
print(person["age"])   # Output: 26
print(person["favourite_food"])  # Output: Pizza

if "name" in person:
    print("The person has a name.")

if "email" in person:
    print(person["email"])
else:
    print("No email address found.")  # Output: No email address found.

for key in person:
    print(key)

for key, value in person.items():
    print(key, ":", value)


people = [
    {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    },
    {
        "name": "Bob",
        "age": 25,
        "city": "Los Angeles"
    },
    {
        "name": "Charlie",
        "age": 35,
        "city": "Chicago"
    }
]

for person in people:
    print(person["name"], person["age"])


product = {
        "name": "Laptop",
        "price": 999.99,
        "in_stock": True
    }

print(product["name"])
print(product["price"])

product["price"] = 899.99

product["rating"] = 4.5

if "in_stock" in product:
    print("The product is available.")

for key, value in product.items():
    print(key, ":", value)

products = [
    {
        "name": "Smartphone",
        "price": 699.99,
        "in_stock": True
    },
    {
        "name": "Tablet",
        "price": 399.99,
        "in_stock": False
    },
    {
        "name": "Headphones",
        "price": 199.99,
        "in_stock": True
    }
]

for product in products:
    print(product["name"], product["price"])