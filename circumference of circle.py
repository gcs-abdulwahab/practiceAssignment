import math
def circum(radius):
    pi = math.pi
    circumference = 2 * pi*radius**2
    print("Circumference of a circle = ",  circumference)
    # it should return the circumference 
    # function name should be descriptive and result variable could be shortcase


radius = float(input("Enter radius of a circle "))

circum(radius)
