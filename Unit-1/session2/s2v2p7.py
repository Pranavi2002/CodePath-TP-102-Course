def highest_altitude(gain):
    altitude = 0
    max = 0
    for alt in gain:
        altitude = altitude + alt
        if max < altitude:
            max = altitude
    print(max)

gain = [-5, 1, 5, 0, -7]
highest_altitude(gain)

gain = [-4, -3, -2, -1, 4, 3, 2]
highest_altitude(gain)
