import math

def area(radius=None, length=None, width=None, side=None, height=None):
    if(radius):
        return math.pi * radius * radius

    elif(length and width):
        return length * width

    elif(side):
        return side*side

    elif(height and width):
        return (height * width)//2

print(f"Area of Square withe side 5 is {area(side=5)} unit sq.")
print(f"Area of Circle with radius 7 is {area(radius=7)} unit sq.")
print(f"Area of Recyangle with length 12 and width 4 is {area(length=12, width=4)} unit sq.")
print(f"Area of Triangle with height 4 and width 2 is {area(height=4, width=2)} unit sq.")