# Comparison Operators (==, !=, >, <, >=, <=)

# Q1. Rahul scored 78 marks. The passing mark is 35. Write a Python expression to check whether Rahul passed.

passing = 35
rahul_marks = 78
print(rahul_marks > passing)  # Output: True


# Q2. A movie ticket is allowed only for people aged 18 or above. A person's age is 16. Write an expression to check if they are eligible.

age = 18
person = 16
print(person >= age)  # Output: False


# Q3. A laptop costs ₹55,000. Your budget is ₹60,000. Check whether the laptop is within your budget.

cost = 55000
budget = 60000
print(budget > cost)  # Output: True


# Q4. There are 25 students in Class A and 25 students in Class B. Write an expression to check whether both classes have the same number of students.

a = 25
b = 25
print(a == b)  # Output: True


# Q5. The temperature today is 42°C. Check whether the temperature is greater than 40°C.

today_temp = 42
actual = 40
print(today_temp > actual)  # Output: True


# Q6. A customer entered the correct OTP 5678. The entered OTP is 6789. Write an expression to check whether the OTP is incorrect.

correct = 5678
entered = 6789
print(correct != entered)  # Output: True


# Q7. The speed limit is 80 km/h. A car is moving at 80 km/h. Check whether the car is following the speed limit.

speed_limit = 80
car_moving = 80
print(speed_limit == car_moving)  # Output: True


# Q8. A train has 150 seats. Currently, 145 seats are booked. Check whether all seats are filled.

seats = 150
booked = 145
print(seats == booked)  # Output: False


# Q9. The minimum balance required in a bank account is ₹1000. Current balance is ₹850. Check whether the balance is less than the required amount.

min_bal = 1000
current = 850
print(min_bal > current)  # Output: True


# Q10. A student needs at least 75% attendance. Current attendance is 75%. Check whether the student is eligible for the exam.

attendence_atleast = 75
current = 75
print(attendence_atleast == current)  # Output: True


# Logical Operators (and, or, not)

# Q11. A student can attend the placement drive only if: CGPA is 7.5 or above AND Attendance is 75% or above. Current CGPA = 8.1, Attendance = 82%. Write the condition.

CGPA = 7.5
Attendence = 75
current_CGPA = 8.1
current_att = 82
print(current_CGPA > CGPA and current_att > Attendence)  # Output: True


# Q12. A customer gets free delivery if: Purchase amount is above ₹500 AND Customer is a Prime member. Purchase = ₹650, Prime Member = True. Write the condition.

off_purchase = 500
off_prime = True
person_pur = 650
person_prime = True
print(person_pur > off_purchase and person_prime == off_prime)  # Output: True


# Q13. A website allows login if: Username is correct OR Email is correct. Username Correct = False, Email Correct = True. Write the condition.

username = True
Email = True
entered_user = False
entered_mail = True
print(username == entered_user or Email == entered_mail)  # Output: True


# Q14. A cricket player is selected if: Runs > 500 AND Wickets > 20. Runs = 620, Wickets = 18. Write the condition.

Runs = 500
Wickets = 20
scored_runs = 620
scored_wickets = 18
print(scored_runs > Runs and scored_wickets > Wickets)  # Output: False


# Q15. A student passes only if: Theory marks ≥ 35 AND Practical marks ≥ 35. Theory = 40, Practical = 30. Write the condition.

Theory_marks = 35
Practical_marks = 35
Theory = 40
Practical = 30
print(Theory > Theory_marks and Practical > Practical_marks)  # Output: False


# Q16. A shop offers a discount if: Customer is a member OR total purchase exceeds ₹2000. Member = False, Purchase = ₹2500. Write the condition.

member = True
pur_exceeds = 2000
Member = False
Purchase = 2500
print(Member == member or Purchase > pur_exceeds)  # Output: True


# Q17. A person can vote if: Age is 18 or above AND is an Indian citizen. Age = 20, Citizen = True. Write the condition.

age = 18
citizen = True
Age = 20
Citizen = True
print(Age >= age and Citizen == citizen)  # Output: True


# Q18. A student is not absent. Absent = False. Write a Python expression using the not operator to check whether the student is present.

Absent = False
print(not (Absent != False))  # Output: True


# Q19. A system grants admin access only if: Username is "admin" AND Password is correct. Username = "admin", Password Correct = True. Write the condition.

Username = "admin"
Password = True
entered_user = "admin"
entered_pass = True
print(Username == entered_user and Password == entered_pass)  # Output: True


# Q20. A person can enter a swimming pool if: They have a membership OR they pay the entry fee. Membership = False, Paid Fee = False. Write the condition.

pool_membership = True
pool_fee = True
Membership = False
paid = False
print(pool_membership == Membership or pool_fee == paid)  # Output: False

# Mixed Comparison + Logical Operators

# Q21. A student gets Grade A if: Marks are between 90 and 100 (inclusive). Marks = 95. Write the condition.

Marks = 95
print(Marks >= 90 and Marks <= 100)  # Output: True


# Q22. A customer is eligible for cashback if: Purchase ≥ ₹1000 AND Purchase ≤ ₹5000. Purchase = ₹3200. Write the condition.

purchase = 3200
print(purchase >= 1000 and purchase <= 5000)  # Output: True


# Q23. A user can reset their password if: OTP is correct AND account is active. OTP Correct = True, Account Active = True. Write the condition.

OTP = True
active = True
entered_otp = True
entered_active = True
print(OTP == entered_otp and active == entered_active)  # Output: True


# Q24. A player qualifies if: Age is between 18 and 25 (inclusive). Age = 23. Write the condition.

Age = 23
print(Age >= 18 and Age <= 25)  # Output: True


# Q25. A vehicle is fined if: Speed > 80 km/h OR signal is broken. Speed = 75, Signal Broken = True. Write the condition.

speed = 81
signal = True
Speed = 75
Signal_broken = True
print(Speed >= speed or Signal_broken == signal)  # Output: True

# Challenge Questions

# Q26. Write a condition to check whether a number is between 10 and 50 (inclusive).

number = 21
print(number >= 10 and number <= 50)  # Output: True
number = 69
print(number >= 10 and number <= 50)  # Output: False


# Q27. Write a condition to check whether a person is either a student or a teacher.

person = "student"
print(person == "student" or person == "teacher")  # Output: True


# Q28. Write a condition to check whether a password length is at least 8 characters and contains at least one digit.

pass_length = 8
condition = True
print(pass_length >= 8 and condition == True)  # Output: True


# Q29. Write a condition to check whether a person's age is not less than 18.

person_age = 18
print(not (person_age < 18))  # Output: True


# Q30. A customer gets a gift only if: Purchase amount is greater than ₹5000 AND customer is a premium member AND today is their birthday. Write the condition using logical operators.

purchase = 4000
premium = True
Today_birthday = True
print(purchase > 5000 and premium == True and Today_birthday == True)  # Output: False