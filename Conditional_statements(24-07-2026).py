#1. Check Even or Odd
num = int(input("Enter the number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
# Input: 6  --> Output: Even number


#2. Divisible by 5 but Not by 10
number = int(input("Enter the number: "))
if number % 5 == 0 and number % 10 != 0:
    print("Satisfy")
# Input: 25 --> Output: Satisfy


#3. Biggest Among Two Numbers
a = 4
b = 7
if a > b:
    print("A is greater")
else:
    print("B is greater")
# Output: B is greater


#4. Smallest Among Two Numbers
a = 4
b = 7
if a < b:
    print("A is smallest")
else:
    print("B is smallest")
# Output: A is smallest


#5. Divisible by 2, 3, and 6
number = 18
if number % 2 == 0 and number % 3 == 0 and number % 6 == 0:
    print("Satisfy")
# Output: Satisfy


#6. Voting Eligibility
age = 19
if age >= 18:
    print("Eligible to vote")
# Output: Eligible to vote


#7. Student Pass/Fail Based on All Subjects >=35
maths = 40
physics = 36
chemistry = 30
if maths >= 35 and physics >= 35 and chemistry >= 35:
    print("Pass")
else:
    print("Fail")
# Output: Fail


#8. Student Pass if Passed Any One Subject
maths = 20
physics = 38
chemistry = 25
if maths >= 35 or physics >= 35 or chemistry >= 35:
    print("Pass")
else:
    print("Fail")
# Output: Pass


#9. Student Pass if Passed Any Two Subjects (YOUR LOGIC IS WRONG)

maths = 40
physics = 20
chemistry = 36

if (maths >= 35 and physics >= 35) or \
   (maths >= 35 and chemistry >= 35) or \
   (physics >= 35 and chemistry >= 35):
    print("Pass")
else:
    print("Fail")
# Output: Pass


#10. Biggest Among Three Numbers
a = 7
b = 4
c = 9
if a > b and a > c:
    print("A is biggest")
elif b > a and b > c:
    print("B is biggest")
else:
    print("C is biggest")
# Output: C is biggest


#11. Smallest Among Three Numbers
a = 7
b = 4
c = 9
if a < b and a < c:
    print("A is smallest")
elif b < a and b < c:
    print("B is smallest")
else:
    print("C is smallest")
# Output: B is smallest


#12. Perfect Square or Not
number = 49
root = int(number ** 0.5)
if root * root == number:
    print("Perfect square")
else:
    print("Not perfect square")
# Output: Perfect square


#13. Cars Required for Members
import math

members = 17
cars_needed = math.ceil(members / 5)
print("Cars needed =", cars_needed)
# Output: Cars needed = 4


#14. Second Biggest Among Three Numbers (YOUR LOGIC IS WRONG)

a = 10
b = 25
c = 18

if (a > b and a < c) or (a < b and a > c):
    print("A is second")
elif (b > a and b < c) or (b < a and b > c):
    print("B is second")
else:
    print("C is second")
# Output: C is second


#15. Leap Year or Not (YOUR LOGIC IS INCOMPLETE)

year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
# Output: Leap year