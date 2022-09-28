# ==============================================================================
# -------------------------- Writing Students Records --------------------------
# ==============================================================================

# Step 1: Open the file
file = open(r"student.txt", "w")    # Create a new file with write mode, The prefix 'r' for a
                                    # raw string (for ignoring any commands in the string like '\n')

# Step 2: Process the file

# Our Data:
student1 = ['100', 'Ali',    3.4, 'IS']
student2 = ['200', 'Ahmed',  2.5, 'CS']
student3 = ['300', 'Khalid', 3.9, 'IS']
student4 = ['400', 'Nasser', 4.7, 'SE']
student5 = ['500', 'Jamal',  4.5, 'CS']
records = [student1, student2, student3, student4, student5]

# Writing:
for student in records:
    sID = student[0]
    name = student[1]
    gpa = student[2]
    department = student[3]
    file.write(sID + " ")           # Write each field separated by " " to read easily later
    file.write(name + " ")
    file.write(str(gpa) + " ")      # Notice everything written as str, so float must be cast before.
    file.write(department + " ")
    file.write("\n")                # Ends the record to start the new record at the next line

# Step 3: Close the file
file.close()
