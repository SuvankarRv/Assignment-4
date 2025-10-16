
# Task 2: Write and Append Data to a File

data = input("Enter some data to write to the file: ")

with open("output.txt", "w") as file:
    file.write(data + "\n")

print("Data written to output.txt")

extra_data = input("Enter additional data to append to the file: ")

with open("output.txt", "a") as file:
    file.write(extra_data + "\n")

print("Additional data appended to output.txt")

with open("output.txt", "r") as file:
    content = file.read()

print("\nFinal content of output.txt:")
print(content)
