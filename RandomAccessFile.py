# ======================================================================================
# -------------------------- Dealing with Random Access files --------------------------
# ======================================================================================

# The main idea of random access file, is using seek(position) and tell() methods.
# seek(position): go directly to the position (index) in the file
# tell(): to tell us what the current position we are in now
# So, the idea is to store each starting point of a record by using tell(), and then
# we could go for that position to read the record using seek(position)

def writeToFile(path, mapping, records):
    file = open(path, "w")
    for student in records:
        position = file.tell()          # Store the current position we want to start writing at
        id = student[0]                 # then, associate that position with the student id. And
        mapping[id] = position          # store that association in the dictionary
        for field in student:
            file.write(field + " ")     # Write each field separated with a white space (we know for sure all fields are
        file.write("\n")                # strings). Then end each record with '\n' to easily read each record later
    file.close()


def readFromFile(path, position):
    file = open(path, "r")
    file.seek(position)                 # Go to the specific position in the file
    record = file.readline().strip()    # Read that line (whole record) and delete the '\n'
    student = record.split()            # split the string into a list (no need to know # of attributes)
    return student


# Our data
student1 = ['100', 'Ali', 'IS']
student2 = ['200', 'Ahmed', '2.5', 'CS']
student3 = ['300', 'Khalid', '3.9', 'IS', 'undergrad']
student4 = ['400', 'Nasser', 'SE', 'grad']
student5 = ['500', 'Jamal', '4.5', 'CS']
records = [student1, student2, student3, student4, student5]
mapping = dict()    # We'll use this dictionary to associate each student id with its position in the file

# Write all the records
writeToFile("RandomAccessFile", mapping, records)

# Read random record
index = "300"  # the student id
randomStudent = readFromFile("RandomAccessFile", mapping[index])

# Prints the retrieved student
print(randomStudent)
