import os

# Function 1: Safe function that calculates the sum of two numbers
def calculate_sum(a, b):
    print("calculating sum of two variables")
    return a + b

# Function 2: Vulnerable function that executes a shell command (injection risk)
def delete_file(filename):
    os.system(f"rm {filename}")

# Function 3: Safe function that checks if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

# Example usage
print("Sum of 10 and 20:", calculate_sum(10, 20))

file_to_delete = "important.txt; ls"  # Dangerous input!
delete_file(file_to_delete)

word = "racecar"
print(f"Is '{word}' a palindrome?", is_palindrome(word))
