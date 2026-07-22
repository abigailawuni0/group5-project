# main.py - Shared entry point for our Team Project
# Each team member will add ONE line here to import and use their function.
# This file is intentionally shared so we can practice git pull + merge conflicts.

print("=== Welcome to our Git Collaboration Project ===")

# TODO: Student 1 - import and call get_greeting() here
from student1 import get_greeting
print(get_greeting("Student 1"))

# TODO: Student 2 - import and call add()/subtract() here
from student2_calculator import add,subtract
print(add(4,5))
print(subtract(10,3))

# TODO: Student 3 - import and call celsius_to_fahrenheit() here
from student3_temperature import celsius_to_fahrenheit
print(celsius_to_fahrenheit(0))
# TODO: Student 4 - import and call count_words() here

# TODO: Student 5 - import and call is_palindrome() here
