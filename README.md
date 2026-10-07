# Distance Converter

Build a Python program that accepts distance measurements, performs conversions, and displays the results.

Before beginning, follow the repository setup instructions in [GITHUB_SETUP.md](GITHUB_SETUP.md).

## Learning Goals

By completing this assignment, you should be able to:

- Accept user input with `input()`.
- Convert input into numeric values.
- Store data in appropriately named variables.
- Perform calculations with arithmetic operators.
- Define and call a function.
- Display results using formatted strings.
- Write readable Python using meaningful names.

## Program File

Build your program in:

```text
distance_converter.py
```

## Requirements

Your program must perform both of the following conversions:

1. Convert **miles, feet, and inches** into a total number of **inches**.
2. Convert a total number of **inches** into **miles, feet, and remaining inches**.

Your program must also:

- Use `input()` to collect values from the user.
- Convert user input to integers.
- Store input and calculated values in variables.
- Define and call at least one function.
- Use at least one f-string when displaying output.
- Use clearly named variables instead of repeating unexplained numeric values throughout the program.

## Input Assumptions

For this assignment:

- All input values will be **whole numbers**.
- Inputs may be `0` or greater.
- You do not need to handle non-numeric input.
- You do not need to validate user input.

## Conversion Information

Use these conversion rates:

- 5,280 feet = 1 mile
- 12 inches = 1 foot

### Miles, Feet, and Inches → Inches

Prompt the user for the number of miles, feet, and inches.

Calculate the total number of inches represented by that distance.

The calculation can be represented as:

```text
total_inches = (5280 * 12 * miles) + (12 * feet) + inches
```

The formula is provided to clarify the required calculation. In your program, use clearly named variables for conversion values rather than relying on repeated magic numbers.

### Inches → Miles, Feet, and Inches

Prompt the user for a total number of inches.

Use arithmetic to determine:

- The number of whole miles.
- The number of whole feet remaining after the miles are removed.
- The number of inches remaining after the feet are removed.

Use arithmetic operators and the remainder operator (`%`) to perform the conversion.

## Constraint 

You should **not** use:

- `if` statements
- loops
- `try` / `except`
- lists or dictionaries
- imported libraries

These concepts are introduced later in the course.

## Sample Output

Your wording does not need to match this example exactly, but your program should clearly display each result.

```text
Welcome to the Distance Converter!
I am going to ask for your measured distance in miles, feet, and
inches and return the value to you in inches.
Input miles: 2
Input feet: 3
Input inches: 4
2 miles, 3 feet, and 4 inches is 126760 inches.

Now, we will convert inches to miles, feet, and inches.
Input inches: 23456
23456 inches is 0 miles, 1954 feet, and 8 inches.
```

## Submission

When your work is complete:

1. Commit and push your changes to your `development` branch.
2. Create a pull request from `development` into `main`.
3. Review the pull request.
4. Merge the pull request into `main`.
5. Submit the GitHub repository URL in Canvas.

See [GITHUB_SETUP.md](GITHUB_SETUP.md) for repository and pull-request instructions.
