def distance_converter(distance_miles, distance_feet, distance_inches):
    print(f"{distance_miles} miles, {distance_feet} feet, {distance_inches} inches")
    total_inches = (5280 * 12 * distance_miles) + (12 * distance_feet) + distance_inches
    return total_inches

def main():
    print("Please enter a value for the following distances: ")
    distance_miles = int(input("Miles: "))
    distance_feet = int(input("Feet: "))
    distance_inches = int(input("Inches: "))
    total = distance_converter(distance_miles, distance_feet, distance_inches)
    print("Here is the total distance in inches: ", total)

main()