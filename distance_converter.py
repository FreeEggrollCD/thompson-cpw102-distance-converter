one_mile_in_inches = 63360

def distance_converter(distance_miles, distance_feet, distance_inches):
    print(f"{distance_miles} miles, {distance_feet} feet, {distance_inches} inches")
    total_inches = (5280 * 12 * distance_miles) + (12 * distance_feet) + distance_inches
    return total_inches

def distance_converterINCHES(inches):
    miles = inches // one_mile_in_inches
    feet = (inches % one_mile_in_inches) // 12
    inches = inches % 12
    return miles, feet, inches

def main():
    print("Please enter a value for the following distances: ")
    distance_miles = int(input("Miles: "))
    distance_feet = int(input("Feet: "))
    distance_inches = int(input("Inches: "))
    total = distance_converter(distance_miles, distance_feet, distance_inches)
    print("Here is the total distance in inches: ", total)
    print("Please enter a value for inches")
    inches = int(input("Inches: "))
    miles, feet, inches = distance_converterINCHES(inches)
    print(f"Here is the total distance in miles: {miles}, feet: {feet}, inches: {inches}")



main()