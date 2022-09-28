# ===========================================================================
# -------------------------- Serializing an Object --------------------------
# ===========================================================================

# Depends on the pickle module for pickling and unpickling.
import pickle

# Data for testing (Graph of friends)
socialNetwork = {
    "Ahmed": {"Khalid", "Nora"},
    "Sara": {"Ali", "Lela", "Nora"},
    "Nora": {"Ahmed", "Ali", "Sara"},
    "Khalid": {"Ahmed", "Ali", "Fahad"},
    "Fahad": {"Khalid", "Lela", "Ali"},
    "Lela": {"Fahad", "Sara"},
    "Ali": {"Fahad", "Khalid", "Sara", "Nora"}
}

# For pickling: convert the object to bytes stream

# Step 1: Open a file with binary writing mode
file = open('socialNetwork.dat', "wb")

# Step 2: dump the object (write it to the file)
pickle.dump(socialNetwork, file)  # Receive the object want to write, and the file object

# Step 3: Close the file
file.close()

# For unpickling: convert the bytes stream to object

# Step 1: Open a file with binary read mode
file = open('socialNetwork.dat', "rb")

# Step 2: load the object (read it from the file)
object = pickle.load(file)  # Receive the file object and load first object exists (ERROR IF THERE'S NO OBJECT)


# Step 3: Close the file
file.close()

# NOTE: We could dump and load multiple objects
# For example: if you dump 2 objects to the same file, then you could read (load) them with the same order while dumping

# Prints the object after load it
for element in object.items():
    print(element)

# Output:
# ('Ahmed', {'Nora', 'Khalid'})
# ('Sara', {'Nora', 'Lela', 'Ali'})
# ('Nora', {'Ahmed', 'Sara', 'Ali'})
# ('Khalid', {'Fahad', 'Ahmed', 'Ali'})
# ('Fahad', {'Lela', 'Khalid', 'Ali'})
# ('Lela', {'Fahad', 'Sara'})
# ('Ali', {'Fahad', 'Nora', 'Khalid', 'Sara'}
