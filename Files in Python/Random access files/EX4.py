with open("myname.txt", "rb") as file:
    file.seek(10)  # Moves the pointer to the 10th byte from the beginning
    print(file.tell())  # Outputs: 10
    file.seek(-5, 2)  # Moves the pointer to 5 bytes before the end of the file
    print(file.tell())
    file.seek(5, 1)  # Moves the pointer 5 bytes forward from the current position
    print(file.tell())
    file.seek(-3, 1)  # Moves the pointer 3 bytes backward from the current position
    print(file.tell())
    file.seek(-10, 2)  # Moves the pointer to 10 bytes before the end of the file
    print(file.tell())
    file.seek(10, 1)  # Moves the pointer to the 10th byte from the start
    print(file.tell())


