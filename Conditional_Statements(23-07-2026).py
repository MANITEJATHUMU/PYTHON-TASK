# 1. Check whether a number is positive, negative, or zero

num = 10
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

# Output: Positive


# 2. Check whether a number is even or odd

num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Output: Odd


# 3. Find the largest of two numbers

A = 5
B = 6

if A > B:
    print("A is Greater")
else:
    print("B is Greater")

# Output: B is Greater


# 4. Find the largest of three numbers

A = 5
B = 6
C = 7

if A > B and A > C:
    print("A is Greater")
elif B > A and B > C:
    print("B is Greater")
else:
    print("C is Greater")

# Output: C is Greater


# 5. Check whether a person is eligible to vote (age >= 18)

Age = 19

if Age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")

# Output: Eligible to vote


# 6. Assign grades based on marks (A, B, C, Fail)

Marks = 69

if Marks >= 90:
    print("Grade A")
elif Marks >= 70:
    print("Grade B")
elif Marks >= 50:
    print("Grade C")
else:
    print("Grade F")

# Output: Grade C


# 7. Check whether a character is vowel or consonant

value = "b"

if value == ("A" or "E" or "I" or "O" or "U"):
    print("Vowel")
else:
    print("Consonant")

# Output: Consonant


# 8. Check whether a number is divisible by both 3 and 5

num = 15

if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not Divisible")

# Output: Divisible by both 3 and 5


# 9. Check whether a character is uppercase, lowercase, digit, or special symbol

value = input("Enter a value: ")

if value.isupper():
    print("Uppercase")
elif value.islower():
    print("Lowercase")
elif value.isdigit():
    print("Digit")
else:
    print("Special symbol")

# Sample Output:
# Enter a value: 5
# Digit


# 10. Check whether a number is divisible by 7

num = 14

if num % 7 == 0:
    print("Divisible by 7")
else:
    print("Not divisible")

# Output: Divisible by 7


# 11. Check whether a person is a senior citizen (age >= 60)

Age = 59

if Age >= 60:
    print("Senior citizen")
else:
    print("Adult")

# Output: Adult


# 12. Check whether a year is a leap year

Year = 2024

if Year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")

# Output: Leap Year


# 13. Build a simple calculator (+, -, *, /)

A = int(input("Enter first value: "))
B = int(input("Enter second value: "))
operator = input("Enter operator: ")

if operator == "+":
    print(A + B)
elif operator == "-":
    print(A - B)
elif operator == "*":
    print(A * B)
elif operator == "/":
    print(A / B)

# Sample Output:
# Enter first value: 10
# Enter second value: 5
# Enter operator: +
# 15


# 14. Check whether a number is in range (1 to 100)

num = int(input("Enter Value: "))

if num > 1 and num < 100:
    print("In range")
else:
    print("Out of range")

# Sample Output:
# Enter Value: 1000
# Out of range


# 15. Input marks of 3 subjects and check pass/fail (>=35 each)

a = eval(input("Enter marks: "))
b = eval(input("Enter marks: "))
c = eval(input("Enter marks: "))

if a >= 35 and b >= 35 and c >= 35:
    print("Pass")
else:
    print("Fail")

# Sample Output:
# Enter marks: 67
# Enter marks: 87
# Enter marks: 90
# Pass


# 16. Check whether a number is a multiple of 3 and 5 (separately)

num = eval(input("Enter value: "))

if num % 3 == 0 and num % 5 == 0:
    print("Divisible by 3 & 5")
else:
    print("Not divisible")

# Sample Output:
# Enter value: 21
# Not divisible


# 17. Simulate ATM withdrawal (check sufficient balance)

amount = int(input("Enter amount: "))
balance = 15000

if amount <= balance:
    print("Withdrawal is possible")
else:
    print("Withdrawal is not possible")

# Sample Output:
# Enter amount: 14000
# Withdrawal is possible


# 18. Calculate tax based on salary slabs

# Code not provided.


# 19. Check whether a number is a 3-digit number

num = 100

if num >= 100 and num <= 999:
    print("Three digit")
else:
    print("Not a three digit")

# Output: Three digit


# 20. Check whether a character is an alphabet

char = "1"

if char.isalpha():
    print("It is an alphabet")
else:
    print("Not an alphabet")

# Output: Not an alphabet


# 21. Find the largest of three numbers using nested if

A = 3
B = 4
C = 5

if A > B and A > C:
    print("A is Greater")
if B > A and B > C:
    print("B is Greater")
else:
    print("C is Greater")

# Output: C is Greater


# 22. Create a login system (username & password check)

username = True
password = False

if username == True and password == True:
    print("Login successful")
else:
    print("Login failed")

# Output: Login failed


# 23. Check whether a number is positive, then check even/odd

num = 21

if num > 0 and num % 2 == 0:
    print("Positive and Even")
elif num > 0 and num % 2 != 0:
    print("Positive and Odd")
else:
    print("Negative")

# Output: Positive and Odd


# 24. ATM system with conditions (balance + withdrawal limit)

amount = int(input("Enter amount: "))
balance = 15000

if amount <= balance:
    print("Withdrawal is possible")
else:
    print("Withdrawal is not possible")

# Sample Output:
# Enter amount: 14000
# Withdrawal is possible


# 25. Student result system (Pass / First Class / Distinction)

Marks = 50

if Marks >= 75:
    print("Distinction")
elif Marks >= 60:
    print("First Class")
elif Marks >= 35:
    print("Pass")
else:
    print("Fail")

# Output: Pass