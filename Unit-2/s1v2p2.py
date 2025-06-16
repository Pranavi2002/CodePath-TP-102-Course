def planet_lookup(planet_name):
    if planet_name in planetary_info.keys():
        orbital_period = planetary_info[planet_name]["Orbital Period"]
        moons = planetary_info[planet_name]["Moons"]
        return f"Planet {planet_name} has an orbital period of {orbital_period} Earth days and has {moons} moons."
    else:
        return "Sorry, I have no data on that planet."

planetary_info = {
    "Mercury": {
        "Moons": 0,
        "Orbital Period": 88
    },
    "Earth": {
        "Moons": 1,
        "Orbital Period": 365.25
    },
    "Mars": {
        "Moons": 2,
        "Orbital Period": 687
    },
    "Jupiter": {
        "Moons": 79,
        "Orbital Period": 10592
    }
}

print(planet_lookup("Jupiter"))
print(planet_lookup("Pluto"))