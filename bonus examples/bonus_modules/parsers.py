def parse_units(feet_and_inches):
    units = feet_and_inches.split(" ")
    feet = float(units[0])
    inches = float(units[1])

    return feet, inches