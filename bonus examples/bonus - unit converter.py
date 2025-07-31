from bonus_modules import converters as unit_converter
from bonus_modules import parsers as unit_parser

feet_inches = input("Enter feet and inches: ")
feet, inches = unit_parser.parse_units(feet_inches)

result = unit_converter.convert_to_meters(feet, inches)
print(f"{feet} feet and {inches} inches are equal to {result} meters")
if result < 1:
    print("Kid is to small")
else:
    print("Kid OK")