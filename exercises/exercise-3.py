# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer
while True:
    age_input = int(input("Input a dog's age in human years: "))

    if age_input == 911:
        break

    elif age_input <= 2:
	    dog_age = age_input * 10
    else:
	    dog_age = 20 + (age_input - 2)*7

    print("The dog's age in dog's years is", dog_age)
