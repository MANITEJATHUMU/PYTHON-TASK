# <!-- Create a Python function named calculate_area that takes the radius of a circle as an argument and returns the area of the circle.
r=float(input('enter radius: '))
def circle_area():
    print(22/7*(r**2),"is area of circle")

# Implement another function named calculate_circumference that takes the radius of a circle as an argument and returns the circumference of the circle.
r=float(input('enter value: '))
def circumference():
    print(2*22/7*(r) ,"is circumference of circle")
   
# Write a main function named main where you call calculate_area and calculate_circumference with a radius of your choice and print the results.
def main():
    circle_area()  
    circumference()
main()    
