# Ask for a number from the user
number = int(input("Enter a number for the times table: "))

# Calculate and print the times table for the entered number up to 12
for i in range(1, 1001):
    #Concatenation of strings and type casting of integer to string
    print(str(7) + " x " + str (i) + " = " + str(number * i))