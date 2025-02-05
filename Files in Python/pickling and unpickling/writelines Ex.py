# program demonstrates the data to write (list)object data into file(secondary memory)
data = ["Hello, world!\n", "Python is fun.\n", "Learn to code!\n"]
with open("example_writelines.txt", "w") as file:
    file.writelines(data)
