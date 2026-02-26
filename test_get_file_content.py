from functions.get_file_content import get_file_content

print("Result for current directory:")
print(get_file_content("calculator", "lorem.txt"))
print("Result for main directory:")
print(get_file_content("calculator", "main.py"))
print("Result for 'pkg' directory:")
print(get_file_content("calculator", "pkg/calculator.py"))
print("Result for '/bin' directory:")
print(get_file_content("calculator", "/bin/cat"))
print("Result for 'pkg/does_not_exist' directory:")
print(get_file_content("calculator", "pkg/does_not_exist.py"))