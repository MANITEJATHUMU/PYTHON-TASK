# 1. Area of Square
Side = 5
Area = Side * Side
print("Area of square is:", Area) 
 # Output: Area of square is: 25


# 2. Area of Rectangle
Length = 6
Breadth = 4
Area = Length * Breadth
print("Area of rectangle is:", Area)  
# Output: Area of rectangle is: 24


# 3. Area of Triangle
Base = 8
Height = 5
Area = (1 / 2) * Base * Height
print("Area of triangle is:", Area)  
# Output: Area of triangle is: 20.0


# 4. Perimeter of Square
Side = 6
Perimeter = 4 * Side
print("Perimeter of square is:", Perimeter) 
 # Output: Perimeter of square is: 24


# 5. Perimeter of Rectangle
Length = 5
Breadth = 3
Perimeter = 2 * (Length + Breadth)
print("Perimeter of rectangle is:", Perimeter) 
 # Output: Perimeter of rectangle is: 16


# 6. Perimeter of Triangle
Side1, Side2, Side3 = 5, 6, 7
Perimeter = Side1 + Side2 + Side3
print("Perimeter of triangle is:", Perimeter)  
# Output: Perimeter of triangle is: 18


# 7. Break Amount into 1000s, 500s, and Remaining Change
Amount = 3700
Thousands = Amount // 1000
Amount = Amount % 1000
FiveHundreds = Amount // 500
Remaining = Amount % 500
print("1000s:", Thousands, "500s:", FiveHundreds, "Remaining:", Remaining)  
# Output: 1000s: 3 500s: 1 Remaining: 200


# 8. Convert Seconds into Hours, Minutes, and Seconds
TotalSeconds = 3672
Hours = TotalSeconds // 3600
Remaining = TotalSeconds % 3600
Minutes = Remaining // 60
Seconds = Remaining % 60
print("Hours:", Hours, "Minutes:", Minutes, "Seconds:", Seconds)  
# Output: Hours: 1 Minutes: 1 Seconds: 12


# 9. Sum of Marks (Maths, Physics, Chemistry)
Maths = 85
Physics = 90
Chemistry = 88
Total = Maths + Physics + Chemistry
print("Total marks:", Total) 
# Output: Total marks: 263


# 10. Average of Marks (Maths, Physics, Chemistry)
Maths = 85
Physics = 90
Chemistry = 88
Average = (Maths + Physics + Chemistry) / 3
print("Average marks:", Average)  
# Output: Average marks: 87.66666666666667
