# first_name: str = 'Asabeneh'

# print("".join(reversed(first_name)))

# one = "Thirty"
# two = "Days"
# three = "Of"
# four = "Python"

# concated_string = f"{one} {two} {three} {four}"

# print(concated_string)


# one = "Coding"
# two = "For"
# three = "All"

# concateneted = f"{one} {two} {three}"

# print(concateneted)

import numbers
from re import I


company = "Coding For All"

# print(len(company))

# uppercase = company.upper()

# print(uppercase)

# lower = company.lower()

# print(lower)

# print(company.lower())

# print(company.capitalize())

# print(company.swapcase())

# print(company.split()[0])

# print(company.find('Coding'))

# print(company.replace('coding', 'Python'))

# print(company.split())

# companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"

# print(companies.split(","))

# print("а"[5] if 5 < len("a") else None)

# print(len(company) - 1) # last index


# string = "Python For Everyone"

# print(''.join(word[0] for word in string.split()))

coding_for_all = "Coding For All"

# print(''.join(word[0] for word in coding_for_all.split()))

# print(coding_for_all.index('C'))
# print(coding_for_all.index('F'))


# print(coding_for_all.rfind('l'))

# str_to_slice = "You cannot end a sentence with because because because is a conjunction"

# print(str_to_slice[str_to_slice.index('because'):str_to_slice.rindex('because') + len('because')])


# print(coding_for_all.startswith('Coding'))

# print('   Coding For All      '.strip())


# print("30DaysOfPytho".isidentifier())

# print("thirty_days_of_python".isidentifier())

# list =  ' - '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'])

# print(list)

# print(f"8 + 6 = {8 + 6}")

# print("Hello \nNazar")
a: int = 8
b: int = 6

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {(a / b):.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")