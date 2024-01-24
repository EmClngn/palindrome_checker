# Write a program to check if the given number is a palindrome number.

# pseudo code

# ask user for an input number
original = input("Please input your desired number: ")

# create an empty variable to hold the reverse number
reverse = ""
# use for loop to reverse
for i in range(len(original), 0, -1):
    reverse += original[i - 1]

# use if function to check if the number is a palindrome
if original == reverse:
    print("Yes,", original, "is a palindrome.")
else:
    print("No,", original, "is not a palindrome.")