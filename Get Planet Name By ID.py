def get_planet_name(id):
    # This doesn't work; Fix it!
    x = str(id)

    diction =  {
        "1": "Mercury",
        "2": "Venus",
        "3": "Earth",
        "4": "Mars",
        "5": "Jupiter",
        "6": "Saturn",
        "7": "Uranus",
        "8": "Neptune"
    }

    return diction.get(x)


print(get_planet_name(3))