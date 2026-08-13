# Section 1: Functions Without Parameters
# 1. Write a function welcome() that prints "Welcome to Python Programming".
def welcome():
    print("Welcome to Python Programming")
welcome()
#     
# 2. Write a function display_details() that prints your name, age, and city.
def display_details(name,age,city):
    print("My Name is",name,"age",age,"I am from",city)
display_details('Maniteja',20,'Karimnagar')
#  
# 3. Write a function show_even_numbers() that prints all even numbers from 1 to 20.
def show_even_numbers(n):
    for i in range(1,n+1):
        print(i)
show_even_numbers(20) 

# 4. Write a function multiplication_table() that prints the multiplication table of 5.
# Section 2: Functions With Parameters
def multiplication_table(n):
    for i in range(1,n+1):
        print(5,"*",i,"=",5*i)
multiplication_table(10)        
    
# 5. Write a function greet(name) that accepts a name and prints a greeting message.
# Example:
# Input: Ravi
# Output: Hello Ravi
def greet_message(name):
    print("HELLO",name)
greet_message('RAVI')

# 6. Write a function add(a, b) that accepts two numbers and prints their sum.
def add(a,b):
    print(a+b)
add(2,3)   

# 7. Write a function find_square(n) that accepts a number and prints its square.
def square():
    n=int(input("enter value: "))
    print(n**2)
square()    

# 8. Write a function find_greatest(a, b, c) that accepts three numbers and prints the greatest number.
def find_greatest(a, b, c):
    print(max(a, b, c))
find_greatest(10, 20, 30) 

# Section 3: Functions Using return
# 9. Write a function add(a, b) that accepts two numbers and returns their sum. Display the returned value outside the function.
def addition():
    a=int(input("enter A value: "))
    b=int(input("enter B value: "))
    print("Addition of a,b is",a+b)
addition()    

# 10. Write a function is_even(n) that returns True if the number is even and False otherwise.
def is_even(n):
    if n%2==0:
        print("even")
    else:
        print("odd") 
is_even(2)           
    
# 11. Write a function find_factorial(n) that calculates and returns the factorial of a number.
def find_factorial(n):
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i
    return factorial
print(find_factorial(5))

# 12. Write a function calculate_area(length, breadth) that returns the area of a rectangle.
def calculate_area(length, breadth):
    return length * breadth
print(calculate_area(2,3))

# Section 4: Positional Arguments
# 13. Create a function student_details(name, age, course) and call it using positional arguments.
def student_details(name, age, course):
    print("Student name is",name,"age",age,"course is",course)
student_details("MANITEJA",21,"CSE") 

# 14. Create a function calculate_bill(item, price, quantity) that returns the total bill amount.
# Call the function by passing all arguments positionally.
def calculate_bill(item,price,quantity):
    print("Your Item is",item,"of price",price,"quantity is",quantity)
calculate_bill("Biscuit",120,2) 
   
# 15. Create a function employee_details(name, department, salary).
# Call the function using positional arguments and display the employee details.
def employee_details(name, department, salary):
    print(name,"of department",department,"holding of salary",salary)
employee_details("Harshitha","IT",90000) 

# Section 5: Default Arguments
# 16. Create a function greet(name, message="Good Morning").
# Call the function:
def greet(name,message="Good Morining"):
    print("HELLO",name,message)
greet("MANITEJA","Good Evening") 

# By passing only the name.
def greet(name,message="Good Morining"):
    print("HELLO",name,message)
greet("MANITEJA")

# By passing both name and message.
def greet(name,message="Good Morining"):
    print("HELLO",name,message)
greet("MANITEJA","Good Morning")  

# 17. Create a function calculate_simple_interest(principal, rate=5, time=2) that returns simple interest.
# Call the function using:
# Only principal
def calculate_simple_interest(principal, rate=5, time=2):
    print((principal*rate*time)/100)
calculate_simple_interest(10000) 

# Principal and rate
def calculate_simple_interest(principal, rate=5, time=2):
    print((principal*rate*time)/100)
calculate_simple_interest(12000,5) 

# Principal, rate, and time
def calculate_simple_interest(principal, rate=5, time=2):
    print((principal*rate*time)/100)
calculate_simple_interest(12000,5,4)   

# Section 6: Keyword Arguments
# 18. Create a function student_details(name, age, course).
# Call the function using keyword arguments in a different order.
def student_details(name,age,course):
    print("Student name is",name,"age",age,"course is",course)
student_details(course="CSE",age=21,name="Maniteja")    

# 19. Create a function product_details(product, price, quantity) that returns the total price.
# Call the function using keyword arguments in different orders.
def product_details(product, price, quantity):
    print("product that u perchased is",product,"of price",price,"and quantity",quantity)
product_details (price=180000, quantity=1,product="IPHONE")    

# Section 7: Mixed Challenge — All Concepts
# 20. Create a function calculate_salary(name, basic_salary, bonus=5000).
# The function should:
# Accept name and basic_salary.
# Have a default value of 5000 for bonus.
# Calculate the total salary.
# Return the total salary.
def calculate_salary(name, basic_salary, bonus=5000):
    total_salary = basic_salary + bonus
    return total_salary
print(calculate_salary('MANITEJA',50000))

# Call the function once using positional arguments.
def calculate_salary(name,basic_salary,bonus):
    return name + " has a basic salary of " + str(basic_salary) + " and a bonus of " + str(bonus)
print(calculate_salary("MANITEJA",50000,5000))

# Call it again using keyword arguments.
def calculate_salary(name,basic_salary,bonus):
    return name + " has salary" + str(basic_salary) + "and bonus"+ str(bonus)
print(calculate_salary(basic_salary=50000,bonus=5000,name='MANITEJA'))

# Call it a third time by using the default value for bonus.
def calculate_salary(name="MANITEJA",basic_salary=50000,bonus=5000):
    return name + " has salary "+ str(basic_salary) + "and bonus" + str(bonus)
print(calculate_salary())

