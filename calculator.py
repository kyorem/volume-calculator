import math
game_start = "yes"
while game_start == "yes":
    print("what shape do you want to calculate the volume of")
    print("1.cylinder")
    print("2.cuboid")
    print("3.cube")
    print("4.pyramid")
    print("5.sphere")

    choice = input("Enter choice(1/2/3/4): ")
    if choice == "1":
        radius = float(input("Radius of cylinder: "))
        height = float(input("Height of cylinder: "))
        units = str(input("Unit of length: "))

        A = (math.pi * (radius ** 2) * height) + (2 * math.pi * (radius ** 2))

        round_A = round(A, 2)

        print("volume of cylinder is ", round_A, units, "cubed when the radius is ", radius, units,
              " and the height is ", height, units, ".")
    elif choice == "2":
        length = float(input("length of cuboid: "))
        breath = float(input("breath of cuboid: "))
        height = float(input("height of cuboid"))
        units = str(input("units of length: "))

        B = (length * breath * height)

        round_B = round(B, 2)

        print("volume of cylinder is ", round_B, units, "cubed when the length is ", length, units,
              " and the breath is ", breath, units, ".")
    elif choice == "3":
        length = float(input("length of cube: "))
        units = str(input("units of length: "))

        C = (length ** 3)

        round_C = round(C, 2)

        print("volume of cube is ", round_C, units, "cubed when the length is ", length, units)
    elif choice == "4":
        length = float(input("length of base in the pyramid"))
        breath = float(input("breath of base in the pyramid"))
        height = float(input("height of pyramid"))
        units = str(input("units of length: "))

        D = ((length * breath * height) / 3)

        round_D = round(D, 2)

        print("volume of pyramid is ", round_D, units, "cubed when the length is ", length, units,
              " ,the breath is ", breath, units, " and when the height is ", height, units)
    elif choice == "5":
        radius = float(input("radius of sphere"))
        units = str(input("units of radius"))

        E = ((4 * math.pi * (radius ** 3))/3)

        round_E = round(E, 2)

        print("volume of sphere is ", round_E, units, "cubed when the radius is ", radius, units,)

    game_start = input("do you want to calculate another shape's volume")



