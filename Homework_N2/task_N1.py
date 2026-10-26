import math
a = float(input("Enter sida a "))
b = float(input("Enter side b"))
c = float(input("Enter side c"))

if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
   print("Triangle like this doesnt exist")
else:
    perimeter = a + b + c #Calculating perimeter
    p = perimeter / 2  # Semi perimeter for  area calculation
    area = math.sqrt(p * (p - a) * (p - b) * (p - c)) # Using heron's formula to calculate the area of the traingle
    print("Perimeter: ", perimeter)
    print("Area: " , area)