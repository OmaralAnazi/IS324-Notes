# ==============================================================================
# -------------------------- Reading Students Records --------------------------
# ==============================================================================

# Step 1: Open the file
file = open(r"student.txt")  # Open a new file with read mode [Default mode]


# Step 2: Process the file

# We use either for or while loop to read text file

# 1) Reading with while-loop:
records = []
line = file.readline()              # Read the line in the file (including '\n')
while line != "":                   # Stops until there's no more lines in the file ("" -> means we reach the end)
    line.strip()                    # Delete white spaces at the beginning or end (e.g., '\n')
    student = line.split()          # Split the line (record) into a list of elements (fields)
    gpa = float(student[2])         # Each field will be a str, but the gpa was float before, so we cast it since
    student[2] = gpa                # we know the index of it
    records.append(student)
    line = file.readline()          # Move to the next line

# 2) Reading with for-loop:
file.seek(0)                        # To make the file back at the starting point
records = []
for line in file:                   # will read each line in the file (including '\n')
    line.strip()                    # Delete white spaces at the beginning or end (e.g., '\n')
    student = line.split()          # Split the line (record) into a list of elements (fields)
    gpa = float(student[2])         # Each field will be a str, but the gpa was float before, so we cast it since
    student[2] = gpa                # we know the index of it
    records.append(student)


# Step 3: Close the file
file.close()

# Prints the information (both for and while loops gives the same output)
for student in records:
    print(student)

# Output:
# ['100', 'Ali', 3.4, 'IS']
# ['200', 'Ahmed', 2.5, 'CS']
# ['300', 'Khalid', 3.9, 'IS']
# ['400', 'Nasser', 4.7, 'SE']
# ['500', 'Jamal', 4.5, 'CS']


# -------------------------- Another Way for Reading a Text --------------------------

# Step 1: Open the file
file = open("student.txt")  # Open a new file with read mode [Default mode]

# Step 2: Process the file
output = file.read()        # Will read the whole text of the file

# Step 3: Close the file
file.close()

# Prints the information (both for and while loops gives the same output)
print(output)

# Output:
# 100 Ali 3.4 IS
# 200 Ahmed 2.5 CS
# 300 Khalid 3.9 IS
# 400 Nasser 4.7 SE
# 500 Jamal 4.5 CS
