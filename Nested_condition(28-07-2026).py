# 1. Write a program to check whether a person is eligible to vote. If the person's age is 18 or above, check whether they have a voter ID.

age = 18
voter_id = True

if age >= 18:
    if voter_id == True:
        print("Eligible to vote")
    else:
        print("Invalid voter ID")
else:
    print("Not eligible to vote")

# Output:
# Eligible to vote


# 2. Write a program to check whether a student has passed. If the student scores 35 or more, check if the marks are 75 or above. Display "Distinction" or "Pass" accordingly.

marks = 36

if marks >= 35:
    if marks >= 75:
        print("Distinction")
    else:
        print("Pass")
else:
    print("Fail")

# Output:
# Pass


# 3. Write a program to check whether a user can log in. If the username is correct, check whether the password is correct.

username = "mani"
password = 1234

if username == "mani":
    if password == 1234:
        print("Login successful")
    else:
        print("Invalid password")
else:
    print("Login failed")

# Output:
# Login successful


# 4. Write a program to check whether a person can drive. If the age is 18 or above, check whether they have a valid driving license.

age = 18
driving_id = True

if age >= 18:
    if driving_id == True:
        print("Eligible to drive")
    else:
        print("Invalid driving license")
else:
    print("Not eligible to drive")

# Output:
# Eligible to drive


# 5. Write a program to check ATM withdrawal. If the account balance is greater than or equal to the withdrawal amount, check whether the withdrawal amount is within the daily limit.

balance = 3000
withdrawal_amount = 1500
daily_limit = 2000

if balance >= withdrawal_amount:
    if withdrawal_amount <= daily_limit:
        print("Cash can be withdrawn")
    else:
        print("Withdrawal exceeds daily limit")
else:
    print("Withdrawal not possible")

# Output:
# Cash can be withdrawn

# 6. Write a program to determine an employee's bonus. If the employee has worked for at least 5 years, check if the performance rating is "Excellent".

employee_exp = 6
performance = "Excellent"

if employee_exp >= 5:
    if performance == "Excellent":
        print("Higher bonus granted")
    else:
        print("Standard bonus")
else:
    print("Better luck next time")

# Output:
# Higher bonus granted


# 7. Write a program to determine whether a student is eligible for a scholarship. If the student's attendance is at least 75%, check whether the marks are 90 or above.

attendance = 71
marks = 94

if attendance >= 75:
    if marks >= 90:
        print("Eligible for scholarship")
    else:
        print("Marks are below scholarship criteria")
else:
    print("Not eligible")

# Output:
# Not eligible


# 8. Write a program to check admission eligibility. If the candidate has passed the entrance exam, check whether their age is between 17 and 25.

entrance_exam = "Pass"
age = 20

if entrance_exam == "Pass":
    if age > 17 and age < 25:
        print("Eligible for admission")
    else:
        print("Age doesn't match the criteria")
else:
    print("Not eligible for admission")

# Output:
# Eligible for admission


# 9. Write a program to determine whether an online order qualifies for free delivery. If the purchase amount is at least ₹1000, check whether the customer is a premium member.

amount = 1000
premium_member = True

if amount >= 1000:
    if premium_member == True:
        print("Free delivery on your order")
    else:
        print("You are not a premium member")
else:
    print("No free delivery")

# Output:
# Free delivery on your order


# 10. Write a program to check if a bank loan can be approved. If the applicant's salary is at least ₹30,000, check whether their credit score is 750 or above.

salary = 22000
credit_score = 782

if salary >= 30000:
    if credit_score >= 750:
        print("Bank loan approved")
    else:
        print("Low credit score")
else:
    print("Sorry, we can't approve the loan")

# Output:
# Sorry, we can't approve the loan


# 11. Write a program to determine a movie ticket price. If the person is a student, check whether they are under 18 to provide an additional discount.

person = "student"
age = 17

if person == "student":
    if age < 18:
        print("Additional discount granted")
    else:
        print("Student ticket only")
else:
    print("No discount")

# Output:
# Additional discount granted


# 12. Write a program to determine hostel eligibility. If the student belongs to another city, check whether hostel rooms are available.

other_city = True
rooms_available = True

if other_city == True:
    if rooms_available == True:
        print("Eligible for hostel")
    else:
        print("Hostel is full")
else:
    print("Hostel not required")

# Output:
# Eligible for hostel


# 13. Write a program to determine promotion eligibility. If an employee has completed at least 3 years of service, check whether the performance rating is at least 4.

service = 4
performance = 5

if service >= 3:
    if performance >= 4:
        print("Eligible for promotion")
    else:
        print("Performance improvement is required")
else:
    print("Better luck next time")

# Output:
# Eligible for promotion


# 14. Write a program to check exam eligibility. If attendance is at least 75, check whether the assignment marks are at least 40.

attendance = 80
assignment_marks = 50

if attendance >= 75:
    if assignment_marks >= 40:
        print("Eligible for exam")
    else:
        print("Assignment marks are low")
else:
    print("Not eligible for exam")

# Output:
# Eligible for exam