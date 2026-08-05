# 1. Create a function that prints "Hello, World!".

def hello():
    print("Hello, World!")
hello()
# Output:
# Hello, World!


# 2. Create a function that prints your name.

def my_name(name):
    print("My name is", name)
my_name("Maniteja")
# Output:
# My name is Maniteja


# 3. Create a function that prints today's date.

from datetime import date

def today_date():
    print(date.today())
today_date()
# Output:
# 2026-08-05


# 4. Create a function that prints numbers from 1 to 10.

def numbers():
    for i in range(1, 11):
        print(i)
numbers()
# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10


# 5. Create a function that prints the multiplication table of 5.

def table():
    for i in range(1, 11):
        print(5, "*", i, "=", 5 * i)
table()
# Output:
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
# 5 * 6 = 30
# 5 * 7 = 35
# 5 * 8 = 40
# 5 * 9 = 45
# 5 * 10 = 50


# 6. Create a function that prints all even numbers from 1 to 20.

def even_numbers():
    for i in range(1, 21):
        if i % 2 == 0:
            print(i)
even_numbers()
# Output:
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20


# 7. Create a function that prints all odd numbers from 1 to 20.

def odd_numbers():
    for i in range(1, 21):
        if i % 2 != 0:
            print(i)
odd_numbers()
# Output:
# 1
# 3
# 5
# 7
# 9
# 11
# 13
# 15
# 17
# 19


# 8. Create a function that prints a square pattern of stars (4 × 4).

def square_pattern(n):
    for i in range(n):
        stars = ""
        for j in range(n):
            stars += "* "
        print(stars)
square_pattern(4)
# Output:
# * * * *
# * * * *
# * * * *
# * * * *


# 9. Create a function that prints a right-aligned triangle of stars.

def right_align(n):
    for i in range(1, n + 1):
        spaces = ""
        for j in range(n - i):
            spaces += "  "
        stars = ""
        for j in range(1, i + 1):
            stars += "* "
        print(spaces + stars)
right_align(5)
# Output:
#         *
#       * *
#     * * *
#   * * * *
# * * * * *


# 10. Create a function that prints the message "Welcome to Python Programming".

def message():
    print("Welcome to Python Programming")
message()
# Output:
# Welcome to Python Programming

# 11. Create a function that takes a name and prints a welcome message.

def welcome(name):
    print("Hello", name)
    print("Welcome to functions problem.")
welcome("Maniteja_Thumu")
# Output:
# Hello Maniteja_Thumu
# Welcome to functions problem.


# 12. Create a function that takes two numbers and prints their sum.

def add(a, b):
    print(a + b)
add(2, 3)
# Output:
# 5


# 13. Create a function that takes two numbers and prints their difference.

def difference(a, b):
    print(a - b)
difference(2, 3)
# Output:
# -1


# 14. Create a function that takes two numbers and prints their product.

def product(a, b):
    print(a * b)
product(2, 3)
# Output:
# 6


# 15. Create a function that takes two numbers and prints their division.

def division(a, b):
    print(a / b)
division(2, 3)
# Output:
# 0.6666666666666666


# 16. Create a function that takes a number and prints its square.

def square(n):
    print(n ** 2)
square(2)
# Output:
# 4


# 17. Create a function that takes a number and prints its cube.

def cube(n):
    print(n ** 3)
cube(2)
# Output:
# 8


# 18. Create a function that takes a number and checks whether it is even or odd.

def even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
even_odd(4)
# Output:
# Even

# 19. Create a function that takes a number and checks whether it is positive or negative.

def positive_negative(n):
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")
positive_negative(-1)
# Output:
# Negative

# 20. Create a function that takes a string and prints its length.
def string_length(text):
    print(len(text))
string_length("mani")
# Output:
# 4