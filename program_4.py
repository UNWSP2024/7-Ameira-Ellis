# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.

# Now write a mainline that has the user enter the two tuples.  
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.  
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2) 
import math

def main():
    try:
        # Get first coordinate from user
        x1 = float(input("Enter x1 coordinate: "))
        y1 = float(input("Enter y1 coordinate: "))
        z1 = float(input("Enter z1 coordinate: "))
        point1 = (x1, y1, z1)

        # Get second coordinate from user
        x2 = float(input("Enter x2 coordinate: "))
        y2 = float(input("Enter y2 coordinate: "))
        z2 = float(input("Enter z2 coordinate: "))
        point2 = (x2, y2, z2)

        # Calculate distance
        distance = calculate_distance(point1, point2)

        # Display the distance
        print(f"The distance between points {point1} and {point2} is: {distance:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values for coordinates.")
def calculate_distance(coord1, coord2):
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    return distance
if __name__ == "__main__":
    main()

    