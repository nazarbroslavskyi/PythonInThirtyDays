# arr = ['Nazar', 'Olia', 'Nastya', 'Oleg']
# print('Naztar' in arr)

#1

# age: int = 5

#2

# height: float = 178.4

#3

# z = complex(3, 2)

#4

# def triangle_area (base: float, height: float) -> float:
#     return 0.5 * base * height

# base: float = float(input('Enter base:'))
# height: float = float(input('Enter height:'))
# print('The area of the triangle is', triangle_area(base=base, height=height))

#5

# def triangle_perimeter(side_a: float, side_b: float, side_c: float) -> float:
#     return sum((side_a, side_b, side_c))

# a: float = float(input('Enter side a:'))
# b: float = float(input('Enter side b:'))
# c: float = float(input('Enter side c:'))

# print(triangle_perimeter(side_a = a, side_b = b, side_c = c))

#6


# a: float = float(input('Enter side a:'))
# b: float = float(input('Enter side b:'))

# perimeter: float = 2 * sum((a, b))
# area: float = a * b

# print('Perieter:', perimeter)
# print('Area:', area)

#7
# import math

# Point = tuple[float, float]

# def line_properties(m: float, b: float) -> tuple[float, float, float]:
#     # m - slope, x - intercept, y - intercep
#     slope: float = m
#     y_intercept: float = b
#     x_intercept: float = -b / m
    
#     return slope, x_intercept, y_intercept

# def slope_between(p1: Point, p2: Point) -> float:
#     (x1, y1), (x2, y2) = (p1, p2)
    
#     return (y2 - y1) / (x2 - x1)

# # --- Task 6: y = 2x - 2 ---
# slope6, x_int6, y_int6 = line_properties(2.0, -2.0)
# print(f"Slope:     {slope6}")   # 2.0
# print(f"x-intercept: {x_int6}")   # 1.0
# print(f"y-intercept: {y_int6}")   # -2.0


# str_1 = "python"
# str_2 = "dragon"
# str_to_find = "on"

# strings = [str_1, str_2]
# if all(str_to_find in s for s in strings):
#     print("It's present")
    
#14

# sentence = 'I hope this course is not full of jargon'
# str_to_find = 'jargon'

# print(str_to_find in sentence)

#15

# str_1 = "python"
# str_2 = "dragon"
# str_to_check = 'on'

# print(str_to_check not in str_1 and str_to_check not in str_2)


# print(type(str(float(len('python')))))

#19

# print(type("10") == type(10))

#21