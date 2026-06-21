"""
Program: Lab8_johnson-2.py
Author: Jaylen Johnson
Purpose: Geometry Calculator that calculates circle and rectangle measurements using imported modules.
Starter code: No starter code was used.
Date: 6/21/2026
"""

import circle as c
import rectangle as r
# Aliases are necessary because both modules contain a function
# named calc_area(). Using aliases lets us specify which module's
# calc_area() function we want to call.

while True:
    print("\nGeometry Calculator")
    print("-------------------")
    print("1. Calculate Circle Area")
    print("2. Calculate Circle Circumference")
    print("3. Calculate Rectangle Area")
    print("4. Calculate Rectangle Perimeter")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")
    if choice == "1":
        radius = float(input("\nEnter the radius of the circle: "))
        area = c.calc_area(radius)
        print(f"\nThe area of the circle is {area:.3f}.")
        input("\nPress Enter to continue...")
    
    elif choice == "2":
        radius = float(input("\nEnter the radius of the circle: "))
        circumference = c.calc_circumference(radius)
        print(f"\nThe circumference of the circle is {circumference:.3f}.")
        input("\nPress Enter to continue...")

    elif choice == "3":
        width = float(input("\nEnter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))

        area = r.calc_area(width, height)

        print(f"\nThe area of the rectangle is {area:.1f}.")
        input("\nPress Enter to continue...")
    
    elif choice == "5":
        print("\nGoodbye!")
        break
    