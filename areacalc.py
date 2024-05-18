
print("===============")
print("Area Calculator")
print("===============")
print()
print("1) Triangle")
print("2) Rectangel")
print("3) Square")
print("4) Circle")
print("5) Quit")
print()

area =0
err = False
shape = int(input("Which shape: "))
print()

if shape == 1:
    base = int(input("Base: "))
    height = int(input("Height: "))
    area = (height*base)/2
elif shape == 2:
    length = int(input("Length: "))
    width = int(input("Width: "))
    area = (length*width)
elif shape == 3:
    side = int(input("Side: "))
    area = (side**2)
elif shape == 4:
    radius = int(input("Radius: "))
    area = (3.14*radius**2)
elif shape == 5:
    quit()
else:
    print("ERROR")
    err = True


if err == True:
    quit()
else:
    print()
    print("The area is ",area)