import csv

with open('employeedata.csv', 'r') as fp:
    datainfile = csv.reader(fp)
    data = list(datainfile)  # Read data into a list
    clean_data = [row for row in data if row]  # Remove empty rows

# Extract employee IDs
empid = [row[0] for row in clean_data[1:]]  # Skip the header row

# Get the employee ID to delete
e = input('Enter Employee ID: ')

if e not in empid:
    print('Employee ID not found')
else:
    # Find and remove the row with the matching employee ID
    for i in range(1, len(clean_data)):  # Start from 1 to skip the header
        if clean_data[i][0] == e:
            print(f"Deleting record for Employee ID: {e}")
            clean_data.pop(i)
            break

# Write updated data back to the file
with open('employeedata.csv', 'w', newline='') as fp:
    csvwriter = csv.writer(fp)
    csvwriter.writerows(clean_data)

# Print the cleaned data
for row in clean_data:
    print(row)
