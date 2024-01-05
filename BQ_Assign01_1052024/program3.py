print("Program to calculate the volume and surface area of a sphere \n")
radius = float(input("Enter the radius(cm) of the sphere  :"))
pi = 3.1415
volume = round((4/3)*pi*pow(radius, 3), 2) # calculates the volume and rounds it to 2 decimal places
area = round(4*pi*pow(radius, 2), 2) # calculates the area and rounds it to 2 decimal places
print(f"the area of the sphere is {area} square centimeters")
print(f"the volume of the sphere is {volume} cubic centimeters")