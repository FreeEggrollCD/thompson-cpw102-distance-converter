one_mile_in_inches:int = 63360

def distance_converter(distance_miles:int, distance_feet:int, distance_inches:int) -> int:
    total_inches:int = (5280 * 12 * distance_miles) + (12 * distance_feet) + distance_inches
    return total_inches

def distance_converterINCHES(inches_in:int) -> tuple:
    miles:int = inches_in // one_mile_in_inches
    feet:int = (inches_in % one_mile_in_inches) // 12
    inches:int = inches_in % 12
    return miles, feet, inches

def main():
    print("Please enter a value for the following distances: ")
    distance_miles:int = int(input("Miles: "))
    distance_feet:int = int(input("Feet: "))
    distance_inches:int = int(input("Inches: "))
    print(f"{distance_miles} miles, {distance_feet} feet, {distance_inches} inches")
    total:int = distance_converter(distance_miles, distance_feet, distance_inches)
    print("Here is the total distance in inches: ", total)
    print("Please enter a value for inches")
    inches:int = int(input("Inches: "))
    miles, feet, inches = distance_converterINCHES(inches)
    print(f"Here is the total distance in miles: {miles}, feet: {feet}, inches: {inches}")

main()