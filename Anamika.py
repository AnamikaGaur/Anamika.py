from math import pi
a = float(input("The Radius of a Circle is:"))
print(" The area of a circle with radius " + str(a) + " is : " + str(pi*a**2))       
          

filename = input("Input the Filename: ")
f_extns = filename.split(".")
print("The extension of the file is : " + repr(f_extns[-1]))
