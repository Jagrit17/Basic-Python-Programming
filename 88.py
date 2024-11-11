# Question 88: Importing Modules Dynamically
import importlib

# Dynamically import the 'math_utils' module
math_utils = importlib.import_module('math_utils')

# Use the 'add' function from the dynamically imported module
result = math_utils.add(15, 30)
print(result)  
print("88. This code is written by Jagrit Ahuja ERP- 0221BCA142")
