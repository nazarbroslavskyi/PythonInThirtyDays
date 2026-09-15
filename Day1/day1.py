# print("Hello World")

# a: int = 5
# b: float = 5.6

# print(a + b)
def greet(name: str) -> str:
    return "Hello, " + name

print(greet("Py"))
print(greet('Nazar'))  # This should trigger a type error