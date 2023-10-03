import math

def areaTriangle(side1, side2, side3):
    
    if (side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2): 
        s = (side1 + side2 + side3) / 2
        area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
        return area
    else:
        raise ValueError("The input sides do not form a valid triangle.")

def main():
    side1 = float(input("Enter the length of side 1: "))
    side2 = float(input("Enter the length of side 2: "))
    side3 = float(input("Enter the length of side 3: "))
        
    area = areaTriangle(side1, side2, side3)
    print(f"The area of the triangle is: {area}")
main()
