from functions.run_python_file import run_python_file

print('Result "main.py":')
print(run_python_file("calculator", "main.py"))

print('Result "main.py "3+5" ":')
print(run_python_file("calculator", "main.py", ["3 + 5"]))

print('Result "tests.py":')
print(run_python_file("calculator", "tests.py"))

print('Result "../main.py":')
print(run_python_file("calculator", "../main.py"))

print('Result "nonexistent.py":')
print(run_python_file("calculator", "nonexistent.py"))

print('Result "lorem.txt":')
print(run_python_file("calculator", "lorem.txt"))
