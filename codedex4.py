earth_weight = float(input("Enter your weight on Earth (in kg): "))
planet_number = int(input("Enter the destination planet's number (1-7): "))

relative_gravity = 0.0
planet_name = ""
is_valid = True

if planet_number == 1:
    relative_gravity = 0.38
    planet_name = "Mercury"
elif planet_number == 2:
    relative_gravity = 0.91
    planet_name = "Venus"
elif planet_number == 3:
    relative_gravity = 0.38
    planet_name = "Mars"
elif planet_name == 4:
    relative_gravity = 2.53
    planet_name = "Jupiter"
elif planet_number == 5:
    relative_gravity = 1.07
    planet_name = "Saturn"
elif planet_number == 6:
    relative_gravity = 0.89
    planet_name = "Uranus"
elif planet_number == 7:
    relative_gravity = 1.14
    planet_name = "Neptune"
else:
    print("Invalid planet number.")
    is_valid = False

if is_valid:
    destination_weight = earth_weight * relative_gravity
    print(f"Your weight on {planet_name} would be {destination_weight:.2f} kg.")