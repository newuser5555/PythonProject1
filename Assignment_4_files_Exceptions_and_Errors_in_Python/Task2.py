user_input = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")
print("Data successfully written to output.txt.")

additional_input = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(additional_input + "\n")
print("Data successfully appended.")

with open("output.txt", "r") as file:
    content = file.read()
print("Final content of output.txt:")
print(content)
