from functions.run_python_file import run_python_file

print("Result for calculator's usage instructions:")
print(run_python_file("calculator", "main.py")) 

print("Result for run the calculator:")
print(run_python_file("calculator", "main.py", ["3 + 5"]))

print("Result for run the calculator test:")
print(run_python_file("calculator", "tests.py"))

print("Result for '../main' directory:")
print(run_python_file("calculator", "../main.py"))

print("Result for nonexistet directory:")
print(run_python_file("calculator", "nonexistent.py"))
 
print("Result for not python file:")
print(run_python_file("calculator", "lorem.txt"))

