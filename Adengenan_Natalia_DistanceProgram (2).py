import math

 # Ask the user to enter the coordinates of the first point
point_x1 = float=(input("Enter x1: "))
point_x2 = float=(input("Enter x2: "))
point_y1 = float=(input("Enter y1: "))
point_y2 = float=(input("Enter y2: "))
 
# Ask the user to enter the coordinates of the second point
point_x = point_x2 - point_x1
point_y = point_y2 - point_y1

# Compute the distance using the distance formula
point_xy = pow(point_x, 2) + pow(point_y, 2)
 
# Display the result rounded to two decimal places
distance = math.sqrt(point_xy)
print("The distance is ", distance)

