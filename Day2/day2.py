# 1. Declare variables
first_name: str = "Nazar"
last_name = "Petrovskyi"
country = "Ukraine"
age = 28

# Check the data type of all variables
print(type(first_name))
print(type(last_name))
print(type(country))
print(type(age))


# 2. Find the length of your first name
first_name_length = len(first_name)
print("Length of first name:", first_name_length)


# 3. Compare the length of your first name and last name
if len(first_name) > len(last_name):
    print("My first name is longer than my last name.")
elif len(first_name) < len(last_name):
    print("My last name is longer than my first name.")
else:
    print("My first name and last name have the same length.")


# 4. Declare num_one and num_two
num_one = 5
num_two = 4


# 5. Addition
total = num_one + num_two
print("Total:", total)


# 6. Subtraction
diff = num_one - num_two
print("Difference:", diff)


# 7. Multiplication
product = num_two * num_one
print("Product:", product)


# 8. Division
division = num_one / num_two
print("Division:", division)


# 9. Modulus division
remainder = num_two % num_one
print("Remainder:", remainder)


# 10. Power
exp = num_one ** num_two
print("Exponent:", exp)


# 11. Floor division
floor_division = num_one // num_two
print("Floor division:", floor_division)


# 12. Circle calculations
import math

radius = 30

# Area of a circle
area_of_circle = math.pi * radius ** 2
print("Area of circle:", area_of_circle)

# Circumference of a circle
circum_of_circle = 2 * math.pi * radius
print("Circumference of circle:", circum_of_circle)


# 13. Take radius as user input and calculate the area
radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius ** 2
print("Area of the circle:", area)


# 14. Get first name, last name, country and age from the user
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))

print("First name:", first_name)
print("Last name:", last_name)
print("Country:", country)
print("Age:", age)
